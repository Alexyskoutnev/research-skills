# How to Write a Method Section
### A plain-English guide. No jargon. Follow the steps.

*Distilled from forensic dissections of fifteen papers by three leading ML
researchers, the classic writing guides, and the canonical ML papers. Sibling of
`intro-related-writing/` — same voice, same recipe style — but for the paper's
center of mass: the Method section.*

Throughout, one invented toy system carries the examples: **PlanCache**, which
routes a courier over a road graph by searching for a path and reusing
previously solved subroutes. Its three parts are the **router** (searches the
graph), the **subplan cache** (stores solved subroutes keyed by their
endpoints), and the **replay checker** (re-verifies a cached subroute still
holds before it is committed). Nothing about PlanCache is real; it exists only to
fill the templates with something concrete.

---

## Part 0 — The terms you need, in plain words

Reviewers and writing coaches use special words for the parts of a method
section. Here is what they actually mean. You never have to say these words; you
just have to do them.

| Fancy term | Plain meaning | Example |
|---|---|---|
| **Notation** | The symbols you name once and reuse. Each costs the reader memory. | "A state $s$ is a node in the road graph $G$; the cache is $C$." |
| **Formalism** | Writing the object as math — a tuple, an equation, a constraint — instead of prose. | "$G=(V,E)$ with a query $(s,g)$." Use it only where it earns its keep. |
| **Pseudocode / algorithm box** | A numbered, boxed recipe of the procedure, captioned like a figure. | "Algorithm 1: PlanCache." SMALL-CAPS steps, line numbers, knobs inside. |
| **Running example** | One concrete instance you thread through every subsection so the reader has intuition first. | "Route a courier from the depot to 12 Oak St." |
| **Roadmap sentence** | The opener that names the N parts in order, before any math. | "We describe the setup, the router, the cache, and the checker." |
| **Setup / Preliminaries** | The first subsection that banks all notation and fences off what is not your contribution. | "Problem statement and representation." |
| **Subsumption** | State the general object, then list the special cases it recovers ("reduces to X when…"). | "Uncached search falls out as the corner where the cache is empty." |
| **Coined component** | A named part, bolded once, then used as a proper noun instead of a description. | "the **subplan cache**," never "our storage step." |
| **Credit-then-contrast** | Praise a neighbor fully, then differ on one axis. Never call it wrong. | "Following prior search-caching work, we instead check each hit before reuse." |
| **Hermetic seal** | The method holds no benchmark numbers, no survey, no limitations — those live elsewhere. | Solve-rates wait for Experiments. |
| **Per-module vs per-timestep** | Two ways to narrate a loop: component-by-component, or step-in-time. Pick one; don't mix. | Pipeline per-module; Algorithm 1 per-timestep. |
| **Handoff** | The last sentence: what the system *can now do*, then straight into Experiments. | "Every reused subroute is checked before it is committed." |

That is all the theory. Everything below is recipes and checklists.

---

## Part 1 — The big secret: the method is N named parts, introduced in a stated order

An introduction is a funnel that answers seven questions. A method section is
simpler and more mechanical: **it is a small number of named parts, announced up
front, then installed one at a time until the system visibly assembles.** This is
the strongest shared fingerprint across the dissected papers — declare N named
parts, then spend the section installing exactly those N parts in order. The
count gravitates to three. No part appears that was not promised in the roadmap.

Three structural rules govern the order:

1. **Overview first.** One roadmap sentence names the parts; often one
   architecture figure and a one-paragraph plain-words overview follow. The
   reader is told the shape before the first symbol. Peyton Jones: "Conveying the
   intuition is primary … once your reader has the intuition, she can follow the
   details (but not vice versa)."
2. **Setup second.** A dedicated subsection banks all notation and fences off the
   borrowed material (Widom's Preliminaries: "delineate material that's not
   original but is needed"). Nothing floats; every symbol is defined at first use.
3. **Star component fattest.** The one genuinely new piece gets the most space and
   the most defense; the plumbing every rival also has is compressed. Kording &
   Mensh: "focus on a single message." For PlanCache the star is the **subplan
   cache** — the search is the easy half every rival already has.

The rest of the section is: the components each introduced alone, the objective
or criteria stated as numbered equations, the parts composed into a loop (figure
+ algorithm box), and a one-sentence handoff to experiments. That is the
skeleton. The three recipes below are three ways to flesh it.

---

## Part 2 — The three recipes

The dissected papers cluster into three ways of building the skeleton. Pick the
one that fits your system, and match the one your closest rival uses — a native
register reads as native to the reviewer who wrote it.

### Recipe A: N named parts, coined and sealed
*Use when: your system is a small set of mechanisms that assemble into a loop, and
your closest rival writes this way. This is the default voice for a
mechanism-built system.*

What the recipe does, in plain words:
- **Opens with a roadmap that names the N parts in order.** "beginning with an
  overview … then turning to the details of its three phases." No math in the
  opener.
- **Banks notation in a dedicated first subsection**, often by "modifying a
  standard formalism in a numbered list" ("We start with the standard MDP
  formalism but modify it in three ways. First…").
- **Coins every component and bolds it once**, then uses it as a proper noun
  (the *router*, the *subplan cache*, the *replay checker*). Sub-components ride
  bold run-in headers, not new subsections.
- **Puts the algorithm box in about half the time**; when present it is titled
  with the system name, uses SMALL-CAPS subroutines, declares
  hyperparameters-with-defaults *inside the box*, and cross-references each line
  to its subsection.
- **Seals the section hermetically:** no benchmark numbers, no related-work
  survey, no limitations. The only leak forward is one bare capability sentence
  into Experiments.

**Fill-in template:**
> We describe [System], which [one-line job], in [N] parts: [part 1], [part 2], …
> and [part N].
> **[Setup subsection.]** We model the task as [formal object], modifying the
> standard [formalism] in [N] ways: First… Second… **[Coined component.]** The
> [**bold name**] [does X]. …
> **[Algorithm box, titled with the system name; SMALL-CAPS steps; defaults
> inside.]**
> We implement [the hard piece] using [tool], because [one-clause reason]. Using
> this, [System] can now [bare capability]. [→ Experiments.]

*Worked (PlanCache):* "We describe **PlanCache**, which routes a courier while
reusing solved subroutes, in three parts: the **router**, the **subplan cache**,
and the **replay checker**. We model routing as search over a graph $G=(V,E)$
with a query $(s,g)$… The **subplan cache** stores each solved subroute $\sigma$
keyed by its endpoints… See Algorithm 1 for the control flow. PlanCache can now
answer a query by stitching checked subroutes, expanding search only where the
cache misses."

### Recipe B: The pipeline recipe
*Use when: your method is a pipeline of prompt / retrieve / execute / verify steps
and there is little or nothing trained. Two of its moves — the pipeline figure
walked in prose, and contamination killed inside the method — graft cleanly onto
the other recipes.*

What the recipe does, in plain words:
- **Calls it "Methods" and puts it right after the intro** — never deferred to
  the tail.
- **Enumerates the method as three components** — bullets ("The key components
  leading to our success:") or numbered prose ("three-fold: Firstly… Secondly…
  Thirdly…").
- **Formalizes only what is trained.** Standard notation with numbered equations
  if there is learning; otherwise *no notation at all* — the "formalism" is the
  prompt string and the execution semantics.
- **Walks one pipeline figure in prose:** "Our pipeline consists of three
  components: encoding, simulation…, and decoding," with a long self-contained
  caption.
- **Writes the body as a recipe:** the exact prompt prefix, the
  embed-then-cosine-similarity retrieval, the execute-and-regenerate-until-correct
  loop, the verifier (unit test / compile / logical check). Each moving part
  coined and bolded.
- **Pre-empts contamination *inside* the method** — its own subsection in a big
  paper, one sentence in a small one ("Since the questions are not online, the
  model is not overfitting").
- **Ends with an implementation-details tail** (public code, fixed 0-temperature
  hyperparameters, "deterministic and reproducible") and a one-line bridge:
  "Next, we describe our … results."

**Fill-in template:**
> **Methods.** Here we describe our [dataset], [pipeline], and [evaluation]. The
> key components: [• component 1] [• component 2] [• component 3]. [Figure 1]
> shows our pipeline; it consists of [three components]. We [verb] the [input],
> [verb] it through [tool], and [verb-and-regenerate] until [success test].
> [Verifier, stated operationally.] [Contamination pre-empted in its own
> subsection or one sentence.] We fix [hyperparameters] for reproducibility.
> Next, we describe our results.

### Recipe C: The staircase
*Use when: your system is built from a familiar baseline plus one new primitive,
and you want to show the old settings falling out as special cases of the new one.*

What the recipe does, in plain words:
- **Runs a staircase, not a monolith.** The method is 3–6 consecutively-named
  sections — setup, then the familiar baseline on its own, then the new primitive
  on its own, then the composed named system last. The composed section is
  literally titled as the sum of the two prior sections (e.g. "CACHE + SEARCH").
- **Names the whole last.** The eponymous system arrives in the final method
  section, "assembled from independently-introduced pieces."
- **Uses the subsumption move:** state the general object, then enumerate what it
  recovers ("reduces to X when…"; "includes … as special cases"). Generality is
  *earned* by making the reader see the old models fall out as corners of the new
  one.
- **Defends by enumerated advantages** ("which has a number of advantages. First…
  Second…") and by **crediting-then-limiting the baseline** ("Plain search is a
  valuable approach … its weak point is that it re-solves subproblems it has
  already solved").
- **Earns a structural claim with a motivation figure *inside* the method** — a
  plot of the very quantity the method exploits, cited to justify the design
  before any experiment (for PlanCache, a figure showing how often subroutes
  recur across queries).
- **Bridges to experiments with a reflective "Why does it work?"** section that
  re-tests each assumption, rather than merely scoring the system.

**Fill-in template:**
> **[Setup.]** We solve [numbered problem]. **[Baseline section.]** [Familiar
> method] is a valuable approach because [virtue]; its weak point is [one
> structural limit] — this is our lever. **[New primitive section.]** We
> introduce [coined primitive], described on its own. **[The composed system,
> named last.]** [System] = [baseline] + [primitive]; see [figure] and
> [Algorithm 1]. This has a number of advantages. First… Second… Prior settings
> [A, B] fall out as special cases when [condition]. [Motivation figure earns the
> key assumption.] [→ "Why does it work?" experiments.]

---

## Part 3 — The devices recipe

Four devices carry a method section. Use each the same way every time.

### The one architecture figure (and its self-contained caption)
- **One figure carries the method; the prose annotates it.** Build the figure
  first, then write to it. MuZero's Fig 1 (A/B/C), DreamerV3's Fig 3 (a/b),
  Voyager's Fig 2 (three modules) each *are* the method.
- **Walk it in prose, left to right.** "Figure 1 is a high-level architecture of
  our approach … Our pipeline consists of three components."
- **The caption re-tells the whole pipeline, self-contained.** A reader who reads
  only the caption should get the method; the dissected captions are long,
  self-contained, and colour-keyed.
- *Toy:* PlanCache's Figure 1 shows the query flowing into the router, the router
  reading and writing the cache, the checker gating each cached subroute, and the
  committed route leaving on the right; the prose walks it left to right, and the
  caption alone conveys the loop.

### The algorithm box (when, and what goes inside)
- **Use it only when there is a real procedure or loop.** In the dissected papers
  a box appears only where there is a genuine procedure — roughly half the time;
  otherwise a labeled multi-line equation or the master figure stands in.
- **Inside the box:** title it with the system name; number the lines; put
  subroutines in SMALL-CAPS; declare hyperparameters *with defaults inside the
  box* ("cache capacity, default 1000"); add right-margin `▷` comments
  cross-referencing each line to its subsection.
- **The box states *what*; the prose states *why it is right and why it wins***
  (Zobel). Point at the box — "See Algorithm 1 for the control flow" — never
  transcribe it line by line in the body.
- *Toy:* Algorithm 1 is titled PlanCache, numbers its lines, puts
  \textsc{CacheLookup}, \textsc{Search}, \textsc{Check}, \textsc{Commit}, and
  \textsc{Store} in SMALL-CAPS, and declares the cache capacity and the search
  depth limit as defaults inside the box.

### The running example (concrete-first, every subsection)
- **Lead with a concrete instance, then generalize.** Peyton Jones: "use EXAMPLES
  and only then present the general case." Widom: "use a running example
  throughout the paper." Every dissected author does this — a single concrete
  instance carried from the first subsection to the last.
- **Thread *one* named instance through the whole method** so intuition precedes
  every equation.
- *Toy:* thread one delivery — the courier from the depot to 12 Oak St — through
  the router (it searches for a path), the cache (the depot→Main St leg is a
  stored subroute), the checker (Main St is closed today, so the subroute fails
  its check), and the commit (the router re-plans that leg only).

### Notation hygiene
- **Notation is a cost — spend it only where it earns its keep** (Knuth).
  Introduce a *tiny* symbol set and reuse it relentlessly (MuZero's h/g/f; ReAct's
  $\hat A = A \cup L$).
- **Define every symbol at first use; never open a sentence with a symbol; separate
  symbols in different formulas with words.** Bank notation under bold run-in
  headers, not dribbled in as needed.
- **State the object as a numbered display and reuse it by number** ("the reused
  subroute satisfies Eq. (valid)"). Equation numbers are the paper's skeleton.

---

## Part 4 — The mechanical checklists

Run these on the finished draft. Each box is a search-and-fix, not an opinion.

### Method-section checklist
- [ ] The opener is a **roadmap sentence** naming the N parts in order — no math
  in it.
- [ ] The section is **not titled a bare "Method"** — a content or mechanism name
  (or at least "Methods").
- [ ] There is a **dedicated setup subsection** that banks all notation; no symbol
  appears before it.
- [ ] Every **component is coined and bolded once**, then used as a proper noun.
- [ ] The **star component is the fattest** subsection; shared plumbing is
  compressed.
- [ ] **One architecture figure**, walked in prose, with a self-contained caption.
- [ ] The **algorithm box** (if any) is titled with the system name, line-numbered,
  SMALL-CAPS steps, knobs-with-defaults inside, cross-referenced to subsections.
- [ ] **One running example** is threaded through every subsection (concrete
  before formal).
- [ ] The objective/criteria are **numbered equations**, one idea each, reused by
  number.
- [ ] Each design choice is **defended in one clause**, in-line, not in a rationale
  subsection.
- [ ] Rivals are **credited-then-contrasted on one axis**; the nearest rival
  credited warmly.
- [ ] The loop is narrated on **one axis** (per-module *or* per-timestep), no
  zig-zag.
- [ ] The **handoff** is one forward-looking capability sentence into Experiments.
- [ ] Prose axioms hold: sentences <= ~28 words, subject+verb early, **zero
  "can"/"could"**, no bare "This"/"These", numbers paired and attached to exact
  objects.

### Prohibitions checklist (search-and-delete)
- [ ] Search benchmark numbers, solve-rates, and deltas → **none in the Method
  body.** The one legal leak is a bare capability sentence, not a scoreboard.
- [ ] Search for a **literature survey** inside the method → cite prior work only
  *instrumentally* (the tool you reuse), never to survey a field.
- [ ] Search for a **limitations paragraph** → at most single scoping clauses
  ("certifies consistency with observed data, not correctness on unseen states").
- [ ] Search for a **hyperparameter dump in prose** → move to the algorithm box as
  defaults, or to an appendix.
- [ ] Search "can" / "could" → **zero hits.** Search bare "This " / "These " →
  each has a noun.
- [ ] Every number is attached to the **exact object** it measures and none is
  conflated — but all of them belong in Experiments regardless, not here.
- [ ] Coined names are used consistently — no component drifts to a generic phrase
  ("our storage step") after it was named.

### What NEVER goes in the method
- Benchmark numbers, solve-rates, deltas, or a results/learning-curve plot —
  Experiments.
- A standalone Related Work or literature survey — Related Work; here, cite only
  the tool you reuse.
- A limitations or failure-mode discussion — Discussion; a single scoping clause
  is the ceiling.
- A hyperparameter table in prose — inside the algorithm box as defaults, or an
  appendix.
- Author names as sentence subjects — systems and ideas are the doers; names ride
  in "cf." asides.
- A "The rest of this section is organized as follows" paragraph — the roadmap
  sentence does that job.

---

## Part 5 — The assembly order

A concrete drafting sequence, synthesizing the three recipes' spines — the
N-part skeleton, the parts-then-composition staircase, and the pipeline-figure
recipe — ending in the handoff to experiments.

1. **Draw the architecture figure first, and write the section to it.** The
   caption re-tells the whole pipeline.
2. **Write the roadmap opener** — one sentence naming the N parts in order, no
   math — and **name the section for its mechanism**, never a bare "Method."
3. **Bank the setup and notation** in a dedicated first subsection under bold
   run-in headers; every symbol defined at first use.
4. **Introduce each shared component alone and briefly** — coin and bold each —
   and state the pipeline's invariant where it appears. Keep it compact: this is
   the plumbing rivals share.
5. **State the objective/criteria as numbered displays**, one idea each; credit
   the nearest rival warmly and contrast on the one axis that matters.
6. **Fatten the star** into the longest, most-defended subsection — the one
   primitive rivals lack.
7. **Give the algorithm box** with SMALL-CAPS primitives, search knobs as
   inside-the-box defaults, and per-line subsection cross-references; let it carry
   the per-timestep control flow so the prose stays per-module.
8. **Thread one running example** back through every subsection, and **earn the
   central structural claim inside the method** — the fact that makes your star
   the hard half.
9. **Pre-empt the validity threat inside the method** (contamination, leakage),
   keeping limitations to single clauses and hyperparameters out of the prose.
10. **Hand off to experiments** with one forward-looking capability sentence and a
    pre-named ablation axis — no benchmark number crosses the boundary.

### A worked example: the toy planner on the recipe

Here is PlanCache mapped onto the skeleton, subsection by subsection — the shape a
finished method section takes.

- **`\section{Planning with a checked subroute cache}` + opener + Figure 1.** The
  roadmap sentence names the three parts in order ("we cover the setup, the
  router, the subplan cache, and the replay checker"); Figure 1 shows the loop and
  its caption re-tells it. The title names the mechanism, not a bare "Method."
- **`\subsection{Problem statement and representation}`.** Banks the notation
  under bold run-ins — the graph $G=(V,E)$, a query $(s,g)$, a route $r$, the
  cache $C$, a subroute $\sigma$ — and introduces the running example (depot to 12
  Oak St) concretely before the abstract graph.
- **`\subsection{Router and checker}`.** The two shared components, each coined,
  bolded once, introduced alone and kept **compact** — this is plumbing a plain
  search baseline also has. The invariant is stated where it appears: no subroute
  is committed while its check is failing.
- **`\subsection{The two criteria}`.** Eq. (valid) — every reused subroute's edges
  still exist in $G$ — and Eq. (reach) — the route connects $s$ to $g$ — as
  numbered displays, one idea each. Credit prior search-caching work, contrast on
  one axis (we check each hit before reuse rather than trusting it).
- **`\subsection{The subplan cache}` — the star, the fattest subsection.** The
  reuse primitive rivals lack earns the most space and the most defense, plus
  Algorithm 1 (titled PlanCache, SMALL-CAPS primitives, cache capacity and depth
  limit as inside-the-box defaults). Here the structural claim is earned: recurring
  subroutes are what make reuse pay, so a motivation figure shows their recurrence.
- **Handoff.** One forward-looking sentence — "PlanCache answers each query by
  stitching checked subroutes and searching only where the cache misses" — and the
  pre-named ablation ("without the cache"), then straight into Experiments. No
  solve-rate crosses the boundary.

---

**Semicolon rule (addendum).** A semicolon is earned only by a true antithesis or
tightly parallel pair; everything else takes a period. Budget about two per section.
After any editing pass, grep `;` — each survivor must name its antithesis or become a
period.
