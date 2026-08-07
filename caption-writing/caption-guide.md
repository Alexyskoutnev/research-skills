# How to Write a Caption
### A plain-English guide. No jargon. Follow the steps.
*Distilled from forensic dissections of fifteen papers by three leading ML
researchers, the classic writing guides (Kording & Mensh on figures above all),
and the canonical ML papers. Sibling of `method-writing/` and `results-writing/`: same voice, same recipe style, but for the text under the exhibit: the
caption.*

Throughout, one invented toy system carries the examples: **PlanCache**, which
routes a courier over a city road graph by searching for a path and reusing
previously solved subroutes. Its three parts are the **router** (searches the
graph), the **subplan cache** (stores solved subroutes keyed by their
endpoints), and the **replay checker** (re-verifies a cached subroute still
holds before it is committed). It is evaluated on **200 courier queries**: 60
carrying a scheduled road closure (the edited-map subset), 140 static, against
a composite **route score** (optimality x search-efficiency, 1 is best), with
three named rivals: **PlainSearch** (the cache-off ablation, identical router),
**GreedyReuse** (reuses cached subroutes without re-checking), and the
shortest-path **oracle** (upper bound). Nothing about PlanCache is real; it
exists only to fill the templates with something concrete.
Its six captioned exhibits, referenced below:
- **Figure 1**: the PlanCache loop diagram (the method figure; flagship, the
  fullest caption).
- **Algorithm 1**: the planning-loop control flow.
- **Table 1**: aggregate route scores across all systems (flagship).
- **Table 2**: the per-query breakdown (workhorse).
- **Figure 2**: the route-score map, sorted by PlanCache score (flagship).
- **Figure 3**: the search-efficiency bars (flagship).
---

## Part 0: The one thing to understand first

A caption is read by someone who **never reads the paper**. They flip to the
figure, read the caption, and move on. So the caption has one job: **make that
person get the finding from the figure alone.** This is why captions repeat
things the body already says, that is not a mistake, it is the whole point. Say
it again under the figure. **Self-containment beats deduplication.**

Two kinds of exhibit, two kinds of caption:
- **A flagship** (your headline table or chart) -> it **claims**. The last
  sentence is a verdict with a number.
- **A workhorse** (a per-item table, a diagram) -> it only **describes**. No
  verdict; just say what it is and how to read it.
Rank the exhibit before you write a word. Length follows the role, not the
Figure/Table label: the method figure (Figure 1) earns the fullest caption; the
aggregate scoreboard (Table 1) earns a three-sentence label.
---

## Part 1: The terms you need, in plain words

The dissections use special words for the parts of a caption. Here is what they
actually mean. You never have to say these words; you just have to do them.
| Fancy term | Plain meaning | Example |
|---|---|---|
| **Verbless opener** | The first phrase names what the reader is looking at, no verb, then a period. | "The PlanCache planning loop." |
| **Reading key / decoder** | The inline note telling you what a color, line, bar, panel, symbol, or abbreviation means. | "brighter is higher"; "exp = node expansions" |
| **Flagship exhibit** | The headline table or chart that carries the argument; its caption claims. | the aggregate route-score table |
| **Workhorse exhibit** | A per-item table or diagram; its caption only describes. | the per-query breakdown |
| **Self-containment** | The caption restates the body so a skimmer who never reads the text still gets the finding. | restating the three means under the score map |
| **Verdict / takeaway** | The closing claim of a flagship caption, carrying one or two paired numbers. | "PlanCache scores 0.90 versus 0.72" |
| **Scale direction** | Stating which way an ordinal axis runs so it is not read upside down. | "lower is faster"; "1 is best" |
| **Paired number** | A number with a partner, glued to its object. | "0.90 versus 0.72"; "48 of 60" |
| **Provenance pointer** | A terse cross-reference, never a sentence of its own. | "Per-leg counts in the supplement." |

That is all the theory. Everything below is recipes and checklists.
---

## Part 2: The recipe (name -> decode -> land)

Every strong caption is three moves in this order:
1. **Name the object.** A label with no verb, then a period. Not "This figure
   shows the loop." Just "**The PlanCache loop.**"
2. **Decode the reading key.** Tell the reader what every color, bar, line,
   panel, and abbreviation means. Anything on the picture that is not obvious
   gets one short "label: meaning" note. Expand every abbreviation on first use,
   and state the scale direction of any ordinal axis that could flip.
3. **Land the takeaway** (flagships only). The last sentence is the verdict,
   carrying one or two numbers. Skip this move for workhorse exhibits.
That is the whole trick. Name it, decode it, land it. The claim is always the
closer, never the opener. Kording & Mensh: the title states the conclusion, the
legend explains how it was done.
---

## Part 3: The fill-in template

> **[Object name].** [One sentence: what it is, what data, what method, restate
> from the body freely.] [Decode each mark: color X means…, dashed line is…,
> brighter is higher, exp = …, ZS = zero-shot.] [Flagship only: the verdict,
> with paired numbers.] [Terse pointer: See supplement.]

Filled in for Figure 2 (the score map):
> **Per-query route score (0–1) for PlanCache, GreedyReuse, and PlainSearch,
> sorted by PlanCache score.** Each cell is one query's route score, the product
> of optimality and search-efficiency, where brighter is higher. Averaged over
> all 200 queries PlanCache scores 0.90, GreedyReuse 0.78, and PlainSearch 0.72,
> under the shortest-path oracle's 1.00.
Name (verbless clause + period) -> decode ("brighter is higher", the formula) ->
land ("PlanCache scores 0.90…"). Three moves, done.
---

## Part 4: The checklist (run on every caption)

**Structure**
- [ ] Opens with a verbless noun phrase + period. No "This figure shows…"
- [ ] Order is name -> decode -> takeaway.
- [ ] Flagship claims (verdict last); workhorse only describes.
**Reading key**
- [ ] Every color, line style, bar direction, panel, and bold cell is decoded.
- [ ] Every abbreviation is expanded on first use (exp, opt, ZS, CoT).
- [ ] Scale direction stated if it could be misread ("lower is faster",
  "brighter is higher").
**Numbers**
- [ ] Only the one or two headline numbers appear; the full row stays in the
  cells.
- [ ] Every number is paired (ours/theirs, from/to, n/N) and glued to its exact
  object.
- [ ] No two distinct rates are rounded together into one figure; each stays
  pinned to what it measures.
**Prose**
- [ ] Present tense, active voice, named agent ("the router searches…", not "is
  searched").
- [ ] Every sentence <= ~28 words. Zero "can" / "could" / "appears to". No em
  dash.
- [ ] Provenance is a short pointer, not a sentence ("Per-leg counts in the
  supplement.").
**Prohibitions**
- [ ] No hyperparameters, no p-values, no equation-to-solve (a formula may name
  a quantity, not invite a derivation).
- [ ] No undefined mark, if it is on the canvas, the caption keys it.
- [ ] No related-work argument and no future work. Name a rival only as a
  compared system.
---

## Part 5: Worked examples

### A) A flagship figure (it claims)

Figure 3, the search-efficiency bars.
**Bad draft** (opens with the verb, front-loads the verdict, over-claims,
decodes nothing):
> This figure shows that PlanCache is more efficient than the other planners
> because it expands fewer nodes, which proves the cache works.
Fails: opens with "This figure shows"; the verdict is the opener, not the
closer; "proves" over-claims; no axis or scale direction decoded; the numbers
are missing and unpaired.
**Good draft** (name -> decode -> land):
> **Node expansions per query for PlanCache and PlainSearch on the 171 shared
> solves.** Each bar is a query's expansion count and lower is faster; the
> dashed line is the oracle's search-optimal count. PlanCache expands fewer
> nodes on 168 of 171 shared queries, 1,180 against PlainSearch's 3,940 in
> total.
Why it works: verbless name + period; the two marks decoded (lower is faster,
dashed line = oracle); the verdict last, carrying two paired numbers each glued
to its object (168 of 171 queries; 1,180 against 3,940).
### B) A workhorse table (it describes, no verdict)

Table 2, the per-query breakdown.
**Bad draft** (describes nothing you cannot see, hides the agent,
over-explains):
> This table shows how each planner did on all the queries, and you can see that
> PlanCache could beat the others on most of them, which is a strong result.
Fails: opens with "This table shows"; has a hedge ("could"); makes a verdict on
a workhorse; decodes no column; has no paired numbers; not glued to objects.
**Good draft** (name -> decode -> pointer, no verdict):
> **Per-query results on all 200 courier queries.** exp = node expansions; opt =
> optimal legs / total legs; score = route score, with every planner evaluated
> against the same shortest-path oracle. PlanCache's under-change queries shown
> as-is (48 of 60 kept optimal); **bold** query IDs and PlanCache scores mark
> strict wins over every other evaluated planner. Per-leg counts in the
> supplement.
Why it works: verbless name + period; every column decoded (exp, opt, score);
the caveats that live nowhere else (48 of 60 kept optimal, and what bold marks);
a terse pointer to the supplement; and, correctly, **no verdict**, because the
breadth table is a workhorse. The claim lives under the flagship exhibits.
### C) An algorithm caption (it describes; fuller, self-contained)

Algorithm 1, the planning-loop control flow.
**Bad draft** (opens with the verb, re-tells nothing, editorializes, decodes no
subroutine):
> Algorithm 1 shows the PlanCache algorithm, which is our main contribution and
> works very well.
Fails: opens with "Algorithm 1 shows"; does not re-tell the procedure so the box
does not stand alone; editorializes ("works very well") on a method exhibit;
leaves the SMALL-CAPS subroutines undefined.
**Good draft** (name -> re-tell the procedure -> decode the subroutines and
line-key):
> **The PlanCache planning loop.** For each courier query the router searches
> the road graph for a path, drawing any subroute the subplan cache holds for
> the query's endpoints; the replay checker re-verifies each reused subroute
> against the current map before it is committed, and a failed check returns
> that leg to the router. SEARCH, REUSE, and CHECK name the three subroutines of
> Section 3; line numbers cross-reference it.
Why it works: verbless name + period; it re-tells the whole procedure so the box
stands alone; present-tense, named-agent voice (the router searches, the checker
re-verifies); the SMALL-CAPS subroutines and the line-number key decoded; and no
verdict, because an algorithm box describes a mechanism, not a result. It earns
the fuller paragraph because it carries the method.
---

## Part 6: The five judgment calls (where the dissected authors diverge)

The three authors agree on almost everything above. Where two of them would
write it differently, here is the call to make:
1. **Claim or describe?** Flagship -> claim. Workhorse -> describe. Rank the
   exhibit first. (One author claims on every results caption; one holds the
   verdict for the body; one splits by rank, the split-by-rank call wins,
   because self-containment beats deduplication.)
2. **How long?** Conference register: one setup sentence + decode + one verdict.
   Only the method figure gets the fuller paragraph. Never the journal-length
   re-teach of the whole method.
3. **Voice?** Named agent, active, present ("the router searches the graph").
   Not passive ("the graph is searched"), not first-person "we apply".
4. **Colon or period after the name?** Period, then a new sentence. Save the
   colon for a column glossary (exp:, opt:) where it earns the term-then-gloss
   pattern.
5. **Bold inside the caption?** None, if your caption package forbids it, carry
   emphasis in plain words ("brighter is higher") and let bold live in the
   table cells the caption refers to, not in the caption prose.
---

## Part 7: The assembly line (do this, in order)

1. **Name the object**: verbless phrase, period.
2. **Decide the rank**: flagship (claims) or workhorse (describes).
3. **Write the setup sentence**: what it is, what data, what method; restate
   from the body without apology.
4. **Decode every mark**: colors, lines, bars, panels, abbreviations, scale
   direction; one "label: meaning" fragment per channel.
5. **Land the takeaway** (flagship only), one or two paired numbers, verdict
   last, each number glued to its object.
6. **Add the pointer**: "See supplement" and nothing more.
7. **Run the Part 4 checklist**, then check claim direction against the data:
   if "lower is faster," the winner holds the lower number.
---

**Semicolon rule (addendum).** A semicolon is earned only by a true antithesis
or a tightly parallel pair whose halves must be read as one thought; everything
else takes a period. Captions are especially prone to the "clause; clause" chain
because they stack decoders, but a decoder stack is a list, and lists take
periods or the "label: meaning" fragment, not semicolons. Budget about one or
two per caption. After any editing pass, grep `;`: each survivor must name its
antithesis or become a period.
---

## Part 8: Figure-text exactness (the figure, its caption, and its table are one exhibit)

A figure, its caption, and the table it corresponds to form ONE exhibit. Audit
them together, never sentence by sentence in isolation. These rules were earned
the hard way, caption patches kept failing until the exhibit was treated as a
unit.
1. **One vocabulary per exhibit.** Figure-internal labels (legends, bar names,
   colorbars) use the caption's terms, and when the caption says "the values
   correspond to Table N," the labels match Table N's row names word for word.
   A mismatched vocabulary ("untaken actions" in the legend, "unobserved pairs"
   in the caption) means regenerating the figure, not wording the caption
   around it.
2. **Legend entries are parallel.** Every entry fills the same slots. "at
   evaluation time, items scored" (a time) beside "final model, items never
   scored" (a thing) is a defect; "model during training, ..." / "final
   model, ..." is the fix.
3. **State the shared comparison once, up top.** When one comparison underlies
   every mark ("every point compares the prediction with the ground truth"),
   say it first; each mark type then carries only its differences (which
   subset, which model stage), decoded with ONE shared verb phrase. Defining
   each mark from scratch re-derives the machinery differently each time.
4. **Anchor every inference to the datum that proves it.** Before attaching a
   lesson clause ("high fit does not guarantee generalization"), check the
   chart: the nearest-named example must be the one that proves the lesson,
   never the counterexample where both quantities happen to agree.
5. **Explain visible anomalies where the eye lands.** If the author pauses on a
   mark pattern (a filled circle sitting right of its open circle), a
   first-time reader stops dead. The caption explains the pattern in plain
   terms at that exact spot ("the open circle averages the whole run, early
   mistakes included; the filled circle tests only the final model").
   Author-stumbles predict reader-stumbles, always.
6. **Timing and coverage in plain words.** "One prediction before every action"
   replaces modifier stacks like "precommitted evaluation-time predictions on
   pairs observed during the run."
7. **Check figure claims against the run data, not memory.** Per-item numbers
   live in the experiment's result files; pull them before asserting or fixing
   any figure-adjacent number. Never silently change a printed number,
   verify against ground truth, then flag the change to the author.
