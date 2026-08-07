# How to Write a Conclusion
### A plain-English guide. No jargon. Follow the steps.
*Distilled from forensic dissections of fifteen papers by three leading ML
researchers, the classic writing guides, and the canonical ML papers. Sibling of
`method-writing/` and `results-writing/`: same voice, same recipe style, but for
the paper's landing: the Conclusion.*

Throughout, the same invented toy system carries the examples: **PlanCache**, which
routes a courier over a road graph by searching for a path and reusing previously
solved subroutes, through a **router**, a **subplan cache**, and a **replay
checker** that re-verifies a cached subroute before it is committed. Its results
world (invented, and reused from `results-writing/`): $200$ courier queries, a
composite **route score** (optimality × search-efficiency, $1$ best), rivals
PlainSearch (cache removed) and GreedyReuse (reuses without checking), and the
finding that reuse serves $64\%$ of legs cheaply while staying optimal under a map
change holds on only $48$ of $60$ edited-map queries. Nothing about PlanCache is
real; it exists only to fill the templates with something concrete.
The thesis the close must land is fixed: **reuse and validity are the easy half;
staying shortest as the map changes is the hard half, and we measured it.** So the
recap-claim must carry the under-change number ($48/60$), and the vista must name
optimality-under-change as the frontier the paper opens.
---

## Part 0: The terms you need, in plain words

Reviewers and writing coaches use special words for the parts of a closing
section. Here is what they actually mean. You never have to say these words; you
just have to do them.
| Fancy term | Plain meaning | Example |
|---|---|---|
| **Thesis restatement** | The first sentence: re-name the system and compress its claim to one line. | "PlanCache treats routing as searching once, reusing checked subroutes, and re-verifying each before commit." |
| **Recap, not report** | Name what you did once; never re-list the results table or re-walk the pipeline. | "searches, reuses checked subroutes, re-verifies each", not the per-query scores. |
| **Make the promise concrete** | The intro's claim cashes out here as the measured number. | The intro promises "we measured the hard half"; the close says "$48$ of $60$." |
| **Speculation quarantine** | New ideas are allowed only here, and only flagged as conjecture. | "a global reroute proposer for heavy closures remains a target for future work." |
| **Hermetic to new evidence** | No new number, table, or figure crosses into the conclusion. | $0.90$, $0.72$, $64\%$ are reprised, never introduced. |
| **Assumption-plus-remedy** | Every limitation is a named assumption welded to its fix. | "replay checking assumes closures are observed, addressable by a stochastic map model." |
| **Feature-not-a-bug** | Flip a structural limit into the paradigm's virtue, or the paper's thesis. | Optimality-under-change being the hard half is not a weakness; it is what we set out to measure. |
| **Welded scope clause** | One flat limitation sentence inside the recap; the full ledger stays upstream. | "checked reuse does not by itself keep a route shortest under a closure." |
| **The vista / zoom-out** | The last sentence widens from the artifact to the field, an insight, not a summary. | "checked, executable subplans let a planner reuse, re-verify, and re-plan as the world changes." |
| **Credit-then-contrast** | Praise a neighbor fully, then differ on one axis. Never call it wrong. | GreedyReuse's speed is credited, then the checking delta is stated. |

That is all the theory. Everything below is recipes and checklists.
---

## Part 1: The big secret: a conclusion is two moves, and it is short

An introduction is a funnel that answers seven questions. A method section is N
named parts assembled in order. **A conclusion is simpler and shorter than either:
it is two moves in one-to-three paragraphs.** The cleanest fingerprint is exactly
this, recap-claim, then zoom-out-with-future-work.
- **Move 1. Recap-claim.** Re-name the system in one past-tense sentence, then
  make the intro's promise concrete by reprising the one or two load-bearing
  numbers. Recap the mechanism; do not re-report the experiments.
- **Move 2. Zoom-out.** Weld in one flat limitation clause (the full ledger lives
  in an earlier Limitations subsection), then close on a vista that widens from the
  artifact to the field.
Three rules govern the whole thing:
1. **It is a landing, not a second results section.** Peyton Jones budgets half a
   page; Widom: under no circumstances should the paragraph simply repeat material
   from the Abstract or Introduction. One to three dense paragraphs of prose, never
   a bulleted future-work list.
2. **It mirrors the introduction.** Kording & Mensh: the discussion brings the
   conclusion, the intro runs broad→narrow to a gap; the conclusion opens at the
   now-filled gap and widens to significance. It is the intro run backwards.
3. **New evidence never enters; new speculation may.** No new number, table, or
   figure (all authors agree). The only fresh content allowed is flagged conjecture
   or one conceptual argument.
For PlanCache the thesis the close must land is fixed: **reuse and validity are the
easy half, staying shortest under change is the hard half, and we measured it.** So
the recap-claim must carry the under-change number ($48/60$), and the vista must
name optimality-under-change as the frontier the paper opens.
---

## Part 2: The three recipes

Pick the one that fits your section layout, and match the one your closest rival
uses, a native register reads as native to the reviewer who wrote it.
### Recipe A: Limitations-as-doorways, close on a horizon
*Use when: the closing section is doing double duty as the limitations discussion,
and your closest rival writes this way.*

What the recipe does, in plain words:
- **Names the section for its function**: `Limitations and Open Directions`, not
  "Conclusion."
- **Opens with one past-tense thesis sentence** re-naming the system ("We have
  presented…", "We contribute an algorithm, X, that…").
- **Makes each limitation an assumption welded to a remedy**, with a citation to the
  tool that would fix it ("we assume closures are observed, addressable by
  synthesizing a stochastic map model … nontrivial but surmountable").
- **Flips a structural limit into a virtue** ("this restriction is a feature, not a
  bug") or states an **honest tradeoff ledger** ("free unlimited re-checking and
  offline reuse, bought with a discrete, indexed road graph").
- **Quarantines the one unbuilt idea** here, flagged as "a prime target for future
  work."
- **Closes on a horizon**: a scaling path from the artifact to the field.
**Fill-in template:**
> We have presented [System], which [one-line mechanism]. Our approach delivers
> [gain], but at [cost: the structural assumption]. This assumption, [name it],
> could be addressed by [remedy + citation]; [it is] nontrivial but surmountable.
> More broadly, [the unbuilt extension] remains a prime target for future work,
> toward [field-scale horizon].
### Recipe B: The terse envoi: recap + welded clause + impact
*Use when: you already have a separate Limitations subsection and you want a clean,
short final paragraph. This is the natural voice for an agent or pipeline paper.*

What the recipe does, in plain words:
- **Keeps a numbered `Conclusion` of one tight paragraph**, two-to-five sentences,
  after a Results-with-Limitations.
- **Opens with a title-echoing recap verb** framing the headline as an achieved
  capability ("This work shows … tackles [the task]"; "Our work is the first to …").
- **Welds one flat scope clause into the recap** ("In contrast, without the
  checker …"; "A limitation of our work is …"), no apology, no new evidence.
- **Closes on impact**, enumerating deployment paths (i)/(ii)/(iii) when there is
  more than one.
- **Keeps task-level future work upstream** in the Limitations subsection, not in
  the Conclusion.
- **In ethics-gated venues, adds a separate Impact Statement**: two sentences of
  responsible deployment.
**Fill-in template:**
> This work shows that [System] [achieved capability, framed at human or
> first-of-its-kind level]. In contrast, [the weaker regime of your own method or
> the baseline] [flat one-clause bound]. Our results open the door to [impact],
> toward [(i) …, (ii) …, (iii) …].
### Recipe C: The two-move close: recap-claim, then zoom-out
*Use when: you want the cleanest textbook shape, one paragraph that says what the
artifact is, then one paragraph that widens to the field with a concrete
future-work list.*

What the recipe does, in plain words:
- **Titles it `SUMMARY` or `DISCUSSION`**, or tucks a bold "Conclusion." run-in at
  the end of the last real section.
- **Paragraph 1 is recap-claim:** re-names the system and its mechanism, re-asserts
  the single headline delta, and often re-quotes the intro's driving question
  verbatim.
- **Paragraph 2 is zoom-out:** a hinge sentence ("This work demonstrates the
  promise … However, there is much more left to do.") turns to a concrete,
  difficulty-graded future-work list, then ends on one aspirational sentence ("we
  look forward to a world in which …").
- **Keeps the tone measured**: "suggests," "we look forward to," never a
  declaration of revolution; no em-dashes-as-drama, no hype adjectives.
- **Puts any new or forward material in a preceding Discussion**, never in the
  one-line conclusion proper.
**Fill-in template:**
> [System] is a [one-line what-it-is] that [mechanism]. It [headline result, the
> delta]. This work demonstrates the promise of [approach]. However, there is much
> more left to do: [difficulty-graded list]. We look forward to [aspirational
> field-scale sentence].
---

## Part 3: The mechanical checklists

Run these on the finished draft. Each box is a search-and-fix, not an opinion.
### Conclusion checklist
- [ ] The opener is **one past-tense sentence re-naming the system** and its
  mechanism.
- [ ] It **opens at the now-filled gap** and widens to significance (mirrors the
  intro).
- [ ] It **recaps the mechanism once**; it does **not** re-walk the pipeline or
  re-list the results table.
- [ ] The intro's promise is **made concrete**: the load-bearing numbers are
  reprised (not introduced).
- [ ] It is **one to three paragraphs of prose**, no bulleted future-work list.
- [ ] Each limitation is a **named assumption welded to a remedy or a path**: no
  naked, no apologetic.
- [ ] Any structural limit is **flipped** (feature-not-a-bug or a tradeoff ledger).
- [ ] The full limitations ledger stays in the **`\subsection{Limitations}`**; the
  close carries **one flat scope clause**.
- [ ] Future work is **payload**: the concrete direction the paper opens, not
  "exciting possibilities."
- [ ] The last sentence is a **vista**: a transferable insight, measured and
  refutable, not a summary.
- [ ] Prose axioms hold: sentences ≤ ~28 words, subject+verb early, **zero
  "can"/"could"**, no bare "This"/"These", no em dashes, numbers paired and
  attached to exact objects.
### Prohibitions checklist (search-and-delete)
- [ ] Search for a **new number / table / figure** → none. Every number in the
  close is reprised from Experiments.
- [ ] Search for a **re-statement of the abstract or intro** → paraphrase and make
  concrete, never repeat.
- [ ] Search for a **bulleted or vague future-work list** ("we will explore various
  directions") → replace with the one named frontier or a difficulty-graded list.
- [ ] Search for **hype / grandiosity** ("opens exciting possibilities,"
  "revolutionary") → replace with a concrete, refutable claim.
- [ ] Search "can" / "could" → **zero hits.** Search bare "This " / "These " → each
  has a noun. Search em dashes → none.
- [ ] Numbers never conflated, each rate is pinned to the object it measures, and
  no two measurements are rounded together into one figure.
- [ ] Coined names are used consistently; rivals **credited then contrasted**, never
  bashed.
### What NEVER goes in the conclusion
- A new experimental number, table, or figure, all evidence was earned in
  Experiments.
- A verbatim restatement of the abstract or introduction (Widom's "under no
  circumstances").
- A bulleted re-listing of results or a re-walk of the method pipeline.
- A re-opened limitations ledger, one welded clause is the ceiling; the full list
  is a prior subsection.
- Vague grandiosity with no concrete direction, or hype adjectives, or
  em-dashes-as-drama.
- Rival-bashing, neighbors are credited, then contrasted on one axis.
---

## Part 4: A worked example: the toy planner on the recipe

Here is a PlanCache conclusion mapped paragraph by paragraph, the shape a finished
close takes. It runs **Recipe B** (a terse numbered `Conclusion` after a
Results-with-Limitations) with the **horizon vista** as the close.
**Paragraph 1, thesis restatement + filled-gap opener.** "PlanCache treats
routing as searching once, reusing checked subroutes, and re-verifying each before
commit." This re-names the system and states its one mechanism, and it opens at the
now-filled gap (the intro's gap was that a planner re-solves subproblems it has
already solved; PlanCache reuses checked subroutes so each scored search becomes
reuse, a caught staleness, or a fresh leg). Clean recap-not-report: the mechanism
is named, the pipeline is not re-walked.
**Paragraph 2, make the promise concrete.** Reprise the two load-bearing numbers
that prove the thesis, reuse serves $64\%$ of legs (the easy half) and PlanCache
stays optimal on $48$ of $60$ edited-map queries (the hard half), plus the cache
delta $0.90$ vs $0.72$ that shows the gain is the method, not the router. All
numbers are reprised, none new. Optionally credit-then-contrast GreedyReuse's
static-suite speed, only if it already appears in Experiments.
**Paragraph 3, welded scope clause + flip + vista.** One welded clause pointing to
the Limitations subsection, not re-opening it: "checked reuse does not by itself
keep a route shortest under a heavy closure." Then flip it, that shortfall is not a
weakness but the hard half PlanCache was built to expose. Close on the vista, naming
the frontier the paper opens (a global reroute proposer that learns which closures
demand a full re-plan) and landing the transferable insight: "checked, executable
subplans let a planner reuse, re-verify, and re-plan as the world changes, tying
stored computation to fresh evidence."

### The number discipline (do not get this wrong)
| Number | What it is attached to | Never say |
|---|---|---|
| **$0.72$ vs $0.90$** | ablation: same router **without vs. with the cache** | $0.90$ alone, unpaired |
| **$64\%$** | reuse rate, legs served from cache (the easy half) | never the under-change number |
| **$48/60$** | edited-map queries kept **optimal** under change (the hard half) | never merge with the reuse rate |
| **GreedyReuse's speed** | published rival, credited then contrasted | present as a fresh comparison the results never ran |

### The assembly line (do this, in order)
1. **Fix the heading and register**: a terse numbered `Conclusion` envoi, or rename
   to `Discussion` for a limitations-led close. Decide before drafting.
2. **Write the one-sentence thesis restatement**: past tense, re-naming the system
   and its one mechanism.
3. **Open at the filled gap and widen**: each scored search becomes reuse, a caught
   staleness, or a fresh leg; then pivot to the thesis that staying shortest under
   change is the hard half.
4. **Make the promise concrete**: reprise the two load-bearing numbers ($64\%$
   reuse, $48/60$ under change) and the cache delta ($0.90$ vs $0.72$); recap the
   mechanism, do not re-report the tables.
5. **Weld the single flat scope clause**: "checked reuse does not by itself keep a
   route shortest under a closure," with the full ledger left in the Limitations
   subsection.
6. **Reframe the structural limit** and, if any new idea enters, quarantine it as
   flagged conjecture, the under-change frontier the paper opens, named as a
   direction, not a result.
7. **Close on the vista**: the transferable insight, measured and refutable,
   numbers pinned to objects, no new evidence crossing the boundary.
---

**Semicolon rule (addendum).** A semicolon is earned only by a true antithesis or
tightly parallel pair; everything else takes a period. Budget about two per section.
After any editing pass, grep `;`: each survivor must name its antithesis or become a
period.
