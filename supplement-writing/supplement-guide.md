# How to Build a Supplement
### A plain-English guide. No jargon. Follow the steps.

*Distilled from forensic dissections of seven complete appendices by leading ML
researchers working on program synthesis and LLM agents, with measured page
fractions. Sibling of `../method-writing/method-guide.md` — same voice, same
recipe style — but for the paper's evidence locker: the supplement.*

---

## Part 0 — The terms you need, in plain words

| Fancy term | Plain meaning | Example |
|---|---|---|
| **Evidence locker** | What the supplement actually is: the room where a skeptic audits and a reimplementer rebuilds. Not a second results section. | The model appendix: ~75% verbatim artifacts, ~3% extra results. |
| **Artifact exhibit** | A verbatim, untouched object the system produced or consumed: a prompt, a learned program, a trace. | The complete learned program for one task, debug prints intact. |
| **Prompt gallery** | The full prompt set, printed last and longest, under one stated reading convention. | 22 pages, six prompts, one color legend. |
| **Reading convention / legend** | Three sentences up front that decode the formatting of every exhibit after them. | "Yellow = dynamic information, blue = main instruction." |
| **Functional gloss** | The one sentence before an exhibit saying what it is for. | "**Refining code.** It asks the LLM to refine code given the failed test." |
| **Pipeline chain** | Consecutive exhibits a reader can follow end to end: input -> prompt -> output. | Table 5 -> 6 -> 7/8 -> 9 in one dissected appendix. |
| **Trace / comic strip** | One learning trajectory walked qualitatively: screenshots beside code, colors carrying epistemic role, diffs highlighted. | An 8.5-page color-coded trace ending in the final program. |
| **Full-population gallery** | Show ALL of it, not a sample, so cherry-picking is off the table; say so in the caption. | All 160 tasks; "no example is dropped and no window is tuned." |
| **Curation disclosure** | Curated in the body, random/exhaustive in the supplement — each caption naming which. | "most interesting samples" (main) vs "drawn at random" (supplement). |
| **Failure specimens** | A NAMED section of verbatim failures tied to a main-text number. | "D. False Positive Solutions" tied to the main text's "about 9%". |
| **Proof choreography** | Intuition -> verbatim restatement of the main-text claim -> named outline -> proofs -> scope disclaimer -> adjacent measurement. | "Theorem 6 makes no guarantees as to cross-task systematicity..." |
| **Scope disclaimer** | The sentence after a proof stating what it does NOT buy, self-asked. | See above. |
| **Fairness sentence** | Per baseline, why the comparison is level. | "...so that the planner is the same for both the baseline and our method." |
| **Software map** | Concepts -> source files, figures -> generating scripts, runnable commands. | "Running `python driver.py demo`..." |
| **Payload-named pointer** | The inline main-text reference that says what the appendix section will give you. | "Appendix D shows example false positives." |
| **Third destination** | The website/repo that absorbs qualitative overflow, announced in the paper. | Gameplay videos; an interactive replay page. |

That is all the theory. Everything below is recipes and checklists.

---

## Part 1 — The big secret: the supplement is an evidence locker, filled with verbatim artifacts, ordered prose-first exhibits-last

A method section is N named parts. A results section is claim-headed
paragraphs. A supplement is simpler still: **it is the box of physical
evidence — prompts, learned code, traces, protocols, costs — arranged so
connective prose comes first and bulky verbatim exhibits close the document.**
Across the seven dissected appendices, artifacts average well over half the
pages; additional experiments average under 5%. Nobody dissected uses the
appendix to keep arguing.

Three structural rules govern it:

1. **Prose first, exhibits last.** Implementation details, protocol, baselines,
   compute — then the gallery: code listings, the trace, the prompts. The model
   appendix runs theory -> planner details -> extra results -> code -> 22 pages
   of prompts, in exactly that order.
2. **Verbatim means verbatim.** Stub `pass` bodies, debug prints, the model's
   own comments, ragged line wrapping — all kept. The credibility of the
   exhibit comes precisely from not tidying it. Curation, where it exists, is
   disclosed in the caption.
3. **Everything is wired.** Every supplement section is pointed at from the
   main text by an inline, payload-naming reference; every supplement section
   re-anchors to the main text in its first sentences. The dissections caught
   the failures: one appendix has zero inbound pointers; another's
   extra-results section is unreachable; a third's hyperparameter tables are
   orphaned. Do not strand a section.

The honesty devices are structural, not rhetorical: a NAMED failure section
with specimens, full-population galleries, curation disclosures, scope
disclaimers after proofs. Reviewers in this literature look for them by name.

---

## Part 2 — The three recipes

### Recipe A: The attached, artifact-heavy appendix (THE model)
*Use for: the appendix bound behind the references of an LLM-agent or
program-synthesis paper.*

What it does, in plain words:
- **Opens with the theory beat** (only because the main text carries a
  theorem): intuition stated as an Observation, definitions and theorem
  restated verbatim, named proof outline, lemma proofs — about two pages, 4% of
  the appendix.
- **Immediately follows with the qualitative trace** (8.5 pages): the
  color-coded screenshot-and-code comic strip of one full learning trajectory,
  failure annotations in the box titles, ending with the complete final
  program.
- **Then subroutine algorithms** with defaults in the box headers, **then a
  small extra-results section**, **then complete synthesized programs** (one
  short domain, one 5.5-page unretouched listing that cashes the main text's
  "250+ lines" claim), **then the prompt gallery last and longest** (22 pages,
  one legend, one gloss per prompt).
- **Continues main-text float numbering**; keeps the main algorithm in the main
  text and exiles only subroutines.

**Fill-in template:**
> **A [Theory beat, if the main text made a formal claim].** Observation
> (intuition) -> restated Defs/Theorem -> outline -> proofs -> scope
> disclaimer. **A.1 [Example learning trajectory on {domain}].** Screenshot |
> code, colors = epistemic role, diffs highlighted, "(what it figured out)
> (what is still wrong)". **B [Subroutine algorithms].** Boxes with
> `Hyperparam:` defaults. **C [Baseline reproduction].** Prose, every default
> stated. **D/E [Synthesized {artifact} for {domain}].** Complete,
> unretouched. **F [Prompts].** Legend once, then gloss + verbatim prompt,
> subsection per pipeline stage.

### Recipe B: The standalone supplement (self-sufficient document shape)
*Use for: a separate supplement PDF that must survive being read alone. It
borrows this shell even while filling it with Recipe-A contents.*

What it does, in plain words:
- **Opens with a roadmap sentence and a typeset Contents**: "We divide our
  supplementary materials into additional results (S1), ... experimental
  methods (S2), ... prior work (S3), and ... implementation (S4)."
- **S-prefixed float series and its own bibliography** — the supplement never
  borrows a number from the main text and never breaks if read alone.
- **Per-domain protocol sections on a rigid template** (count -> provenance ->
  split -> verbatim primitive list -> tricks -> deviations), the same beats
  repeated for every domain.
- **Theory choreographed in layers and paired with measurements**: every
  theorem gets an intuition sentence before it, a scope disclaimer after it,
  and an adjacent figure measuring the thing it proves.
- **Keeps full caption discipline in the supplement** — the only paper of the
  seven that does; legends, error-bar semantics, and exclusions live inside
  the captions.
- **Closes with a software map for reimplementers** (concepts -> files,
  figures -> scripts).

**Fill-in template:**
> "We divide this supplement into [results], [methods/protocol], [background],
> and [implementation]." -> Contents -> [galleries with stated sampling] ->
> [per-domain template x N] -> [expanded background, if the venue squeezed it]
> -> [derivations + algorithms + proofs, each with intuition before and
> disclaimer after, each paired with its measurement] -> [hyperparameter table
> + "informal coarse search" honesty] -> [software map] -> [own references].

### Recipe C: The honesty pack (the graft every supplement takes)
*Use for: the three devices the newest papers in this literature add on top of
either shell.*

- **The highlighted prompt diff:** when the paper's claim is a controlled
  comparison, print both prompts in full and highlight the only difference.
  The ablation becomes visually auditable.
- **The named failure section:** specimens of the system's OWN failures,
  verbatim, each dissected in a sentence, tied to the main-text rate, pointed
  at by a declarative main-text sentence.
- **The compute-and-fairness block:** one paragraph per baseline ending in a
  fairness sentence; a compute subsection with dollars, hours, hardware, and
  any caching trick disclosed. Most papers omit cost — including it beats them
  on their own terms.

---

## Part 3 — The devices recipe

### The prompt gallery
- **One legend, stated once, before the first exhibit** (three sentences
  maximum). Every exhibit after it obeys the legend.
- **One functional gloss per exhibit**, bold run-in, one sentence; the gloss
  may carry a real parameter ("seven uniformly randomly sampled examples").
- **Templates or transcripts — pick and disclose.** Unfilled slots
  (`{examples}`) show the machinery; one filled invocation with a real
  counterexample shows it running. Print the static preamble once in full; do
  not reprint shared bodies per variant (one dissected appendix wasted ~6
  pages on duplication).
- **Adjacent siblings for compared conditions**, delta highlighted.

### The trace (the single most imitable device)
- One task, start to finish. Alternate environment states and model code.
  Title bars carry `role (what it just figured out) (what is still wrong)`.
  One color code for epistemic role — data-consistent, imagined/goal-driven,
  milestone. Highlight changed lines so each repair reads as a diff. Close
  with the final complete program. All failure honesty for the happy path
  lives here.

### The learned-code exhibit
- **Complete, unretouched, captioned, numbered.** One task in full beats five
  excerpts. Keep the model's own docstrings and comments — they are the
  exhibit.
- **The diptych upgrade:** show the same behavior re-expressed WITHOUT the
  learned structure, with the cost stated ("32 function calls... 10^72 years
  of brute-force search"). The compression is the point.

### The theory beat
- Intuition Observation -> definitions/claim restated verbatim from the main
  text (self-containment) -> named outline -> proofs cheapest-first -> scope
  disclaimer -> pointer to the adjacent measurement. One page is enough when
  the paper carries one proposition.

### The protocol/fairness/compute block
- Template once + per-domain exceptions, not N repetitions. One
  provenance-and-fairness paragraph per comparison row. Compute in its own
  subsection: tokens, cost, hours, hardware. Sensitivity checks stated with
  their deltas.

### The wiring
- Main text -> supplement: inline, parenthetical, payload-named, at the end of
  the claim sentence. Captions may hand off to their bigger supplement selves
  ("Fig. S5 shows 150 random samples at each stage.").
- Supplement -> main: re-anchor in the first two sentences of every section
  ("The main paper's Algorithm 1 states the system in twenty-eight lines...").
- **No strays:** every section referenced at least once from outside itself;
  every float referenced from prose.

---

## Part 4 — The mechanical checklists

### Supplement checklist
- [ ] Roadmap paragraph names the parts in order (standalone doc: plus a
      Contents).
- [ ] Prose sections first; verbatim exhibits last.
- [ ] Every exhibit verbatim; every curation disclosed in its caption.
- [ ] Prompt gallery: legend stated once; gloss per exhibit; compared prompts
      adjacent with delta highlighted.
- [ ] One pipeline chain traceable across consecutive exhibits.
- [ ] One qualitative trace with epistemic color-coding and failure
      annotations.
- [ ] At least one artifact shown COMPLETELY (one full learned program).
- [ ] Named failure section with specimens, tied to a main-text number.
- [ ] Theory beat choreographed (intuition / verbatim restatement / outline /
      proofs / scope disclaimer) and paired with its measurement.
- [ ] Protocol template + exceptions; fairness sentence per baseline; compute
      subsection.
- [ ] Software map: concepts -> files, figures -> scripts, runnable commands.
- [ ] Every supplement section pointed at from the main paper by a
      payload-naming reference; no orphaned sections or floats.
- [ ] Captions at full house discipline (name-decode-claim) — the
      caption-collapse most appendices allow is NOT imitated here.
- [ ] Prose axioms hold: sentences <= ~28 words, zero can/could, no bare
      This/These, numbers glued to objects.

### Prohibitions checklist (search-and-delete)
- [ ] Search for new cross-system comparisons or claims not in the main
      paper -> the supplement audits existing claims; it does not open new
      fronts.
- [ ] Search for tidied/prettified exhibit code -> restore verbatim or
      disclose the abridgment in the caption.
- [ ] Search `\ref{sec:` in supplement files -> under document classes with
      `secnumdepth=0` these render EMPTY. Refer to appendix sections by NAME,
      never by `\ref`. (Figure/table/listing refs are fine.)
- [ ] Search notation splits -> one convention per object paper-wide; unify
      to the main paper's forms and flag the choice.
- [ ] Search "can" / "could" in new prose -> zero. Search bare "This " /
      "These " -> each gets a noun.
- [ ] Numbers discipline: every headline number pairs with its partner; two
      distinct rates are never rounded or merged into one.

### What NEVER goes in the supplement
- New headline claims or rankings absent from the main paper.
- A limitations essay — specimens and scoping clauses only; limitations prose
  lives in the main paper.
- Retouched artifacts presented as verbatim.
- A literature survey beyond what the venue squeezed out of the main paper.

---

## Part 5 — The assembly line (do this, in order)

1. **Inventory the material against the recipe slots:** roadmap, protocol,
   theory beat, galleries, learned-artifact exhibit, trace, failure section,
   prompt gallery, software map. Mark what exists, what is orphaned, what is
   missing.
2. **Re-couple anything decoupled** (sections living in side files) into the
   compiled document, then fix the landmines: section-name references instead
   of `\ref{sec:}`, one notation convention, consistent vocabulary.
3. **Write the roadmap paragraph** naming the parts in order.
4. **Add the prompt gallery** (main prompt in full + any compared variant as a
   highlighted diff).
5. **Compose the trace** for one task from run artifacts, color-coded,
   failure-annotated.
6. **Write the failure section** — verbatim specimens tied to the main-text
   rate.
7. **Upgrade the learned-artifact exhibit** to one complete listing; add the
   pipeline chain (input -> prompt -> output -> validation).
8. **Add the software map** (one page).
9. **Wire everything:** payload-named pointers from the main paper, re-anchors
   in each section, no orphans; captions to house discipline.
10. **Run the Part 4 checklists**, then the full build-and-render chain, and
    verify the layout on the rendered pages.
