---
name: rebuttal-writing
description: Plan and write an academic rebuttal in two stages. Stage 1 triages the reviews, splits them into atomic concerns, diagnoses the doubt behind each, rates severity and decision impact, and produces a prioritized P0-P3 experiment plan. Stage 2 drafts the rebuttal from completed results using Direct Answer -> Evidence -> Revision. Use when reviews arrive, when deciding whether a rebuttal is worth the author's time, when ranking rebuttal experiments, or when drafting or quality-checking the response. Encodes the moves present in nine public OpenReview threads where a reviewer raised a score, and a short-form recipe for per-review forms with character limits. Never fabricates results, reviewer intent, or manuscript locations.
---

# Rebuttal writing (two-stage method)

A rebuttal period is short. The job is not to answer every reviewer sentence
equally; it is to identify the few doubts that decide acceptance and resolve
those with evidence. So the skill runs in two stages: triage first, drafting
only after results exist. When the author supplies only reviews, scores, and
an abstract, produce the triage and plan, never the finished rebuttal.

## Stage 0: Is a rebuttal worth writing?

Before planning any experiment, decide whether the rebuttal or a resubmission
is the better use of the remaining time.
- **Normalize the score scale first.** Venues differ: find the range, the
  meaning of each score, the approximate accept boundary, and whether
  reviewers may change scores or see new experiments. If the boundary is
  unknown, say the assessment is provisional.
- **Read the live response form, not the call for papers.** Record: one
  response per review or one per paper; the limit, in characters or words;
  whether Markdown, LaTeX, tables, links, or uploads are allowed; who reads each
  response; whether it stays editable until the deadline; the deadline with
  its time zone; and whether a confidential channel to the chair exists. Where
  the form forbids links, "see our repository" is a violation, not an answer;
  a per-review character limit fixes the shape of every answer before any
  experiment is chosen.
- **Classify the situation:**
  - **Promising**: at least one advocate above the boundary, the negatives
    rest on fixable misunderstandings or missing evidence, and no reviewer
    has found a correctness flaw. Invest in targeted experiments and a full
    response.
  - **Uncertain**: scores cluster at the boundary and one decisive
    experiment or clarification could tip it. Run only fast, high-value work;
    draft a concise response; log resubmission revisions in parallel.
  - **Low expected return**: every score sits below the boundary, no
    advocate exists, or several reviewers independently reject the premise.
    Say plainly that heavy rebuttal work is unlikely to change the outcome;
    offer a short factual-corrections response plus a full resubmission plan.
    Never declare rejection certain, keep the language calibrated.
- A low-return verdict still produces output: what is worth answering now,
  what to skip, why the paper lost, and a ranked revision roadmap for the
  next venue.
## Stage 1: Triage the reviews

1. **Split every review into atomic concerns.** One reviewer paragraph often
   bundles three complaints (cost, fairness, novelty); give each its own ID
   (C1, C2, ...) so evidence maps one-to-one.
2. **Diagnose the doubt behind the words.** For each concern, separate the
   surface text from the underlying decision-relevant question ("is the gain
   an artifact of unmatched compute?", "does this generalize past the
   benchmark?", "is the paper unclear rather than wrong?"). Name the evidence
   that would settle it. This diagnosis step is mandatory.
3. **Flag uncertain intent instead of guessing.** When a comment supports two
   readings, show the author both interpretations, your confidence, why it is
   ambiguous, and, where possible, one experiment that answers both plus a
   response wording that stays valid under either. Surface this before any
   scarce resource is spent.
4. **Rate each concern** on four axes:
   - **Severity:** FATAL (if valid and unresolved, the main claim dies:
     correctness flaw, leakage, invalid protocol) > MAJOR (could reject, but
     survivable if resolved: missing strong baseline, weak ablation) >
     MODERATE (dents confidence or scope) > MINOR (typos, local clarity).
   - **Sharedness:** raised by all reviewers, several, one, or the meta-review.
     Shared concerns outrank lone ones.
   - **Decision impact:** how much resolving it could move the outcome, not
     the same as severity; a low-confidence outlier's major complaint may
     matter less than a shared moderate one.
   - **Resolution confidence:** can available evidence or a feasible
     experiment actually settle it before the deadline?
5. **Build the prioritized plan.** Label every proposed action:
   - **P0, must run now:** answers a fatal or shared major concern, feasible
     in time, interpretable even if negative.
   - **P1, high value if time remains** after all P0 work.
   - **P2, nice to have:** cheap, secondary, never allowed to delay P0.
   - **P3, defer to revision/resubmission:** needs redesign, new data, or
     more time than exists.
   - **Do not run:** does not touch the underlying doubt, duplicates existing
     evidence, or lacks the controls to be interpretable. Anxiety is not a
     reason to run an experiment.
   For each planned experiment, state the concern IDs it addresses, the
   hypothesis, baselines and controls, metric, seeds where relevant, the
   minimum result that supports the claim, what a negative result would mean,
   and the fallback wording if it cannot finish. Prefer information-dense
   experiments that answer several concerns at once (a matched-compute
   comparison hits fairness, efficiency, and baseline complaints together).
6. **Separate experiments from clarifications.** Return three buckets: run
   now; answer from existing evidence; defer. Many concerns need a sentence,
   not a run.
7. **Hand the author a result template** (experiment ID, concerns addressed,
   protocol, controls, metric, runs, result, uncertainty, surprises, claim
   supported / not supported) so Stage 2 starts from structured evidence.
## Stage 2: Draft from evidence

Run only after the author supplies completed results, or explicitly confirms
no further experiment will run (then every unsupported claim stays visibly
marked).
1. **Validate each result before using it:** does it answer the underlying
   doubt, are the conditions matched, is the uncertainty adequate, and which
   exact claim does it license? Never upgrade an inconclusive result to a
   positive one.
2. **Update the concern ledger:** resolved, partially resolved, unresolved,
   resolved by clarification, conceded and narrowed, or deferred.
3. **Write every major response as Direct Answer -> Evidence -> Revision.**
   The first sentence answers the question outright, no throat-clearing
   thanks before it. The evidence follows with its controls and uncertainty,
   numbers paired (ours vs theirs, before vs after) and glued to the exact
   claim each measures. The revision names the concrete manuscript change,
   with its verified location.
4. **Order by decision weight:** fatal and central technical concerns, then
   shared major ones, then empirical validity and fairness, then novelty and
   positioning, then robustness/efficiency/reproducibility, then scope and
   clarity, minor comments last and grouped in one compact block. Merge
   shared concerns into one response unless the venue format forbids it.
5. **Open with a short summary** that names the strengths reviewers actually
   stated (never manufactured ones) and the two or three main concerns the
   response will resolve. This opener belongs to a global response; a
   per-review block under a character limit has none.
6. **Engage critics the way the paper engages rivals, credit, then
   contrast.** Concede what is right before contesting what is not: name the
   valid point in the concern, then the one axis where the evidence says
   otherwise. A reviewer treated as a careful reader reads the response
   carefully. Write for the neutral chair who will audit the exchange, not
   only for the reviewer.
7. **Handle negative or mixed results honestly.** A negative experiment can
   still help: narrow the claim to what the evidence supports, state the new
   limitation, and commit to the wording change. Never hide it.
8. **Keep the prose in house style:** short sentences (<= ~28 words), subject
   and verb early, no hedging "can/could" claims, every number attached to
   the exact thing it measures.
9. **When over the limit, run the trim ladder in `rebuttal-paragraph`:**
   duplication, padding, ceremony, low-stakes promises, then content; under a
   character limit the opening thanks and quoted reviewer sentences go first. Never cut direct answers, key numbers, controls, uncertainty,
   claim narrowing, or promised revisions.
## What moves scores

Distilled from nine public OpenReview threads in which a reviewer raised a
score after the response (eight 5→8 or 3→8 at ICLR 2024–2025; two raised
to 8 and to 9 at NeurIPS D&B 2022, starting scores not recorded). The cases
and what failed in the same threads are in `score-movers-guide.md`. Each move
carries the count of threads in which it appeared.

1. **A new number aimed at the named concern, stated inline** (9/9). It need
   not sit in a table or a revised PDF.
2. **The reviewer's own labels, point by point** (9/9). Verbatim quotation
   is optional and costs space; four of the nine paraphrased the labels.
3. **A concession that narrows a claim** (7/9): "will tone down", "You are
   correct", an introduction rewritten so its claims match the results.
4. **The location of every change** (7/9): appendix, table, figure, line.
   A promise with a location is a commitment; without one it is a hope.
5. **A fast second round that admits any error outright** (5/9). Where the
   form allows follow-ups, watch the thread, answer before the window closes,
   and concede in one sentence what is wrong.
6. **The protocol behind a disputed number, not a defense of the number**
   (4/9): which checkpoint, which averaging, which compute match.
7. **A global summary listing every new experiment** (6/9): written for the
   chair, never cited by the raising reviewer. Practice, not a finding: where
   the form has no global response, repeat a one-sentence list of the new
   experiments in each reply, and use a confidential channel for this only
   where the venue's instructions allow it.
8. **Commitments accepted in lieu of results** (3/9); in the clearest case
   the promises sat beside inline numbers.

Three of the nine papers were rejected anyway; one decision read "the
experiments seem still incomplete". One reviewer's flip does not move a chair
who still sees a gap. Write the summary for the chair as carefully as the
replies.

## Short-form venues

Some forms allow one response per review under a limit of a few hundred to a
few thousand characters; some also forbid links or uploads. Any one of these
changes the shape. The moves above still apply, though none of the nine
threads was written under such a form; the shape below is derived from them,
not observed. It replaces the order in Stage 2 item 4 and the opener in
item 5:

1. One block per reviewer label, direct answer first, in the reviewer's own
   numbering (W1, Q2, ...).
2. Inline numbers, as many as the limit affords, each with its denominator
   and the protocol in a clause ("same backbone, data split and compute
   budget: X vs Y").
3. One standalone concession sentence for each concern the ledger marks
   conceded and narrowed; none where the ledger has no such entry.
4. One commitment sentence naming what the final version will contain and
   where.
5. No opening thanks beyond a clause, no paper summary, no quoted reviewer
   sentences; the reviewer's labels (or a two-word paraphrase where they gave
   none) and three to six of their words, bold where the form renders
   Markdown, are enough.
6. The last sentence on the concern a chair would echo.
7. Slack for the second round when the form stays editable: a reviewer who
   names "one remaining" item must be answerable without cutting the first
   answer. Reserve table space with placeholder digits (`rebuttal-paragraph`, axiom
   18).

## Output modes

- **TRIAGE_AND_EXPERIMENT_PLAN**: before results: viability verdict, form
  record (per-review or per-paper, limit, allowed markup, editability,
  deadline, confidential channel), claim map from the abstract, concern matrix (ID / surface text / underlying doubt
  / severity / sharedness / confidence), P0-P3 plan, clarification bucket,
  time-budget suggestion, author result template, resubmission roadmap if
  return is low.
- **RESULT_INTEGRATION**: after some results: validity check per result,
  concern-resolution status, remaining gaps, whether more experiments beat
  more polishing, claims now supportable and claims that must narrow.
- **FULL_REBUTTAL**: the drafted response: opening summary, merged major
  responses, per-reviewer residuals, grouped minors, the manuscript revision
  list, and the word/character count against the venue limit. For a
  per-review form: no opening summary; one block per review, each with its
  count against the limit, placeholders visible, and, where the form has a
  channel for it, the summary for the chair drafted last.
- **RESUBMISSION_PLAN**: rejection-mechanism diagnosis, a
  preserve/change/remove table, a ranked revision backlog, the decisive
  experiments for the next submission, and the revised core story. Framed as
  the higher-return path, never as failure.
- **QUALITY_REVIEW**: audit a drafted rebuttal for buried answers, wrong
  concern diagnosis, unsupported claims, missing uncertainty, tone risks,
  unfulfilled promised revisions, claim-scope mismatch, links or uploads in a
  no-link form, a block over its character limit, changes without a location,
  concerns answered without the number that settles them, and unfilled
  placeholders.
## Evidence and integrity rules (non-negotiable)

- Never invent an experimental value, a reviewer quote, a citation, or a
  manuscript location.
- Never present planned work as completed, and never promise a future
  experiment will succeed.
- Never claim statistical significance without the test that supports it.
- Never conceal a negative result that reached the ledger, and never state
  ambiguous reviewer intent as certain.
- Missing information gets a visible placeholder the author must fill,
  `[RESULT NEEDED]`, `[SETTING NEEDED]`, `[LOCATION NEEDED]`: never a
  silently invented value.
## Tone

Calm, precise, auditable. "We agree...", "We clarify...", "Our presentation
may have obscured...", "We will narrow...". Never "the reviewer failed to
understand", never speculation about motives, never pressure for score
changes, thanks at most one clause in the opener, never inside a response, and the
first thing cut under a character limit. Process complaints (a
score-text mismatch, an unprofessional review) go through the confidential
channel, factually, quoting only what is necessary, kept separate from the
technical responses.

## Reference file

- `score-movers-guide.md`: the nine threads behind "What moves scores" (forum
  and reviewer IDs, the raise comments, what the authors did), the evidence
  behind each move, and what failed in the same threads.
