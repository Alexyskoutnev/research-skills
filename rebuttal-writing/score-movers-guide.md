# What moves a reviewer's score: the evidence behind the rules

Companion to `SKILL.md`. The rules there are distilled from the cases here; read
this when you want to know *why* a rule exists or need the pattern behind it.

Sources: nine public OpenReview threads in which a reviewer raised a score after
the author response, read in full (reviews, responses, follow-ups, meta-reviews).
Eight are ICLR 2024–2025 main-track papers found through OpenReview's public
search endpoint; one is a NeurIPS 2022 Datasets & Benchmarks paper (MineDojo).
Initial scores come from the reviewers' own "from X to Y" comments, final scores
from the stored reviews. Quotes are kept under fifteen words. Three of the nine
papers were still rejected, which is itself a finding.

## The cases

| Paper (venue, outcome) | Score move | What the reviewer said moved them | What the authors did |
|---|---|---|---|
| GNNCert / GraphGuard (ICLR 2024, oral) | 5 → 8 | "the authors have promised to address several weaknesses" | Conceded uncited prior work ("will cite and discuss", "will tone down our claim"); ran the missing plain baseline and reported it **inline, with no table and no PDF revision** (≤3% gap on 6 datasets, ≤15% on 2). Two comments of 2.4k and 3.6k characters, bold paraphrased headings, answer first. When the reviewer found a contradiction in the reply, the authors wrote: "Yes, the understanding of the reviewer is correct." |
| SEDD discrete diffusion (ICLR 2024, rejected) | 3 → 8 | "the results remain impressive even with the additional experimental results" | Rewrote the proofs, corrected a theorem statement, added three baselines with compute matching, qualified a "first time" claim. Global response (3.4k, one table) plus per-reviewer response (8.8k) opening with a three-bullet executive summary and the reviewer's own [W1]–[W5] labels. The AC still rejected: "the experiments seem still incomplete". |
| LaMo offline RL (ICLR 2024, poster) | 5 → 8 | "increasing my confidence that the experiments support the claims" | Explained the **protocol behind the disputed number** (average of the last checkpoints versus the best checkpoint), then added the table the reviewer's metric implied, full ablations with appendix locations, and a parameter-count table for the reviewer's "one remaining" concern. Global EXP1–EXP7 list plus per-reviewer 13k characters quoting every reviewer sentence, Q1.1/A1.1 numbering, answer first. |
| In-context vs in-weight learning (ICLR 2025, poster) | 5 → 8 | "the claims and the theory now line up" | Round one, mostly "please see the general response", failed; the reviewer kept three weaknesses and offered the deal: make the introduction's claims match the conclusions. Round two **rewrote the introduction** (line numbers cited), replaced a loose proposition with a tight bound, and added the sentence that the model is "only an example of a mechanism". Narrowing, not new experiments, decided it. |
| Stiefel flow matching (ICLR 2025, poster) | 5 → 8 | "additional baseline results and further ablation studies" | Conceded ("You are correct that molecules are not perfectly rigid"), put the argument the reviewer wanted in an appendix, added a baseline, a six-row timing table and convergence statistics. Bold run-in headings restating each concern; concession, then argument. |
| Δ-DiT (ICLR 2025, rejected) | 5 → 8 | "the additional experiment and the explanation of Tables 2 and 10" | Three-part response with verbatim italic quotes and three tables; the explanation of two existing tables counted as much as the new experiment. |
| MaxSup (ICLR 2025, rejected) | 5 → 8, in round three | — | Re-ran the baseline **with the setting the reviewer suggested** and inserted the reviewer's own explanatory sentence into the paper. |
| GATE (ICLR 2024, poster) | 5 → 8 | "being able to understand the method deepens my appreciation of it" | A PDF revision that unified the notation. Clarity alone moved the score. |
| MineDojo (NeurIPS 2022 D&B, accepted) | 7 → 8 and 8 → 9 | "convincing results during this rebuttal phase" | Quoted each reviewer sentence, then answered it; ran the exact experiment asked for (a single multitask agent, held-out tasks, five harder evaluation tasks) and reported it as a table in the paper's own metric; toned down the overclaim ("we have toned down the claim in Sec. 6") and named every revision's location ("added to the supplementary, Sec. 9.3"). Six responses, each 2k–6k characters, split into numbered parts. |

## The moves, ranked by how often they appeared (n = 9)

1. **New numbers aimed at the named concern, stated inline** (9/9). Every
   raise comment cites a specific experiment or table, never the thanks or the
   prose. The number need not be in a table or in a revised PDF.
2. **Mirror the reviewer's own labels, point by point** (9/9). Five threads
   quoted verbatim, four paraphrased; both worked. Labels suffice; verbatim
   quotation is optional and costs space.
3. **An explicit concession that narrows a claim** (7/9): "will tone down",
   "You are correct", an introduction rewritten, "only an example of a
   mechanism". In one case this alone was the raise.
4. **The exact location of each change** (7/9): appendix, table, figure,
   line number. A promise with a location reads as a commitment; without one
   it reads as a hope.
5. **A fast, short second round that admits any error outright** (5/9). In
   three threads the reviewer named one deciding item ("one remaining",
   "especially 1 and 4") and raised after it was resolved. The decisive
   exchange is often the follow-up, not the first response.
6. **The protocol behind a disputed number, instead of a defense of the
   number** (4/9): which checkpoint, which averaging, which compute match.
7. **A global summary listing every new experiment** (6/9): read by the AC,
   never cited by the raising reviewer.
8. **Concrete commitments accepted in lieu of results** (3/9): GNNCert's
   5 → 8 rested on promises plus two inline numbers.

What never appears in a raise comment: thanks, restated contributions,
background, or the authors' summary of the paper.

## What failed, in the same threads

- "Please see the general response" as the per-reviewer answer (one round lost).
- Defending a number without its protocol (the raise came only after the
  protocol was explained).
- A first response that argued where the reviewer wanted a narrower claim
  (the reviewer repeated the three weaknesses verbatim).
- New experiments without the specific one the AC called "incomplete": three
  papers with a 5 → 8 reviewer were rejected anyway. One reviewer's flip does
  not move a chair who reads "incremental" or "incomplete" in the other reviews.

## Short-form venues (character limits, no links)

Some venues allow one response per review, a limit of a few thousand or a few
hundred characters, and forbid links, uploads, and references to external
material under threat of rejection. GNNCert is the existence proof that this is
enough: two comments, no tables, no revised PDF, numbers inline, and a 5 → 8.

Per response, in order:

1. One block per reviewer label, direct answer first, ordered by the
   reviewer's own severity.
2. Two to four inline numbers, each with its denominator and the protocol in
   a clause ("same model, sandbox and action cap: X vs Y").
3. One concession sentence that narrows a claim. Standalone, not subordinate.
4. One commitment sentence naming what the final version will contain and
   where.
5. No opening thanks beyond a clause, no paper summary, no verbatim quotes;
   the reviewer's labels and three to six of their words in bold are enough.
6. If a disputed number stems from protocol, state the protocol.
7. Spend the last sentence on the concern an AC would echo.
8. Leave slack for the second round when the form stays editable: a reviewer
   who names "one remaining" item must be answerable without cutting the first
   answer.

A three-row Markdown table costs 250–350 characters; a placeholder table with
`XX.X` digits reserves that space so results drop in without re-trimming.

## Reconnaissance before drafting

Read the live form, not the call for papers. Record: one response per review or
one per paper; the limit, in characters or words; whether Markdown, LaTeX,
tables, links, or uploads are allowed; who reads each response; whether
responses are editable until the deadline; the deadline with its time zone; and
whether a confidential channel to the chair exists. Each of these changes the
draft's shape, and a form that forbids links turns "see our repository" into a
rejection.
