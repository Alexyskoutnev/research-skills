# How to Write a Results Section
### A plain-English guide. No jargon. Follow the steps.
*Distilled from forensic dissections of fifteen papers by three leading ML
researchers, the classic writing guides, and the canonical ML papers. Sibling of
`method-writing/`: same voice, same recipe style, but for the section where the
evidence lands: the Results.*

Throughout, one invented toy system carries the examples: **PlanCache**, which
routes a courier over a road graph by searching for a path and reusing previously
solved subroutes. Its three parts are the **router** (searches the graph), the
**subplan cache** (stores solved subroutes keyed by their endpoints), and the
**replay checker** (re-verifies a cached subroute still holds before it is
committed). Its results world is equally invented: a suite of **200 courier
queries** over a city road graph, **60** of them carrying a scheduled road
closure (the edited-map subset) and **140** static; a composite **route score**
(optimality × search-efficiency, 1 is best); and the rival planners named below.
Nothing about PlanCache is real; it exists only to fill the templates with
something concrete.
The thesis PlanCache's results must land is fixed, and it is the shape most
systems papers carry: **reuse is the easy half; keeping reused subroutes valid
and shortest as the map changes is the hard half, and we measured it.** So the
ablation (route score $0.72$ without the cache versus $0.90$ with it) and the
under-change drill-down carry the argument; the aggregate scoreboard is the
setting, not the point.
---

## Part 0: The terms you need, in plain words

Reviewers and writing coaches use special words for the parts of a results
section. Here is what they actually mean. You never have to say these words; you
just have to do them.
| Fancy term | Plain meaning | Example |
|---|---|---|
| **Purpose opener** | The first sentence(s), naming the questions the section will answer, no result yet. | "asking two questions: does reuse make the planner faster, and do reused subroutes stay valid?" |
| **Claim-first paragraph** | The topic sentence is the finding in English; the number is its evidence, not its lead. | "PlanCache is search-efficient … then the $1{,}180$-vs-$3{,}940$ node counts." |
| **Paired numbers** | Every number carries a partner: before/after, ours/theirs, or fraction-and-percent. | "$196/200$ ($98\%$)"; "$0.72$-to-$0.90$." |
| **Lesion / ablation** | Remove one named component and report the drop, to prove the component is load-bearing. | "remove the cache: $0.90 \to 0.72$." |
| **Necessity claim** | The ablation's verdict, stated as "X is necessary for Y." | "the cache is decisive." |
| **Per-example drill-down** | One concrete case narrated in domain terms, to show what the mean cannot. | "one delivery keeps $5$ of $6$ legs cached yet needs a re-plan when Main St closes." |
| **Credit-then-contrast** | Praise a rival fully, then differ on one axis. Never call it wrong; never a pejorative. | "GreedyReuse expands the fewest nodes on the static queries." |
| **Fairness declaration** | Stating the comparison's fairness out loud, up front, before anyone objects. | "one map against one map"; "only the PlanCache–PlainSearch pair shares the identical router." |
| **Self-contained caption** | A caption that states the conclusion and decodes every series, readable alone. | "PlanCache expands fewer nodes on $168$ of $171$ shared queries." |
| **Reading key** | The decoder printed inside the caption or table note. | "lower is faster"; "**bold** marks strict wins." |
| **Hermetic seal** | Results hold no method re-introduction, no new component, no literature survey. | The ablation names the **checker**, never re-explains it. |

That is all the theory. Everything below is recipes and checklists.
---

## Part 1: The big secret: results are a sequence of claims, each discharged by a paired number

A method section is N named parts that assemble. **A results section is a
sequence of claims, each one discharged by a number, all organized by a stable
unit and all traceable to a promise made in the abstract.** Kording & Mensh Rule
7: deliver the results as a sequence of statements, supported by figures, that
connect logically to support the central contribution. Peyton Jones's model of a
whole paper is claim → evidence, and the results section is where the evidence
lands.
Four structural rules govern the shape:
1. **Purpose first.** One or two sentences name the questions the section answers, not a result. The reader is told what is on trial before any number.
2. **A stable organizing unit, never a metric.** Organize by benchmark, by
   domain, or by rival, never a "Metrics" subsection then a "Baselines"
   subsection. Setup facts live inside the blocks.
3. **Star evidence fattest.** The one result that carries the thesis gets the most
   weight. For PlanCache the thesis is **reuse is the easy half, staying valid and
   shortest under change is the hard half, and we measured it**: so the ablation
   ($0.72$ without the cache vs. $0.90$) and the under-change drill-down ($48$ of
   $60$ edited-map queries kept optimal) carry the argument, not the scoreboard.
4. **Every number pays rent.** Each figure, table, and statistic traces to a claim
   promised earlier; cut anything that defends no promised claim.
The rest is: the setup banked in a few paragraphs, the findings as claim-headed
blocks each ending on its answer, the ablation as a lesion, one per-example
drill-down, a terse Limitations, and a hard seal against method re-introduction.
The three recipes below are three ways to flesh it.
---

## Part 2: The three recipes

The dissected papers cluster into three ways of building the section. Pick the one
that fits your system, and match the one your closest rival uses, a native
register reads as native to the reviewer who wrote it.
### Recipe A: Per-claim discharge, lesion ablations, claim-carrying captions
*Use when: your system is one method shown across many tasks, and your closest
rival writes this way. This is the default voice for a mechanism-built system
evaluated across a task suite.*

What the recipe does, in plain words:
- **Opens with a purpose sentence** naming the domains and what each is there to
  probe, no result.
- **Organizes by domain, not metric.** Each domain is a bold run-in header and a
  self-contained mini-study: one-line description, setup, main finding as
  claim+number+named rival, and the ablation of the relevant component woven in.
- **Opens each paragraph with a CLAIM, then discharges it with a number.** Never a
  naked statistic: "PlainSearch answers only $171$ of $200$ within budget, showing
  that search without reuse does not scale to long routes."
- **Runs ablations as lesion studies** with coined, one-line-defined variant names
  mapped to method components, and states the verdict as necessity: "the cache is
  necessary for any budget-feasible answer on the long routes." Null results are
  reported honestly and used as a segue.
- **Writes captions that state the claim and stand alone**, naming each baseline's
  handicap in the caption body.
- **Seals the section:** no method re-introduction, no new component, no
  related-work survey, no limitations dump; scope claims rather than chest-thump.
**Fill-in template:**
> We study [System] on [set], asking [the question(s) each result probes]. **[Claim
> header.]** [System] [does X], [claim in words], [number] versus [named rival]'s
> [number]. **[Ablation.]** Removing [**named component**] drops [metric] from [Y]
> to [Z], showing [component] is necessary for [effect]. [Caption states the claim
> and decodes every series.] [Scope the win; state any loss plainly.]

### Recipe B: Benchmark-by-benchmark, action-first, limitations inside results
*Use when: your method is an agent or pipeline evaluated on a benchmark suite, and
you want one clean benchmark report with the honest boundary sitting beside the
evidence.*

What the recipe does, in plain words:
- **Names it "Results"** for an agent/pipeline and puts it right after the method.
- **Organizes by benchmark**, each subsection a self-contained mini-report with its
  own setup and number.
- **Opens each subsection action-first:** "We evaluate PlanCache and three rivals
  on $200$ courier queries." The number arrives one or two sentences later, not as
  a claim-first topic sentence.
- **Writes the "whereas" comparative:** "PlainSearch answers $171/200$ within
  budget, whereas PlanCache answers $196/200$." Numbers are paired as
  fraction-and-percent; improvements are from→to, never a bare delta.
- **Names every rival inline**, credits it, then out-scopes honestly: "GreedyReuse
  expands the fewest nodes on the static queries. However, it commits $12$ stale
  routes once closures appear."
- **Puts a Limitations subsection inside Results** as a flat list, each item
  reframed as future work, followed by a reflective zoom-out placing the number
  against the upper bound.
- **Pre-empts validity in-line** (the shared human/oracle baseline, the fairness
  protocol, the compute the metric ignores) rather than deferring it.
**Fill-in template:**
> **Results.** We evaluate [our method] on [set of N]. [Our method] scores
> [$n/N$ ($p\%$)] whereas [named rival] scores [$m/N$]. [Read the headline figure
> line by line, numbered.] [Credit the rival where it wins; out-scope honestly.]
> [Validity pre-empted in-line.] **Limitations.** [Flat numbered list, each routed
> to future work.] [Reflective zoom-out vs. the upper bound.]

### Recipe C: Axis-titled, rival-by-rival, "why does it work?"
*Use when: your system is a learned system with an offline/online split and named
rival systems, and you want a fairness-first, self-interrogating register.*

What the recipe does, in plain words:
- **Never titles it "Results" or "Experiments"**: names the axis of evaluation
  ("SPEED," "COMPUTATIONAL EVIDENCE," "EXPERIMENTAL EVALUATION").
- **Opens on reproducibility infrastructure**, not a result: hardware, the
  single-core fairness constraint, the code URLs, the uniform preprocessing,
  stated once and "used in all the experiments."
- **Enumerates the rivals in one breath**, each cited and given a one-clause
  identity, then names the metric and the fairness protocol ("for a fair
  comparison, we show both a warm-cache and a cold-cache version").
- **Delivers findings as a numbered list of claim-sentences**, each stating a delta
  against a named rival and interpreting it ("more than $3\times$ fewer expansions
  than PlainSearch … This indicates the cache, not the heuristic, carries the
  speed").
- **Re-casts the ablation as a question, "Why does it work?"**: that concedes the
  load-bearing assumption first, then tests it with bold-run-in micro-experiments.
- **Keeps tables data-only** (no bold winner cells, no significance stars); the
  reader picks the winner; robustness is medians and interquartile bands over many
  draws.
- **Closes on one real-world drill-down** narrated in domain terms, for
  interpretability and stakes.
**Fill-in template:**
> **[Axis of evaluation].** [Hardware; single-core fairness; code URLs; uniform
> preprocessing, used in all experiments.] We compare [rival 1 [cite], rival 2
> [cite], … each a one-clause identity]. **[Rival subsection.]** [Numbered
> claim-list: 1 … 2 … 3 …, each a delta + interpretation.] **Why does it work?**
> [Concede the assumption; test it with bold-run-in probes.] [One real-world
> drill-down.]

---

## Part 3: The devices recipe

Five devices carry a results section. Use each the same way every time.
### The purpose opener (questions, not a result)
- **State the design logic, not an outcome.** A strong opener says what is on trial, "with the goal of understanding whether reuse pays and whether reused subroutes
  stay valid", with no number in it. Kording & Mensh: the first results paragraph
  gives the gist.
- Keep it number-free; make each subsection answer exactly one previewed question.
### The claim-stating caption (and its reading key)
- **The title/caption states the conclusion; the legend explains how it was done**
  (Kording & Mensh / Tufte). A skimmer who reads only the figure must learn the
  finding.
- **Decode every series and print the reading key inside the caption or table
  note**: each baseline's handicap, the failure marker, "$1$ is best."
- *Toy:* the scoremap caption states the four means (Oracle $1.00$ / PlanCache
  $0.90$ / GreedyReuse $0.78$ / PlainSearch $0.72$) and the route-score formula;
  the efficiency caption states "PlanCache expands fewer nodes on $168$ of $171$
  shared queries." Keep the keys (lower is faster; dashed line is the oracle;
  **bold** marks strict wins) in caption and note, never in the prose.
### The ablation (lesion mapped to a named component)
- **Remove one named component; report the drop; state the verdict as necessity.**
  The ablation exists to license "component X is load-bearing." Voyager removes its
  design choices one at a time with quantified drops.
- **Isolate one variable at a time** where the design allows; where you remove a
  bundle, say so.
- *Toy:* removing the **subplan cache** drops route score $0.90 \to 0.72$ and
  coverage $196 \to 171$ of $200$; the verdict is "the cache is decisive." If the
  cache is removed together with the checker, say the lesion is a bundle and name
  that in Limitations.
### The per-example drill-down (what the mean cannot show)
- **Narrate one concrete case in domain terms.** One held-out instance, one grouped
  cluster, one named hero case. The point is stakes and interpretability, not
  another mean.
- *Toy:* the drill-down is the thesis measured, one delivery (depot to $12$ Oak
  St) serves $5$ of $6$ legs from cache, then Main St closes; the checker catches
  the stale depot→Main St leg, the router re-plans that leg only, and the route is
  valid but two blocks longer than the true shortest. Validity is cheap; global
  optimality under change is the hard half.
### Number discipline
- **Numbers travel in pairs**: before/after, ours/theirs, fraction-and-percent. A
  bare single number is the exception.
- **Name every rival inline** with its identity; never "the baseline" or "prior
  work."
- **Trace every number to a promised claim** and forward-reference it; cut numbers
  that defend nothing.
---

## Part 4: The mechanical checklists

Run these on the finished draft. Each box is a search-and-fix, not an opinion.
### Results-section checklist
- [ ] The opener is a **purpose sentence** naming the questions, no number in it.
- [ ] The body is organized by a **stable unit** (benchmark / claim-question),
  **not by metric**; no standalone Metrics / Baselines / Datasets subsection.
- [ ] Each **subsection header is a declarative claim**, and each paragraph answers
  it in its last sentence.
- [ ] Each finding **opens as a claim, then discharges a number** (findings); setup
  paragraphs may open action-first.
- [ ] **Every number is paired** (before/after, ours/theirs, or $n/N$ + $p\%$); no
  naked statistic.
- [ ] Every **rival is named inline** with its identity and citation.
- [ ] The **ablation is a lesion mapped to named components**, verdict stated as
  necessity.
- [ ] There is **one per-example drill-down** narrated in domain terms.
- [ ] **Captions state the conclusion** and decode every series; reading keys and
  baseline handicaps live in caption/note, not prose.
- [ ] Tables are **ordered by the headline metric**, column order fixed, metric
  defined once.
- [ ] **Fairness is declared out loud** at the point of comparison ("one run
  against one run").
- [ ] **Rivals are credited, losses stated plainly**; no pejorative anywhere.
- [ ] Prose axioms hold: sentences $\le \sim 28$ words, subject+verb early, **zero
  "can"/"could"**, no bare "This"/"These", no em dashes, numbers glued to exact
  objects.
### Prohibitions checklist (search-and-delete)
- [ ] Search for a **naked or unpaired number** → every headline number has a
  partner ($0.90$ beside $0.72$, $0.78$, $1.00$).
- [ ] Search for a **method re-introduction** → the ablation references components,
  never re-explains the loop.
- [ ] Search for a **literature survey** inside Results → positioning stays in
  Related Work.
- [ ] Search for **SOTA chest-thumping** → claims scoped ("of a possible $200$,"
  "$48$ of $60$").
- [ ] Search "can" / "could" → **zero hits.** Search bare "This " / "These " → each
  has a noun.
- [ ] Numbers never conflated, each rate is glued to the object it measures, and no
  two measurements are rounded together into one figure.
- [ ] Coined names are used consistently, no component drifts to a generic phrase
  ("our storage step") after it was named.
### What NEVER goes in the Results
- A method re-introduction, a new component, or a re-derivation. Method.
- A standalone Related Work or literature survey. Related Work.
- A pejorative toward a rival, or an unqualified "state of the art", scope it
  instead.
- A naked statistic, a bare delta, or an unpaired hero number.
- Author names as sentence subjects, systems and ideas are the doers.
- Two distinct rates merged into one rounded figure, keep each pinned to its own
  measurement.
---

## Part 5: A worked example: the toy planner on the recipe

Here is PlanCache mapped onto the skeleton, block by block, the shape a finished
results section takes. It runs **Recipe B** in shape (one benchmark, Limitations
inside Results) with **Recipe A** claim-headed findings and lesion ablation, and
the "one map against one map" fairness that stands in for error-bar-free honesty.
- **`\section{Experimental Results}` + the figures/tables + opening question
  paragraph.** The **purpose opener**: "asking two questions: does reuse make the
  planner faster, and do reused subroutes stay valid as the map changes?", carries
  no number. The scoremap, the efficiency bars, the aggregate table, and the
  per-query table each state their conclusion and print their reading key.
- **`\paragraph{Setup.}` + `\paragraph{Compute and protocol.}` +
  `\paragraph{Systems.}`** Action-first setup banking; every rival named with its
  identity. **PlainSearch** (the cache-removed ablation: identical router, cache
  off), **GreedyReuse** (reuses cached subroutes without re-checking), and the
  shortest-path **oracle** (upper bound). Fairness declared out loud: "one map
  against one map," "only the PlanCache–PlainSearch pair shares the identical
  router." The compute the metric ignores is disclosed, the route score counts
  node expansions, not the $1{,}000$-entry cache memory or the offline
  preprocessing seconds.
- **`\subsection{Reusing checked subroutes plans well}`.** The **claim-header**
  subsection; the paired headline (route score $0.90$, ahead of $0.78$ and $0.72$,
  under the oracle's $1.00$); the win decomposed into **parallel claim-headed
  paragraphs**: "The margin is widest on the long routes" and "PlanCache is
  search-efficient, expanding $1{,}180$ nodes versus PlainSearch's $3{,}940$ on the
  shared solves." **Credit-then-contrast** on GreedyReuse's win: it expands the
  fewest nodes on the $140$ static queries, then commits $12$ stale routes on the
  $60$ edited-map queries where PlanCache's checker holds.
- **`\subsection{Is it the cache? An ablation}`.** The **lesion ablation**:
  removing the **subplan cache** reports route score $0.90 \to 0.72$ and coverage
  $196 \to 171$ of $200$, verdict "the cache is decisive." The under-change
  paragraph is the **per-example drill-down** and the **thesis measurement**:
  reuse serves $64\%$ of legs (the easy half), the checker commits zero stale
  routes, yet PlanCache stays optimal on only $48$ of $60$ edited-map queries, the
  $12$ near-misses need a global reroute the local re-plan misses. Staying shortest
  under change is the hard half.
- **`\subsection{Limitations}`.** The **Limitations-inside-Results** move, terse,
  each boundary routed to "remain open": only the PlanCache–PlainSearch pair holds
  the router fixed; the cache and checker are lesioned as a bundle, not one at a
  time; validity is certified only against the closures actually logged; the metric
  counts node expansions, not cache memory.
### The number discipline (do not get this wrong)
| Number | What it is attached to | Never say |
|---|---|---|
| **$0.72 \to 0.90$** | ablation: same router **without vs. with the cache** | $0.90$ alone, unpaired |
| **$64\%$** | reuse rate, legs served from cache (the easy half) | never the optimality-under-change number |
| **$48/60$** | edited-map queries kept **optimal** under change (the hard half) | never merge with the reuse rate |
| **$196/200$ vs $171/200$** | coverage within the node budget, PlanCache vs PlainSearch | a bare delta with one endpoint |
| **$0.78$ / $1.00$** | GreedyReuse / the oracle upper bound | any pejorative toward the rival |

### The assembly line (do this, in order)
1. **Build the two figures and two tables first**, and write the section to them;
   each caption states its conclusion and prints its reading key.
2. **Write the purpose opener** naming the two questions, no number in it.
3. **Bank the setup** action-first: name every rival with its identity, declare
   "one map against one map," disclose the compute the metric ignores.
4. **Write the first claim subsection:** paired headline, then parallel
   claim-headed findings, each discharged with paired numbers; credit GreedyReuse's
   win.
5. **Write the ablation:** lesion the cache, $0.90 \to 0.72$ and $196 \to 171$,
   necessity verdict, then the under-change drill-down that measures the thesis.
6. **Write Limitations inside Results:** terse, each boundary routed to open work.
7. **Run both checklists in Part 4.** No naked/unpaired number, every number glued
   to its object; no method re-introduction, no survey.
---

**Semicolon rule (addendum).** A semicolon is earned only by a true antithesis or
tightly parallel pair; everything else takes a period. Budget about two per section.
After any editing pass, grep `;`: each survivor must name its antithesis or become a
period.
---

## Part 6: The insight layer (correct is not the same as worth reading)

The recipes above produce a correct Results section. This layer produces one a
reviewer quotes. Run it before drafting the findings paragraphs.
1. **Mine the artifacts with provenance.** Read the run logs, traces, and
   per-example outputs, not just the aggregate table. Keep a facts ledger:
   each candidate fact recorded with its source (file, field, computation), so
   any number in the section traces back to an artifact in one hop.
2. **Apply the quotability test.** For each candidate finding, ask: would a
   reviewer repeat this sentence to a colleague? "The system scored 0.90" fails;
   "the system solved the two mazes no baseline finished" passes. Facts that
   fail the test stay in the ledger.
3. **Escalate rate -> guarantee -> exhibit.** A rate is good ("92% of actions
   came from validated plans"). A guarantee is better ("every scored action
   passed the check, the harness enforces it"). An exhibit is best (the one
   trace, printed or pointed to, where the reader watches it happen). For each
   key claim, report the strongest of the three forms the data supports.
4. **Pick a story shape** for the section's arc, then arrange the claim
   subsections to serve it:
   - **Mystery:** open on the surprising number, spend the section explaining it.
   - **Objection-kill:** name the doubt a skeptical reviewer holds, then present
     the experiment that removes it.
   - **Pivot:** the expected story fails; the real story the data tells is
     more interesting, say so.
   - **Honest negative:** what did not work, stated plainly and early, with the
     boundary it draws.
   - **Artifact inspection:** read the system's own outputs closely and let the
     specimens carry the argument.
5. **Re-run the Part 4 checklists after the layer.** The insight layer adds
   claims; every added claim still needs its paired number and its provenance.
