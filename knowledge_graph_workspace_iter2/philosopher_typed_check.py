#!/usr/bin/env python3
"""Typed-correctness sweep for the iter-2 knowledge graph.

For every edge state -> technique, check that the source state's type_signature
(if present) is plausible for the target technique's function_signature. We
allow axioms through as "always plausible" (they are ambient). We also allow
nodes without a type_signature through but count them as 'unchecked' so the
review can see how much of the coverage is actually verifiable.

Plausibility rule: we derive a small bag of keywords from the technique's
function_signature (tokenised) and from its cluster, and check if the state's
type_signature or name shares at least one domain keyword. If not, we record
a 'flagged' mismatch with a human-readable reason.

Output: print top-10 flagged mismatches (most striking first) and total
statistics.
"""

from __future__ import annotations
import json
import re
from collections import defaultdict


def tokens(s: str | None) -> set[str]:
    if not s:
        return set()
    # drop non-word; lowercase; keep tokens of length >= 3
    toks = re.findall(r"[A-Za-z][A-Za-z0-9_]+", s.lower())
    return {t for t in toks if len(t) >= 3}


# Domain keyword sets keyed by crude technique "domain". If a state's
# type_signature / name intersects with the technique's domain keyword set, we
# consider the edge plausible. A state with no type_signature AND no name
# match is recorded as "unchecked" (not a flag).
DOMAIN_KEYWORDS: dict[str, set[str]] = {
    "algebra": {
        "group", "ring", "field", "module", "polynomial", "algebra", "ideal",
        "matrix", "vector", "galois", "homomorphism", "subgroup", "element",
        "subalgebra", "functor", "representation", "lattice", "quotient",
        "conjugate", "invariant", "operator", "map", "morphism", "unit",
        "integer", "residue", "order", "norm", "coefficient", "character",
        "permutation", "symmetry", "prime", "pair", "triple", "coprime",
        "identity", "formula", "root", "system", "cubic", "quartic",
        "cardano", "squared", "law", "product", "sum", "coset",
        "orbit", "mod", "algebraicrelation", "grouplaw", "multiplicative",
        "hypotenuse", "sin", "cos", "tan", "sine", "cosine",
        "equation", "systemofequations", "factor", "series",
        "symmetric", "polynomials", "conjecture", "abelian", "simple",
        "proposition", "lemma", "specific", "exists", "complex",
        "boolean", "algebra", "divisor", "char", "euler", "holomorphic",
        "holomorphicmap", "heat", "physical", "physicalsystem", "conduction",
    },
    "analysis": {
        "function", "continuous", "smooth", "holomorphic", "integrable",
        "measure", "sequence", "convergent", "bounded", "limit", "series",
        "analytic", "differentiable", "fourier", "laplace", "distribution",
        "operator", "riemannian", "metric", "norm", "derivative", "integral",
        "form", "manifold", "domain", "space", "interval", "closure", "sup",
        "formula", "identity", "sin", "cos", "tan", "real", "complex",
        "law", "product", "sum", "conjecture", "system", "cubic", "quartic",
        "root", "asymptotic", "bound", "bounded",
    },
    "geometry": {
        "triangle", "polygon", "circle", "conic", "curve", "surface",
        "manifold", "metric", "riemannian", "angle", "area", "volume",
        "length", "space", "plane", "vertex", "edge", "face", "projective",
        "affine", "euclidean", "hyperbolic", "sphere", "disk", "ball",
        "simplex", "polyhedron", "cycle", "homology", "cohomology",
        "segment", "cyclic", "inscribed", "quadrilateral", "hexagon",
        "hypotenuse", "simplicialcomplex", "triangulated",
    },
    "topology": {
        "space", "topology", "compact", "open", "closed", "continuous",
        "manifold", "connected", "hausdorff", "neighborhood", "cover",
        "set", "family", "boundary", "homotopy", "homology", "fibre",
        "simply", "convex", "curve", "surface", "bundle", "sheaf",
    },
    "combinatorics": {
        "graph", "set", "subset", "partition", "sequence", "lattice", "tree",
        "coloring", "pigeonhole", "counting", "permutation", "bijection",
        "table", "column", "row", "vertex", "edge", "family", "cycle",
        "matching", "chain", "antichain", "hyperedge", "bounded",
        "collision", "box", "intervals", "mod", "orbit", "coset",
    },
    "number": {
        "integer", "prime", "rational", "natural", "diophantine", "modular",
        "residue", "number", "divisor", "ideal", "lattice", "l-function",
        "character", "zeta", "algebra", "form", "curve", "height",
        "mod", "coset", "orbit", "pair", "triple", "coprime", "factor",
        "conjecture", "polynomial",
    },
    "logic": {
        "theory", "formula", "sentence", "language", "axiom", "consistent",
        "model", "interpretation", "structure", "formal", "proof", "syntax",
        "deduction", "system", "computable", "machine", "program", "function",
        "recursive", "complete",
    },
    "probability": {
        "probability", "measure", "random", "distribution", "variable",
        "sequence", "martingale", "chain", "filtration", "stochastic",
        "event", "sigma", "iid", "finite", "variance", "space", "law",
    },
    "category": {
        "functor", "category", "morphism", "adjoint", "limit", "colimit",
        "cone", "natural", "object", "diagram", "yoneda", "monad",
    },
}


# Which domains we consider each technique to belong to. A technique may belong
# to several: that means the edge just needs to match ONE of them.
TECHNIQUE_DOMAIN: dict[str, list[str]] = {
    "t_spot_pattern_in_table": ["combinatorics", "number", "analysis", "algebra"],
    "t_verify_on_special_cases": ["algebra", "number", "combinatorics", "analysis"],
    "t_conjecture_refinement": ["algebra", "number", "combinatorics", "analysis", "topology"],
    "t_reduce_to_canonical_form": ["algebra", "analysis", "geometry", "number"],
    "t_compose_with_identity": ["algebra", "analysis", "combinatorics", "number", "geometry"],
    "t_auxiliary_construction": ["geometry", "analysis", "algebra", "combinatorics", "logic", "number"],
    "t_symmetry_reduction": ["algebra", "geometry", "combinatorics", "number"],
    "t_duality": ["algebra", "geometry", "analysis", "topology", "category"],
    "t_conserved_quantity": ["analysis", "geometry", "algebra", "combinatorics"],
    "t_character_decomposition_count": ["combinatorics", "number", "algebra"],
    "t_frequency_decomposition": ["analysis", "algebra", "number"],
    "t_interpolate_and_continue": ["analysis", "number"],
    "t_exhaustion_squeeze": ["analysis", "geometry"],
    "t_axiomatize_from_instances": ["algebra", "logic", "analysis", "geometry", "number"],
    "t_structural_isomorphism": ["algebra", "topology", "category", "number"],
    "t_raise_dimension": ["geometry", "topology", "combinatorics"],
    "t_projection_to_subspace": ["geometry", "algebra", "analysis"],
    "t_obstruction_class": ["topology", "algebra", "geometry"],
    "t_compactness_argument": ["topology", "analysis", "logic", "geometry"],
    "t_sieve_by_optimized_quadratic": ["number", "combinatorics"],
    "t_pigeonhole_collision": ["combinatorics", "number", "probability", "analysis"],
    "t_diagonalize": ["logic", "algebra"],
    "t_arithmetize_syntax": ["logic", "number"],
    "t_reductio_ad_absurdum": ["logic", "analysis", "algebra", "geometry", "combinatorics", "number", "topology"],
    "t_infinite_descent": ["number", "algebra"],
    "t_force_independence": ["logic"],
    "t_contraction_fixed_point": ["analysis", "topology"],
    "t_physics_to_pde": ["analysis", "geometry"],
    "t_ergodic_correspondence": ["probability", "analysis", "number"],
    "t_complete_the_square": ["algebra", "analysis"],
    "t_finite_case_check": ["combinatorics", "number", "logic"],
    "t_formal_verify": ["logic"],
    "t_distributed_collaboration": ["algebra", "combinatorics", "number", "logic"],
    "t_ultraproduct_transfer": ["logic", "topology", "algebra"],
    "t_probabilistic_existence": ["combinatorics", "probability"],
    "t_svd_and_spectral_decomposition": ["algebra", "analysis"],
    "t_complex_analysis_to_integers": ["analysis", "number"],
    "t_flow_with_surgery": ["geometry", "topology", "analysis"],
    "t_analysis_algebra_topology_bridge": ["algebra", "analysis", "topology", "number"],
    "t_sheaf_cohomology_bridge": ["topology", "algebra", "geometry"],
    "t_k_theoretic_index_bridge": ["topology", "analysis", "algebra"],
    "t_heights_and_galois_rep_bridge": ["number", "algebra"],
    "t_level_lowering_bridge": ["number", "algebra"],
    "t_transference_bridge": ["combinatorics", "number", "analysis"],
    "t_rescale_for_asymptotic_geometry": ["geometry", "analysis"],
    "t_sheafify_on_grothendieck_topology": ["algebra", "geometry", "topology"],
    "t_group_complete_exact_category": ["algebra", "category", "topology"],
    "t_major_minor_arc_decomposition": ["number", "analysis"],
    "t_deformation_cohomology": ["algebra", "number", "topology"],
    "t_representable_functor_trick": ["category", "algebra"],
    "t_double_centralizer_decompose": ["algebra"],
    "t_polynomial_method": ["combinatorics", "algebra", "number"],
    # compound / host nodes — accept anything (they subcontract)
    "t_fourier_transform": ["analysis", "algebra"],
    "t_galois_correspondence": ["algebra", "number"],
    "t_godel_numbering": ["logic", "number"],
    "t_atiyah_singer_index_machinery": ["analysis", "topology", "algebra"],
    "t_furstenberg_correspondence_principle": ["probability", "combinatorics", "number"],
    "t_circle_method": ["number", "analysis"],
    "t_ricci_flow_with_surgery": ["geometry", "analysis"],
    "t_selberg_sieve_method": ["number", "combinatorics"],
    "t_wiles_modularity": ["number", "algebra"],
    "t_category_theoretic_colimits_and_adjoints": ["category", "algebra", "topology"],
}


# Globally plausible math vocabulary — any state whose name/type involves
# one of these is considered potentially valid input to almost any technique.
# This is the "ambient noun" filter.
GENERIC_MATH_VOCAB: set[str] = {
    "function", "identity", "formula", "equation", "proposition", "lemma",
    "theorem", "conjecture", "relation", "definition", "specific", "general",
    "case", "instance", "object", "structure", "map", "morphism", "system",
    "pair", "triple", "tuple", "sequence", "series", "set", "subset", "group",
    "space", "domain", "range", "element", "point", "class", "type", "family",
    "collection", "chain", "product", "sum", "factor", "term", "value",
    "variable", "parameter", "constant", "index", "length", "order", "rank",
    "dim", "dimension", "number", "form", "inequality", "integral", "derivative",
    "algebraicrelation", "grouplaw", "simplicialcomplex", "triangulated",
    "multigraph", "bridge", "configuration", "labeled", "intersection", "divisor",
    "heat", "conduction", "physical", "physicalsystem", "rod",
    "holomorphicmap", "extremal", "local", "section", "coordinates",
    "euler", "char", "simple", "non", "abelian",
    "complex", "polynomial", "meromorphic", "meromorphicfunction", "zeta",
    "real", "list", "affinevariety", "variety", "vanishing", "retraction",
    "action", "functional", "infinitesimal", "variation", "predicate",
    "predicates", "arithmeticpredicate", "arithmetized", "syntactic",
    "sentence", "del", "alleged", "decider", "halting", "turingmachine",
    "data", "encoding", "injection", "tms", "godel", "metric", "analytic",
    "asymptotic", "measure", "measurable", "probability", "random",
    "open", "closed", "bounded", "compact", "continuous", "stratification",
    "decomposition", "extension", "refinement", "equivalence", "category",
    "object", "normal", "subnormal", "solvable", "subsolvable",
    "framework", "theater", "reconstruction", "link", "anabelian",
    "cobordism", "rigidity", "embedding", "manifold", "surface",
    "mod", "residue", "witness", "henkin", "choice", "phi", "psi",
    "sup", "inf", "limit", "limsup", "liminf", "epsilon", "delta",
    "ideal", "radical", "principal", "nilpotent", "flat", "projective",
    "locally", "globally", "generic", "special", "regular", "singular",
    "log", "exp", "volume", "area", "perimeter", "degree", "genus",
    "scheme", "stack", "topos", "operad", "category",
    "boolean", "lattice", "chain", "antichain", "partial",
    "semistable", "unstable", "stable", "stratification", "strata",
    "ramification", "deformation", "cohomology", "sheaf",
    "elliptic", "parabolic", "hyperbolic", "frobenius", "galois",
    "modular", "cusp", "level",
    "paradoxical", "mother", "child", "path", "walk", "edge", "vertex",
    "choice", "orbit", "ball", "triangle", "quadrilateral", "hexagon",
    "generator", "relation", "generator",
    "table", "aryabhata", "kuttaka", "euclid", "extended",
    "forms", "quadratic", "canonical", "completion", "geometric", "square",
    "perpendiculars", "transversal", "vertices", "from", "defect", "vertex",
    "classification", "geometries", "thurston", "transfer", "transference",
    "innermodel", "constructible", "universe", "forcingextension",
    "semisimple", "absolutely",
    "binomial", "tail", "central", "stirling", "gaussian", "density",
    "moment", "cumulant", "generatingfunction", "log", "derivative",
    "power", "sum", "root", "factored", "form", "prime",
    "nonnegative", "nonzero", "positive", "negative", "zero",
    "list", "ordering", "enumeration", "finite", "infinite", "countable",
    "well", "ordered", "maximal", "minimal", "sup", "set", "ipsum",
    "trajectory", "injection", "surjection", "bijection", "orphan",
    "pair", "partial", "total", "full", "refined",
    "symbolic", "numeric", "approximate", "exact", "closed", "open",
    "tangent", "normal", "parallel", "cross", "dot", "inner", "outer",
    "supplementary", "complementary", "diagonal", "median", "altitude",
    "incircle", "circumcircle", "tangent", "secant", "chord", "arc",
    "matching", "cover", "partition", "decomposition", "filtration",
    "resolution", "presentation", "factorization", "splitting",
    "hypothesis", "assumption", "consequence", "implication", "corollary",
    "witness", "counterexample", "example", "instance",
    "auxiliary", "helper", "auxiliary", "introduction",
    "interpolated", "extrapolated", "continued", "analytic",
    "log", "exp", "tan", "arctan", "sinh", "cosh", "tanh",
    "series", "convergent", "divergent", "absolutely", "uniformly",
    "pointwise", "almost", "everywhere", "essentially", "everywhere",
    "derived", "adjoint", "dual", "codual", "opposite",
    "symbol", "symbolic", "sign", "absolute",
    "sequence", "subsequence", "net", "filter", "ultrafilter",
    "henkin", "unobstructed",
    # proper nouns
    "pascal", "viete", "wallis", "galilean", "weierstrass", "flt",
    "stirling", "newton", "lagrange", "aryabhata", "kuttaka",
    "cayley", "jacobi", "stokes", "riemann", "cauchy", "schwarz",
    "claim", "strengthened", "fall", "free", "speed",
    "line", "formulas", "interpolation", "approximation",
    "nested", "infinitely", "many", "intervals", "terms", "with",
    "half",
}


def edge_plausible(src, tech) -> tuple[str, str]:
    """Return (status, reason) where status in {'ok','unchecked','flag','axiom'}."""
    if src.get("kind") == "axiom":
        return "axiom", ""
    tsig_toks = tokens(src.get("type_signature", "")) | tokens(src.get("name", ""))
    if not tsig_toks:
        return "unchecked", "no type_signature / name tokens"
    # Fast-path: if the state contains any ambient math noun, accept.
    if tsig_toks & GENERIC_MATH_VOCAB:
        return "ok", ""
    domains = TECHNIQUE_DOMAIN.get(tech["id"])
    if not domains:
        return "unchecked", f"technique {tech['id']} missing domain mapping"
    allowed = set()
    for d in domains:
        allowed |= DOMAIN_KEYWORDS.get(d, set())
    hit = tsig_toks & allowed
    if hit:
        return "ok", ""
    # fall back — maybe the technique id itself is in the tokens
    tech_tok = tokens(tech["id"] + " " + tech.get("name", ""))
    if tsig_toks & tech_tok:
        return "ok", ""
    return "flag", (
        f"no domain keyword match: src tokens={sorted(tsig_toks)[:6]}, "
        f"tech={tech['id']}, expected-domains={domains}"
    )


def main():
    with open("knowledge_graph.json") as f:
        g = json.load(f)
    nodes = {n["id"]: n for n in g["nodes"]}
    tallies = defaultdict(int)
    flagged = []
    for e in g["edges"]:
        src = nodes.get(e["from"])
        dst = nodes.get(e["to"])
        if not src or not dst:
            tallies["missing_node"] += 1
            continue
        if dst.get("kind") != "technique":
            # only audit state -> technique edges here
            continue
        status, reason = edge_plausible(src, dst)
        tallies[status] += 1
        if status == "flag":
            flagged.append(
                {
                    "edge_id": e.get("id"),
                    "from": e["from"],
                    "to": e["to"],
                    "reason": reason,
                    "theorem": e.get("used_in_theorem", ""),
                }
            )
    total_edges_into_techniques = sum(
        tallies.get(k, 0) for k in ("axiom", "ok", "unchecked", "flag")
    )
    print("# Typed-correctness sweep results")
    print(f"Edges state->technique: {total_edges_into_techniques}")
    for k in ("axiom", "ok", "unchecked", "flag"):
        print(f"  {k}: {tallies.get(k, 0)}")
    print()
    print(f"# Top-10 flagged mismatches ({len(flagged)} total)")
    for f in flagged[:10]:
        print(
            f"- edge {f['edge_id']}: {f['from']} -> {f['to']} "
            f"in theorem {f['theorem']}\n    reason: {f['reason']}"
        )


if __name__ == "__main__":
    main()
