# Jech Set Theory — merged candidate list (from 3 Extractors, deduped across extractors)

Format: Name | kind | description | deps

## ZFC axioms & basic constructions
- Axiom of Extensionality | axiom | Two sets are equal iff they have the same elements | logic
- Axiom of Pairing | axiom | For any a,b there is a set {a,b} | Extensionality
- Axiom of Union | axiom | For any X there is ⋃X containing members of members of X | Extensionality
- Axiom of Power Set | axiom | For any X there is P(X) of all subsets | Extensionality
- Axiom of Infinity | axiom | There exists an inductive set (∅∈S, closed under x↦x∪{x}) | Pairing,Union
- Axiom Schema of Separation | axiom | For each formula φ and set X, {u∈X:φ(u)} exists | formula schema
- Axiom Schema of Replacement | axiom | The image of a set under a definable class function is a set | formula schema
- Axiom of Foundation/Regularity | axiom | Every nonempty set has an ∈-minimal element | ∈-relation
- Class / proper class | axiom | A collection {x:φ(x)}; proper class is not a set | formula
- Ordered pair (Kuratowski) | state | (a,b):={{a},{a,b}} | Pairing
- Transitive set | axiom | A set T with ⋃T⊆T (every element is a subset) | ∈
- Transitive closure TC(x) | state | The smallest transitive set containing x | Union,Replacement

## Ordinals
- Ordinal number (von Neumann) | axiom | A transitive set well-ordered by ∈ | transitive,well-order,Foundation
- Well-ordering | axiom | A linear order where every nonempty subset has a least element | order
- Transfinite induction | technique | Prove ∀α φ(α) via φ at all β<α ⟹ φ(α) | ordinal
- Order type | state | The unique ordinal isomorphic to a given well-ordered set | well-order,Mostowski collapse
- Comparability of ordinals | theorem | Ordinals are linearly ordered by ∈ (trichotomy) | ordinal,Foundation
- Burali-Forti paradox | theorem | The class Ord of all ordinals is a proper class | ordinal
- Ordinal arithmetic (+, ·, exp) | state | Operations on ordinals by transfinite recursion; non-commutative | transfinite recursion
- Cantor normal form | theorem | Unique base-ω representation α=ω^{β1}k1+...+ω^{βn}kn | ordinal arithmetic
- Epsilon numbers (ε-numbers) | state | Ordinals ε with ω^ε=ε; ε0 the least | ordinal exp

## Cumulative hierarchy / well-founded
- Rank function | state | rank(x)=least α with x∈V_{α+1} | Vα,Foundation
- ∈-induction (Foundation induction) | technique | Prove ∀x φ(x) via (∀y∈x)φ(y)→φ(x) | Foundation
- Well-founded relation | axiom | A relation with no infinite descending chain | Foundation analog
- Well-founded recursion | technique | Defining a function by recursion along a well-founded relation | well-founded relation
- H(κ) hereditarily <κ | state | Sets whose transitive closure has cardinality <κ | TC,cardinal
- Inner model | axiom | A transitive proper class containing all ordinals, modeling ZF | transitive class,ZF
- V_κ ⊨ ZFC for inaccessible κ | state | Rank-initial segments modeling Zermelo/ZFC | Vα,inaccessible

## Cardinals & arithmetic
- Equinumerosity (equipotence) | axiom | X≈Y iff a bijection exists | bijection
- Cantor's theorem | theorem | |X|<|P(X)| for every set | Power Set,diagonalization
- Cantor–Bernstein (Schröder–Bernstein) theorem | theorem | |X|≤|Y| and |Y|≤|X| ⟹ |X|=|Y| | injections
- Aleph function ℵ_α | state | Enumeration of infinite cardinals via initial ordinals | ordinal,Hartogs
- Hartogs' theorem / Hartogs number | theorem | Least ordinal not injectable into X exists (without AC) | ordinal,Replacement
- Initial ordinal | state | An ordinal not equinumerous with any smaller ordinal | ordinal
- Cardinal arithmetic (κ+λ,κ·λ,κ^λ) | state | Sum/product/exponentiation via disjoint union/product/function space | cardinality,AC
- Absorption law κ+λ=κ·λ=max(κ,λ) | theorem | For infinite cardinals | AC
- κ·κ=κ (Hessenberg) | theorem | Every infinite cardinal κ satisfies κ²=κ | Gödel pairing
- Gödel pairing function | state | Canonical well-ordering of Ord×Ord, bijection on κ×κ | ordinal
- Cofinality cf(α) | state | Least order type of an unbounded subset of α | ordinal
- Regular cardinal | axiom | cf(κ)=κ | cofinality
- Singular cardinal | axiom | cf(κ)<κ | cofinality
- Successor cardinals are regular | theorem | ℵ_{α+1} regular under AC | AC,cofinality
- König's theorem (κ<κ^{cf(κ)}) | theorem | Σκᵢ<Πλᵢ when κᵢ<λᵢ; gives cf(2^κ)>κ | cardinal arithmetic
- Continuum function κ↦2^κ | state | The cardinal exponential; 2^ℵ0=c | Power Set
- Generalized Continuum Hypothesis GCH | state | 2^{ℵ_α}=ℵ_{α+1} for all α | continuum function
- Hausdorff formula | theorem | ℵ_{α+1}^{ℵ_β}=ℵ_α^{ℵ_β}·ℵ_{α+1} | cardinal exp
- Gimel function ℶ(κ)=κ^{cf κ} | state | Cardinal exponentiation reduces to gimel and 2^λ | cofinality
- Beth function ⊐_α | state | ⊐0=ℵ0, ⊐_{α+1}=2^{⊐α}; iterated power-set cardinals | continuum function

## AC equivalents
- Well-ordering theorem (Zermelo) | theorem | Every set can be well-ordered; equivalent to AC | AC
- Hausdorff maximal principle | theorem | Every poset has a maximal chain; equiv AC | poset,AC
- Tukey's lemma | theorem | Every family of finite character has a maximal element; equiv AC | AC
- Trichotomy of cardinals | theorem | For any X,Y: |X|≤|Y| or |Y|≤|X|; equiv AC | AC

## Filters, ultrafilters, Boolean algebras
- Filter | axiom | Collection closed under supersets and finite intersections, not containing ∅ | subset
- Ideal | axiom | Dual of a filter | filter
- Principal vs non-principal ultrafilter | state | Generated by a point vs containing cofinite filter | ultrafilter
- Ultrafilter existence / Boolean Prime Ideal Theorem | theorem | Every filter extends to an ultrafilter | filter,Zorn
- κ-complete filter | axiom | Closed under intersections of <κ members | filter,cardinal
- Ultraproduct / ultrapower | state | Reduced product ∏Mᵢ/U of structures modulo U | ultrafilter
- Łoś's theorem | theorem | A formula holds in the ultraproduct iff its index set is in U | ultraproduct
- Boolean algebra | axiom | A complemented distributive lattice | lattice
- Complete Boolean algebra | axiom | Every subset has a supremum | Boolean algebra
- Stone representation theorem | theorem | Every BA ≅ a field of clopen sets of its Stone space | BA,ultrafilters
- Regular open algebra RO(P) | state | Complete BA of regular open sets; canonical completion | BA,topology
- Antichain / c.c.c. / saturation in BA | state | Pairwise-disjoint nonzero elements; κ-saturation | BA

## Club / stationary
- Closed unbounded (club) set | state | Closed and unbounded subset of regular κ | regular cardinal
- Club filter | state | Filter generated by club sets; κ-complete and normal | club,filter
- Stationary set | state | Meets every club set | club
- Normal filter / diagonal intersection | state | Club filter closed under diagonal intersection △C_α | club filter
- Closed unbounded sets form a filter | theorem | Intersection of <κ clubs is club | club,regular
- Δ-system (sunflower) lemma | theorem | Uncountable family of finite sets has uncountable Δ-system | cardinal arithmetic

## Trees
- Tree (set-theoretic) | axiom | Partial order where predecessors of each node are well-ordered | poset,well-order
- Branch/level/height of a tree | state | Maximal chain; nodes at level α; height=sup of levels | tree,ordinal
- Aronszajn tree | state | κ-tree of height κ, levels <κ, no branch of length κ | tree,cardinal
- König's lemma (tree form) | theorem | Every infinite finitely-branching tree has an infinite branch | tree,ω
- Aronszajn tree existence | theorem | An ℵ1-Aronszajn tree exists in ZFC | κ-tree
- Suslin tree | state | ℵ1-tree, no uncountable branch or antichain (ccc Aronszajn) | Aronszajn,antichain
- Suslin's problem / Suslin line / SH | state | Whether every ccc dense complete LO without endpoints ≅ ℝ | LO,ccc
- Equivalence of Suslin tree and Suslin line | theorem | A Suslin line exists iff a Suslin tree exists | Suslin tree
- Kurepa tree / Kurepa's hypothesis | state | ℵ1-tree, countable levels, ≥ℵ2 branches | tree,branches
- Special Aronszajn tree | state | Aronszajn tree = union of countably many antichains | Aronszajn,antichain
- Tree property | state | κ inaccessible with no κ-Aronszajn tree | tree,cardinal

## Combinatorial principles
- Partition calculus / arrow notation κ→(λ)^n_m | state | Every m-coloring of n-tuples from κ has homogeneous set of type λ | cardinal,coloring
- Ramsey's theorem (infinite) ℵ0→(ℵ0)^n_k | theorem | Finite coloring of n-subsets of infinite set has infinite homogeneous set | partition,ω
- Square principle □_κ (Jensen) | axiom | Coherent sequence ⟨C_α⟩ of clubs with otp<κ, coherence | club,V=L
- Club principle ♣ | state | Sequence of cofinal A_α guessing every uncountable X (weakening of ◊) | stationary,club
- Diamond ◊_κ (generalized) | state | Diamond at a regular uncountable κ on a stationary set | diamond,stationary
- ◊ implies CH | theorem | The diamond principle implies CH | diamond,CH
- Silver's theorem on singular cardinals | theorem | If GCH below singular κ of uncountable cofinality (stationarily), then 2^κ=κ^+ | singular,stationary,GCH
- Singular Cardinal Hypothesis (SCH) | state | If 2^{cf κ}<κ then κ^{cf κ}=κ^+ for singular κ | cardinal exp,cofinality

## Reflection / absoluteness
- Reflection principle (Lévy–Montague) | theorem | For finite lists of formulas, arbitrarily large Vα reflect their truth | Vα,Replacement
- Lévy hierarchy (Σ_n/Π_n) | state | Classification of formulas by quantifier alternation | logic
- Absoluteness | technique | Truth preserved between transitive models; Δ0/Σ1 up/down absolute | Lévy hierarchy
- Löwenheim–Skolem / elementary submodel method | technique | Countable M≺H(θ), collapse it; core combinatorial tool | elementarity,Mostowski collapse
- Skolem functions / Skolem hull | technique | Definable witnessing functions forming elementary substructures | logic,AC

## Constructibility
- Gödel operations (𝒢1–𝒢10) | technique | Ten finitary set operations generating Σ0-definable relations | ZF
- Definable power set Def(M) | technique | Subsets of M definable over (M,∈) with parameters | formula
- Axiom of constructibility V=L | axiom | Every set is constructible | L
- L is an inner model of ZF | theorem | (L,∈) satisfies all ZF axioms | L,absoluteness
- Absoluteness of L/Lα | theorem | α↦Lα is Σ1-definable and absolute for transitive ZF models | L,Lévy hierarchy
- Condensation lemma | theorem | Elementary submodel of (Lα,∈) collapses to some (Lβ,∈) | L,Mostowski collapse
- Constructible well-ordering <_L | state | Definable Σ1 well-ordering of L | L
- AC holds in L | theorem | L⊨AC via global well-ordering <_L | <_L
- Relative constructibility L[A] | state | Hierarchy built with predicate A; smallest inner model with A∩M | Def relativized
- L(A) constructible closure of A | state | Smallest inner model of ZF containing A as element | Lα with A
- ◊ holds in L (Jensen) | theorem | V=L implies ◊ | V=L,condensation
- □_κ holds in L | theorem | V=L implies □_κ for all κ | V=L,fine structure
- Suslin tree exists in L | theorem | V=L (via ◊) gives a Suslin tree | ◊ in L
- Kurepa tree in L | theorem | V=L (◊⁺) yields a Kurepa tree | ◊⁺,V=L

## Fine structure & 0#
- Rudimentary functions | technique | Functions closed under bounded quantification; define J-hierarchy | Gödel operations
- Jensen J-hierarchy Jα | state | Refined constructible hierarchy via rudimentary closure | rudimentary
- Σ_n-projectum ρ_n | state | Least ρ with a Σn-definable subset of ρ not in the structure | J-hierarchy
- Fine-structural condensation | theorem | Σn-elementary submodels of J-levels collapse to J-levels | J-hierarchy
- Zero sharp 0# | state | A Π¹2 real coding indiscernibles for L / a nontrivial j:L→L | indiscernibles
- Silver indiscernibles | state | Club class of order-indiscernibles generating L; exist iff 0# exists | indiscernibles,L
- 0# exists ⟹ V≠L | theorem | If 0# exists every uncountable cardinal is inaccessible in L | 0#
- Jensen's covering lemma | theorem | If 0# doesn't exist, every uncountable set of ordinals is covered by a constructible set of same cardinality | fine structure,0#
- Covering ⟹ SCH | theorem | Failure of 0# implies SCH | covering lemma

## Forcing
- Notion of forcing (poset P,≤,1) | state | A separative partial order of conditions | poset
- Dense set / predense | state | D⊆P meeting every condition's extensions | forcing poset
- Compatible/incompatible conditions; antichain | state | Common extension exists; pairwise incompatible | forcing poset
- Rasiowa–Sikorski lemma | theorem | For countably many dense sets there is a filter meeting them all | dense sets
- P-names | technique | Hereditarily P-labeled sets interpreted via G | forcing poset,recursion
- Canonical names (x̌, Ġ) | technique | Check-name for ground-model x; name Ġ for the generic filter | P-names
- Generic extension M[G] models ZFC | theorem | Every generic extension of a model of ZFC models ZFC | M[G]
- Forcing relation p⊩φ | state | p forces φ iff φ holds in M[G] for every generic G∋p | forcing poset,names
- Definability lemma | theorem | The relation p⊩φ is definable in the ground model | forcing relation
- Truth lemma | theorem | M[G]⊨φ iff some p∈G forces φ | forcing relation
- Forcing theorem (fundamental) | theorem | Definability + Truth lemmas reduce truth in M[G] to a ground-definable relation | def lemma,truth lemma
- Ground model definability | theorem | M is definable with a parameter inside any generic extension | forcing theorem
- Separativity / separative quotient | technique | Replace poset by its separative quotient / dense BA embedding | poset,BA
- Cohen real / Cohen forcing | technique | Forcing with Fn(ω,2) adds a new real | forcing poset
- Adding κ Cohen reals Fn(κ×ω,2) | technique | Product Cohen forcing adjoining κ mutually generic reals | Cohen,product
- Countable chain condition (ccc) | state | Every antichain is countable | antichains
- ccc forcing preserves cardinals & cofinalities | theorem | ccc posets preserve cardinals/cofinalities | ccc,nice names
- Fn(I,2) is ccc | theorem | Cohen forcing is ccc (via Δ-system lemma) | Δ-system,ccc
- Nice names | technique | Count subsets of ground model in M[G] via antichain-indexed names | ccc,antichains
- Con(ZFC)⟹Con(ZFC+¬CH) (Cohen) | theorem | Forcing Fn(ω2×ω,2) makes 2^ℵ0=ℵ2 | Cohen,ccc
- Boolean-valued universe V^B | state | Hierarchy of B-valued names with truth values ‖φ‖∈B | complete BA,names
- Boolean truth value ‖φ‖ | technique | Recursively assigned element of B = degree of truth of φ | V^B
- Mixing lemma | theorem | Given antichain {b_i} and names {ẋ_i}, exists name ẋ with b_i≤‖ẋ=ẋ_i‖ | V^B,antichains
- Maximum principle | theorem | If ‖∃xφ(x)‖=b there is a name ẋ with ‖φ(ẋ)‖=b | mixing,V^B
- Levy collapse Coll(ω,κ) / Coll(ω,<κ) | technique | Forcing collapsing κ (or all <λ) to ω | forcing poset
- κ-closed / <κ-closed forcing | state | Descending <κ-sequences have lower bounds; adds no new <κ-sequences | forcing poset
- <κ-closed forcing adds no new <κ-sequences | theorem | Preserves H_κ and small cardinals | κ-closed forcing
- κ-cc / κ-Knaster | state | Antichains of size <κ; Knaster linkedness | antichains
- κ-cc forcing preserves cardinals ≥κ | theorem | Chain condition controls surviving cardinals | κ-cc
- Product forcing & product lemma | theorem | G×H generic for P×Q iff G generic, H generic over M[G]; M[G×H]=M[G][H] | forcing,generic
- Two-step iteration P∗Q̇ | technique | Forcing with P then a P-name Q̇ for a poset | iteration,names
- Easton forcing / Easton's theorem | technique | Class product realizing any reasonable κ↦2^κ on regulars | product,König

## Martin's axiom & iterated forcing
- Martin's Axiom MA_κ | axiom | For every ccc poset and ≤κ dense sets there is a filter meeting all | ccc,dense
- Martin's Axiom MA | axiom | MA_κ for all κ<2^ℵ0 | MA_κ
- MA_{ℵ0} is a theorem (ZFC) | theorem | Martin's axiom for countably many dense sets = Rasiowa–Sikorski | Rasiowa–Sikorski
- Con(MA+¬CH) (Solovay–Tennenbaum) | theorem | FS ccc iteration of length ω2 forces MA+2^ℵ0=ℵ2 | iterated forcing
- Finite-support iteration ⟨P_α,Q̇_α⟩ | technique | Iterated forcing with finite support | two-step iteration
- FS iteration of ccc is ccc | theorem | Finite-support iterations of ccc forcings remain ccc | FS iteration,Δ-system
- MA_{ℵ1}⟹2^ℵ0>ℵ1 | theorem | Martin's axiom for ℵ1 dense sets refutes CH | MA_κ
- MA⟹SH (no Suslin tree) | theorem | MA_{ℵ1} implies every Aronszajn tree is special, no Suslin tree | MA,Suslin
- Con(SH) (Solovay–Tennenbaum) | theorem | Suslin's Hypothesis is consistent with ZFC | Con(MA+¬CH)
- MA consequences (additivity of measure/category) | theorem | MA_κ: union of ≤κ null/meager sets is null/meager | MA_κ
- Random real forcing (measure algebra) | technique | Forcing with Borel/null measure algebra adds a random real; ccc | complete BA,measure

## Large cardinals & embeddings
- Mahlo cardinal | state | Regular κ with {λ<κ: λ inaccessible} stationary | stationary,inaccessible
- Weakly compact cardinal | state | Inaccessible κ with tree property / κ→(κ)²2 / Π¹1-indescribable | inaccessible,partition,trees
- Tree property characterization of weak compactness | theorem | For inaccessible κ: weakly compact iff tree property iff κ→(κ)²2 | weakly compact
- Inaccessibility ⟹ V_κ⊨ZFC | theorem | If κ inaccessible then (V_κ,∈)⊨ZFC | inaccessible,Vκ
- Normal measure / ultrafilter | state | κ-complete ultrafilter on κ closed under diagonal intersections | measurable,club
- Ultrapower Ult(V,U) | technique | V^κ/U; well-founded by κ-completeness, collapse to transitive M | ultrafilter,Łoś,collapse
- Elementary embedding j:V→M with critical point κ | theorem | Measurable κ yields nontrivial j:V→M, crit(j)=κ; characterizes measurability | ultrapower
- Scott's theorem (measurable ⟹ V≠L) | theorem | If a measurable cardinal exists then V≠L | embedding,V=L absoluteness
- Iterated ultrapowers | technique | Iterating Ult by image measure to produce a chain of embeddings | ultrapower
- Ramsey cardinal | state | κ→(κ)^{<ω}2 | partition relations
- Erdős cardinal κ→(α)^{<ω} | state | Least κ with the partition relation for ordinal α | partition relations
- Indiscernibles / Ehrenfeucht–Mostowski models | technique | Order-indiscernibles generating elementary submodels via Skolem functions | Skolem,partition
- κ→(ω1)^{<ω} ⟹ 0# exists | theorem | An Erdős/Ramsey cardinal gives indiscernibles for L, hence 0# | indiscernibles,Erdős cardinal
- Strongly compact cardinal | state | Every κ-complete filter extends to a κ-complete ultrafilter | embeddings,ultrafilters
- Huge cardinal | state | ∃j:V→M with crit κ and ^{j(κ)}M⊆M | embeddings,closure
- Extenders | technique | Systems of ultrafilters coding strong embeddings | ultrapowers
- Reflection principle (ZF) | theorem | Lévy–Montague: arbitrarily large Vα reflect any finite list of formulas | Replacement,hierarchy
- Vopěnka's principle | axiom | Every proper class of structures has one elementarily embedding into another | embeddings,proper classes
- Proper forcing | state | Forcing preserving stationary subsets of [λ]^ω; preserves ω1 | stationary,elementary submodels
- Countable-support iteration | technique | Iterating proper forcings with countable support | proper forcing,iteration
- Properness preserved under CS iteration | theorem | CS iterations of proper forcings are proper | CS iteration

## Descriptive set theory
- Baire space ω^ω | state | Infinite sequences of naturals with product topology; canonical space of reals | product topology
- Cantor space 2^ω | state | Infinite binary sequences; compact perfect totally disconnected Polish space | Baire space
- Baire space homeomorphic to the irrationals | theorem | ω^ω ≅ irrational reals via continued fractions | Baire space
- Universality of Baire space | theorem | Every Polish space is a continuous image of ω^ω | Baire space
- Tree on a set / body [T] | state | Tree of finite sequences closed under initial segments; [T]=infinite branches=closed set | finite sequences
- Well-founded tree / rank | state | Tree with no infinite branch; ordinal rank by well-founded recursion | tree,well-foundedness
- Borel hierarchy (Σ0_α,Π0_α,Δ0_α) | state | Transfinite stratification of Borel sets | Borel,ordinals
- Borel codes | technique | Each Borel set has a real code; Borel relations absolute and definable | Borel,coding
- Baire category theorem | theorem | In a complete metric space the intersection of countably many dense open sets is dense | complete metric space
- Property of Baire (Baire property) | state | A=open set modulo meager set; BP sets form σ-algebra closed under Suslin operation | meager,Borel
- Suslin operation (operation 𝒜) | technique | 𝒜_s A_s=∪_f∩_n A_{f↾n}; generates analytic sets from closed sets | sequences,trees
- Coanalytic set Π¹1 | state | Complement of an analytic set | analytic
- Tree representation of analytic sets | technique | A is Σ¹1 iff A=p[T] for a tree T on ω×ω | tree,projection
- Suslin's theorem (Σ¹1∩Π¹1=Borel) | theorem | A set is Borel iff both analytic and coanalytic | analytic,coanalytic,Borel
- Lusin separation theorem | theorem | Two disjoint analytic sets can be separated by a Borel set | analytic,Borel
- Cantor–Bendixson theorem | theorem | Every closed subset of a Polish space = perfect kernel ∪ countable scattered set | perfect set,ordinals
- Cantor–Bendixson derivative/rank | technique | Iterated removal of isolated points stabilizing at a countable ordinal | CB theorem
- Perfect set property (PSP) | state | A set is countable or contains a perfect subset | perfect set
- Analytic sets have the perfect set property | theorem | Every uncountable analytic set contains a perfect subset | analytic,perfect
- Analytic sets are Lebesgue measurable | theorem | Every Σ¹1 set is Lebesgue measurable | analytic,measure
- Analytic sets have the Baire property | theorem | Every Σ¹1 set has the BP | analytic,BP
- Universal analytic set | state | A single Σ¹1 set universal for all Σ¹1 subsets; gives Σ¹1≠Π¹1 | analytic
- Π¹1 norm / rank | technique | A Π¹1-norm assigns each x the ordinal rank of its well-founded tree (<ω1) | Π¹1,ordinal rank
- Boundedness theorem (Σ¹1-bounding) | theorem | A Σ¹1 set of well-founded trees has bounded ranks below ω1 | Σ¹1,Π¹1 norm
- Projective hierarchy (Σ¹_n,Π¹_n,Δ¹_n) | state | Σ¹1=analytic; Π¹_n complements; Σ¹_{n+1}=projections of Π¹_n | analytic,projection
- Universal Σ¹_n sets / hierarchy is proper | theorem | For each n a universal Σ¹_n set; hierarchy strictly increasing | projective,diagonalization
- Uniformization | state | Selecting a single y per x with (x,y)∈R, graph in a pointclass | relations,pointclass
- Kondô uniformization theorem (Π¹1) | theorem | Every Π¹1 relation can be uniformized by a Π¹1 function | Π¹1,scale
- Σ¹2-uniformization (Novikov–Kondô–Addison) | theorem | Every Σ¹2 set can be uniformized by a Σ¹2 set | Kondô
- Prewellordering property | state | Every set in Γ admits a Γ-norm; Π¹1, Σ¹2 have it | norm,pointclass
- Scale property / scale | state | Sequence of norms with convergence enabling uniformization | norm,prewellordering
- Periodicity theorems (Moschovakis) | theorem | Under determinacy PWO/scale property alternates up the projective hierarchy | determinacy,scale
- Shoenfield absoluteness theorem | theorem | Σ¹2/Π¹2 statements absolute between V and any inner model with all countable ordinals | Mostowski absoluteness,trees,L
- Shoenfield tree | technique | Tree on ω×ω1 representing a Σ¹2 set; reduces membership to well-foundedness | Shoenfield,tree
- Σ¹2 well-ordering under V=L | theorem | If V=L there is a Σ¹2 well-ordering of the reals; gives non-measurable Δ¹2 set | L,projective
- Constructible reals ℝ∩L | state | The reals of L; Σ¹2; under V=L equal all reals | L,projective

## Infinite games & determinacy
- Infinite game G(A) / strategy | state | Two players alternately play naturals; I wins iff x∈A; strategy dictates moves | Baire space
- Determinacy of a set Det(A) | state | One player has a winning strategy in G(A) | infinite game
- Gale–Stewart theorem (open/closed determinacy) | theorem | Every open and closed game is determined | infinite game,trees
- Borel determinacy (Martin) | theorem | Every Borel game is determined (in ZFC) | Gale–Stewart,Borel
- Unraveling / covering technique | technique | Lifting a game to a higher tree where the payoff is clopen | Borel determinacy
- AD ⟹ all sets Lebesgue measurable | theorem | Under AD every set of reals is Lebesgue measurable | AD,measure
- AD ⟹ Baire property for all sets | theorem | Under AD every set of reals has the BP | AD,Banach–Mazur
- AD ⟹ perfect set property for all sets | theorem | Under AD every uncountable set of reals contains a perfect subset | AD,perfect
- Banach–Mazur game | technique | Players play decreasing basic open sets; characterizes comeager/BP | infinite game,BP
- Analytic (Σ¹1) determinacy | theorem | Every analytic game is determined; equiv to sharps; from a measurable | sharps,measurable
- Sharps x# and determinacy equivalence | state | Existence of x# for all reals x is equivalent to analytic determinacy | sharps,analytic determinacy
- Homogeneous tree / homogeneously Suslin set | technique | Tree with a coherent system of measures whose projection is determined | tree,measure,Woodin
- Martin–Steel theorem (projective determinacy) | theorem | n Woodin cardinals (measurable above) imply Π¹_{n+1} determinacy; ω Woodins ⟹ PD | Woodin,homogeneous trees
- Woodin: AD^{L(ℝ)} from ω Woodins | theorem | ω Woodin cardinals with a measurable above imply L(ℝ)⊨AD | Woodin,AD,L(ℝ)
- PD ⟹ regularity for all projective sets | theorem | PD implies every projective set is measurable, has BP, PSP, and uniformization | PD,periodicity
- AD equiconsistent with infinitely many Woodins | theorem | Con(ZF+AD) ⟺ Con(ZFC+∞ Woodin cardinals) (Woodin) | AD,Woodin
- Wadge reducibility / Wadge hierarchy | state | A≤_W B iff A=f^{-1}(B) for continuous f; degrees nearly well-ordered under determinacy | continuous reductions,determinacy
- Wadge's lemma | theorem | Under determinacy, for any A,B either A≤_W B or B≤_W complement of A | Wadge,determinacy
- Solovay's model construction via Lévy collapse | technique | Lévy collapse of an inaccessible gives ZF+DC model where all sets are measurable/BP/PSP | Lévy collapse,inaccessible
- Shelah: inaccessible necessary for all sets Lebesgue measurable | theorem | "All sets Lebesgue measurable" implies ω1 inaccessible in L | Solovay model,inaccessible
