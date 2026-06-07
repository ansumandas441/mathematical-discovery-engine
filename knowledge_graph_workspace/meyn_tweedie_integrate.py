import json, sys

GRAPH = "/Users/primetrce/Documents/maths/knowledge_graph.json"

new_nodes = [
{"id":"s_substochastic_kernel","kind":"axiom","name":"Sub-stochastic kernel","type_signature":"K: X x B(X) -> [0,1], K(x,X) <= 1","description":"A kernel K(x,A) that is a sub-probability measure in A for each x (total mass at most 1), arising as taboo or restricted transition kernels where mass can be lost to a forbidden set or to escape."},
{"id":"s_linear_state_space_model","kind":"axiom","name":"Linear (Gaussian) state-space LSS model","type_signature":"X_{n+1} = F X_n + G W_{n+1}, Y_n = H X_n + V_n","description":"The Markov chain driven by the linear recursion X_{n+1}=F X_n+G W_{n+1} with i.i.d. Gaussian noise, whose irreducibility, T-chain property, and geometric ergodicity follow from controllability of (F,G) and the spectral radius of F being below 1."},
{"id":"s_random_walk_half_line","kind":"axiom","name":"Random walk on a half-line","type_signature":"X_{n+1} = max(X_n + W_{n+1}, 0) on R_+","description":"The reflected random walk X_{n+1}=(X_n+W_{n+1})^+ on the half-line, a canonical Meyn-Tweedie queueing/storage Markov model whose recurrence is governed by the sign of the increment mean E[W]."},
{"id":"s_random_walk_increment_mean_criterion","kind":"state","name":"Increment-mean criterion for random-walk stability","type_signature":"E[W] < 0 => positive recurrent; E[W] > 0 => transient","description":"The classification that a random walk on a half-line is positive Harris recurrent when the increment has negative mean, null recurrent when the mean is zero, and transient when the mean is positive."},
{"id":"s_forward_recurrence_time_chain","kind":"state","name":"Forward/backward recurrence-time chains","type_signature":"V_n^+ (forward), V_n^- (backward) on Z_+ or R_+","description":"The Markov chains formed by the residual (forward) and elapsed (backward) time to the next or last renewal of a renewal process, canonical examples used to test irreducibility, small sets, and ergodicity criteria."},
{"id":"s_existence_small_sets","kind":"theorem","name":"Existence of small sets","type_signature":"phi-irreducible => exists small set C with phi(C) > 0","description":"Every phi-irreducible Markov chain admits a small set of positive irreducibility measure, obtained by partitioning the state space and applying a minorization to one cell, so that the splitting construction always applies."},
{"id":"s_reachable_point_mc","kind":"axiom","name":"Reachable point","type_signature":"x* s.t. for all open O containing x* and all y: sum_n P^n(y,O) > 0","description":"A point every neighbourhood of which is reached with positive probability from every initial state; existence of a reachable point links topological structure to phi-irreducibility for Feller and T-chains."},
{"id":"s_topological_irreducibility_t_chain","kind":"theorem","name":"Topological irreducibility for T-chains","type_signature":"T-chain + reachable point => psi-irreducible","description":"For a T-chain, open-set (topological) irreducibility together with the existence of a reachable point implies phi-irreducibility, so the topological and measure-theoretic notions of irreducibility coincide."},
{"id":"s_recurrence_transience_dichotomy_mc","kind":"theorem","name":"Recurrence/transience dichotomy","type_signature":"psi-irreducible => (recurrent) XOR (transient)","description":"Every psi-irreducible Markov chain is either recurrent, with potential U(x,A)=infinity for all x and all psi-positive A, or transient, with the state space a countable union of uniformly transient sets, with no intermediate case."},
{"id":"s_maximal_harris_set","kind":"theorem","name":"Maximal Harris set / Harris decomposition","type_signature":"X = H union N, H maximal absorbing Harris, psi(N)=0","description":"A recurrent psi-irreducible chain decomposes its space into a maximal absorbing Harris-recurrent set H, on which the chain returns to every psi-positive set with probability one, and a psi-null remainder."},
{"id":"s_drift_operator_mc","kind":"axiom","name":"Drift operator Delta V = P V - V","type_signature":"Delta V(x) = int P(x,dy) V(y) - V(x)","description":"The discrete generator Delta=P-I applied to a function V, giving the one-step expected change of V and serving as the central object of all Foster-Lyapunov drift conditions."},
{"id":"s_f_regularity_mc","kind":"state","name":"f-regular set / f-regularity","type_signature":"sup_{x in C} E_x[ sum_{k=0}^{tau_B-1} f(X_k) ] < infinity","description":"A set C is f-regular if the expected f-weighted occupation time before hitting any psi-positive set is uniformly bounded over C; f-regularity of the chain quantifies the rate in f-norm ergodic theorems."},
{"id":"s_drift_criterion_f_regularity","kind":"theorem","name":"Drift criterion V3 for f-regularity","type_signature":"P V <= V - f + b*1_C => f-regular","description":"If a function V>=0 satisfies the drift inequality P V(x) <= V(x) - f(x) + b*1_C(x) for a petite set C, then sublevel sets of V are f-regular and the chain is f-ergodic, the V3 condition of Meyn-Tweedie."},
{"id":"s_poisson_equation_mc","kind":"state","name":"Poisson equation for Markov chains","type_signature":"(I - P) g_hat = f - pi(f)","description":"The equation (I-P) g_hat = f - pi(f) whose solution g_hat, the centered potential of f, removes the drift of f, underlying martingale decompositions, the CLT, and asymptotic-variance formulas."},
{"id":"s_fundamental_kernel_z_mc","kind":"state","name":"Fundamental kernel Z = (I - P + Pi)^{-1}","type_signature":"Z = (I - P + Pi)^{-1}, Pi f = pi(f)*1","description":"The fundamental kernel of an ergodic chain, the bounded inverse of I-P+Pi on functions of zero pi-mean, providing the canonical solution g_hat=Z f to the Poisson equation and the asymptotic variance formula."},
{"id":"s_dynkin_formula_discrete_mc","kind":"theorem","name":"Dynkin's formula (discrete, Markov chain)","type_signature":"E_x[V(X_n)] = V(x) + E_x[ sum_{k=0}^{n-1} Delta V(X_k) ]","description":"For a Markov chain with drift operator Delta=P-I, the telescoping identity E_x[V(X_{tau wedge n})] = V(x) + E_x[ sum_{k=0}^{tau wedge n-1} Delta V(X_k) ], the discrete-time analogue of Dynkin's formula linking drift to expected values at stopping times."},
{"id":"s_clt_geometric_ergodicity","kind":"theorem","name":"CLT under geometric ergodicity","type_signature":"V-geometrically ergodic + pi(f^2 V) < infinity => sqrt(n)(S_n/n - pi(f)) => N(0,sigma_f^2)","description":"A V-geometrically ergodic chain satisfies the central limit theorem for every f with f^2 <= V and has finite asymptotic variance sigma_f^2, the sharp moment-condition strengthening of the Harris-chain CLT."},
{"id":"s_functional_clt_markov","kind":"theorem","name":"Functional CLT / invariance principle for Markov chains","type_signature":"(1/sqrt(n)) sum_{k<=floor(nt)} (f(X_k)-pi(f)) => sigma_f B(t) in D[0,1]","description":"Under geometric ergodicity or f-regularity with finite variance, the partial-sum process of a centered functional of a Markov chain converges weakly to a Brownian motion with variance sigma_f^2, a Donsker-type invariance principle proved via martingale approximation."},
{"id":"s_quasi_compactness_weighted_mc","kind":"theorem","name":"Quasi-compactness / spectral gap of P on L_inf^V","type_signature":"P on L_inf^V: spectral radius 1, essential spectral radius < 1","description":"V-geometric ergodicity is equivalent to the transition operator P being quasi-compact on the weighted space L_inf^V with a spectral gap, an isolated simple eigenvalue 1 and essential spectral radius strictly below 1, giving the geometric convergence rate."},
{"id":"t_martingale_approximation_mc","kind":"technique","name":"Martingale approximation / Poisson-equation method","function_signature":"(f - pi(f)) = g_hat - P g_hat => S_n = M_n + (g_hat(X_0) - g_hat(X_n))","description":"The technique of solving the Poisson equation (I-P) g_hat = f - pi(f) to write the centered partial sums as a martingale plus a negligible telescoping remainder, the engine behind the CLT, FCLT, and LIL for Markov chains."},
{"id":"s_sub_super_harmonic_mc","kind":"state","name":"Sub/super-harmonic functions for a Markov chain","type_signature":"P h <= h (superharmonic) / P h >= h (subharmonic)","description":"Functions satisfying P h <= h (superharmonic/excessive, the Lyapunov objects of recurrence drift conditions) or P h >= h (subharmonic), whose boundedness and minimal-solution structure characterize recurrence, transience, and hitting probabilities."},
]

edges_raw = [
("s_poisson_equation_mc","t_martingale_approximation_mc","input","s_clt_geometric_ergodicity"),
("s_fundamental_kernel_z_mc","t_martingale_approximation_mc","input","s_clt_geometric_ergodicity"),
("t_martingale_approximation_mc","s_clt_geometric_ergodicity","output","s_clt_geometric_ergodicity"),
("t_martingale_approximation_mc","s_functional_clt_markov","output","s_functional_clt_markov"),
("t_martingale_approximation_mc","s_clt_harris_chain","output","s_clt_harris_chain"),
("t_martingale_approximation_mc","s_asymptotic_variance_mc","output","s_clt_geometric_ergodicity"),
("s_drift_operator_mc","t_lyapunov_foster_criterion","input","s_drift_criterion_f_regularity"),
("s_sub_super_harmonic_mc","t_lyapunov_foster_criterion","input","s_recurrence_transience_dichotomy_mc"),
("t_lyapunov_foster_criterion","s_drift_criterion_f_regularity","output","s_drift_criterion_f_regularity"),
("t_lyapunov_foster_criterion","s_f_regularity_mc","output","s_drift_criterion_f_regularity"),
("t_lyapunov_foster_criterion","s_recurrence_transience_dichotomy_mc","output","s_recurrence_transience_dichotomy_mc"),
("t_lyapunov_foster_criterion","s_random_walk_increment_mean_criterion","output","s_recurrence_transience_dichotomy_mc"),
("t_lyapunov_foster_criterion","s_dynkin_formula_discrete_mc","output","s_dynkin_formula_discrete_mc"),
("s_dynkin_formula_discrete_mc","t_lyapunov_foster_criterion","input","s_comparison_theorem_drift"),
("t_lyapunov_foster_criterion","s_comparison_theorem_drift","output","s_comparison_theorem_drift"),
("s_small_set","t_nummelin_splitting","input","s_existence_small_sets"),
("s_minorization_condition","t_nummelin_splitting","input","s_existence_small_sets"),
("t_nummelin_splitting","s_existence_small_sets","output","s_existence_small_sets"),
("t_nummelin_splitting","s_maximal_harris_set","output","s_maximal_harris_set"),
("s_atom_general_state_space","t_regeneration_technique","input","s_fundamental_kernel_z_mc"),
("t_regeneration_technique","s_fundamental_kernel_z_mc","output","s_fundamental_kernel_z_mc"),
("t_regeneration_technique","s_maximal_harris_set","output","s_maximal_harris_set"),
("s_poisson_equation_mc","t_regeneration_technique","input","s_fundamental_kernel_z_mc"),
("s_drift_operator_mc","t_generator_characterization","input","s_quasi_compactness_weighted_mc"),
("t_generator_characterization","s_quasi_compactness_weighted_mc","output","s_quasi_compactness_weighted_mc"),
("s_reachable_point_mc","t_generator_characterization","input","s_topological_irreducibility_t_chain"),
("s_t_chain","t_generator_characterization","input","s_topological_irreducibility_t_chain"),
("t_generator_characterization","s_topological_irreducibility_t_chain","output","s_topological_irreducibility_t_chain"),
("s_substochastic_kernel","t_generator_characterization","input","s_transience_mc"),
("t_generator_characterization","s_transience_mc","output","s_transience_mc"),
("s_linear_state_space_model","t_lyapunov_foster_criterion","input","s_v_uniform_ergodicity"),
("t_lyapunov_foster_criterion","s_v_uniform_ergodicity","output","s_v_uniform_ergodicity"),
("s_random_walk_half_line","t_lyapunov_foster_criterion","input","s_drift_criterion_positive_recurrence"),
("t_lyapunov_foster_criterion","s_drift_criterion_positive_recurrence","output","s_drift_criterion_positive_recurrence"),
("s_forward_recurrence_time_chain","t_regeneration_technique","input","s_positive_harris_recurrence"),
("t_regeneration_technique","s_positive_harris_recurrence","output","s_positive_harris_recurrence"),
("s_random_walk_increment_mean_criterion","t_lyapunov_foster_criterion","input","s_recurrence_mc"),
("t_lyapunov_foster_criterion","s_recurrence_mc","output","s_recurrence_mc"),
("s_f_regularity_mc","t_martingale_approximation_mc","input","s_clt_geometric_ergodicity"),
("s_quasi_compactness_weighted_mc","t_martingale_approximation_mc","input","s_clt_geometric_ergodicity"),
("s_sub_super_harmonic_mc","t_generator_characterization","input","s_recurrence_transience_dichotomy_mc"),
("t_generator_characterization","s_drift_operator_mc","output",""),
]

d = json.load(open(GRAPH))
existing_ids = {n["id"] for n in d["nodes"]}

# 1. node id uniqueness
for n in new_nodes:
    if n["id"] in existing_ids:
        sys.exit("DUP NODE ID: " + n["id"])
if len({n["id"] for n in new_nodes}) != len(new_nodes):
    sys.exit("dup within new nodes")

all_ids = existing_ids | {n["id"] for n in new_nodes}

# 2. validate bipartite + endpoints exist
kind_of = {n["id"]: n["kind"] for n in d["nodes"]}
kind_of.update({n["id"]: n["kind"] for n in new_nodes})
for f,t,role,thm in edges_raw:
    if f not in all_ids: sys.exit("missing from: "+f)
    if t not in all_ids: sys.exit("missing to: "+t)
    if thm and thm not in all_ids: sys.exit("missing used_in_theorem: "+thm)
    kf, kt = kind_of[f], kind_of[t]
    if role == "input":
        assert kf in ("state","theorem","axiom") and kt=="technique", ("bad input edge",f,t,kf,kt)
    else:
        assert kf=="technique" and kt in ("state","theorem","axiom"), ("bad output edge",f,t,kf,kt)

# 3. max edge id
maxid = 0
for e in d["edges"]:
    try: maxid = max(maxid, int(str(e["id"]).split("_")[1]))
    except: pass
nextid = maxid + 1

new_edges = []
for f,t,role,thm in edges_raw:
    new_edges.append({"id":"e_%d"%nextid,"from":f,"to":t,"role":role,"parameter_binding":{},"used_in_theorem":thm})
    nextid += 1

d["nodes"].extend(new_nodes)
d["edges"].extend(new_edges)

# final id-uniqueness check
nid = [n["id"] for n in d["nodes"]]
assert len(nid)==len(set(nid)), "dup node ids after merge"
eid = [e["id"] for e in d["edges"]]
assert len(eid)==len(set(eid)), "dup edge ids after merge"

json.dump(d, open(GRAPH,"w"), ensure_ascii=False, indent=2)
print("OK nodes=%d edges=%d (added %d nodes, %d edges, edge ids %d..%d)" % (
    len(d["nodes"]), len(d["edges"]), len(new_nodes), len(new_edges), maxid+1, nextid-1))
