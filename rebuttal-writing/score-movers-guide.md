# What moves a reviewer's score: the evidence behind the rules

Companion to `SKILL.md`. The rules there are distilled from the cases here; read
this when you want to know *why* a rule exists or need the pattern behind it.

Sources: nine public OpenReview threads in which a reviewer raised a score after
the author response, read in full (reviews, responses, follow-ups, meta-reviews).
Eight are ICLR 2024–2025 main-track papers found through OpenReview's public
search endpoint; one is a NeurIPS 2022 Datasets & Benchmarks paper (MineDojo).
Initial scores come from the reviewers' own "from X to Y" comments where they
wrote one, final scores from the stored reviews; a row without such a comment
says so. Forum and reviewer IDs: GNNCert IGzaH538fz/xWrk; SEDD 71mqtQdKB9/4UNx;
LaMo AY6aM13gGF/GHKm; ICL vs IWL aKJr5NnN8U/8YMd; Stiefel 84WmbzikPP/519h;
Δ-DiT pDI03iK5Bf/81e2; MaxSup zVtwIWyX4S/2YeD; GATE 3z60EWfh1p/Gg1C; MineDojo
reviewers bi9J and SPDY. Quotes are kept under fifteen words. Three of the nine
papers were still rejected, which is itself a finding.

## The cases

| Paper (venue, outcome) | Score move | What the reviewer said moved them | What the authors did |
|---|---|---|---|
| GNNCert / GraphGuard (ICLR 2024, oral) | 5 → 8 | "the authors have promised to address several weaknesses" | Conceded uncited prior work ("will cite and discuss", "will tone down our claim"); ran the missing plain baseline and reported it **inline, with no table and no PDF revision** (≤3% gap on 6 datasets, ≤15% on 2). Two comments of 2.4k and 3.6k characters, bold paraphrased headings, answer first. When the reviewer found a contradiction in the reply, the authors wrote: "Yes, the understanding of the reviewer is correct." |
| SEDD discrete diffusion (ICLR 2024, rejected) | 3 → 8 | "the results remain impressive even with the additional experimental results" | Rewrote the proofs, corrected a theorem statement, added three baselines with compute matching, qualified a "first time" claim. Global response (3.4k, one table) plus per-reviewer response (8.8k) opening with a three-bullet executive summary and the reviewer's own [W1]–[W5] labels. The area chair still rejected: "the experiments seem still incomplete". |
| LaMo offline RL (ICLR 2024, poster) | 5 → 8 | "increasing my confidence that the experiments support the claims" | Explained the **protocol behind the disputed number** (average of the last checkpoints versus the best checkpoint), then added the table the reviewer's metric implied, full ablations with appendix locations, and a parameter-count table for the reviewer's "one remaining" concern. Global EXP1–EXP7 list plus per-reviewer 13k characters quoting every reviewer sentence, Q1.1/A1.1 numbering, answer first. |
| In-context vs in-weight learning (ICLR 2025, poster) | 5 → 8 | "the claims and the theory now line up" | Round one, mostly "please see the general response", failed; the reviewer kept three weaknesses and offered the deal: make the introduction's claims match the conclusions. Round two **rewrote the introduction** (line numbers cited), replaced a loose proposition with a tight bound, and added the sentence that the ICL predictor is "only an example of a mechanism", and added a new figure. Narrowing, more than new experiments, decided it. |
| Stiefel flow matching (ICLR 2025, poster) | 5 → 8 | "additional baseline results and further ablation studies" | Conceded ("You are correct that molecules are not perfectly rigid"), put the argument the reviewer wanted in an appendix, added a baseline, a six-row timing table and convergence statistics. Bold run-in headings restating each concern; concession, then argument. |
| Δ-DiT (ICLR 2025, rejected) | 5 → 8 | "the additional experiment and the explanation of Tables 2 and 10" | Three-part response with verbatim italic quotes and three tables; the reviewer cited the explanation of two existing tables alongside the new experiment. |
| MaxSup (ICLR 2025, rejected) | 5 → 8, in round three | (no raise comment recorded) | Re-ran the baseline **with the setting the reviewer suggested** and inserted the reviewer's own explanatory sentence into the paper. |
| GATE (ICLR 2024, poster) | 5 → 8 | "being able to understand the method deepens my appreciation of it" | A PDF revision that unified the notation. Clarity alone moved the score. |
| MineDojo (NeurIPS 2022 D&B, accepted) | two reviewers raised to 8 and to 9 (starting scores not recorded) | "convincing results during this rebuttal phase" | Quoted each reviewer sentence, then answered it; ran the exact experiment asked for (a single multitask agent, held-out tasks, five harder evaluation tasks) and reported it as a table in the paper's own metric; toned down the overclaim ("we have toned down the claim in our revised paper (Sec. 6)") and named every revision's location ("added the above results to the supplementary (Sec. 9.3)"). Six responses, each 2k–6k characters, split into numbered parts. |

## The moves, with the count of threads in which each appeared (n = 9)

1. **New numbers aimed at the named concern, stated inline** (9/9). Five of
   the eight quoted raise comments name an experiment, a table, or results; the
   other three name promises (GNNCert), claims that now match the theory (ICL
   vs IWL), or clarity after a notation revision (GATE); MaxSup left no
   comment. None names the thanks. The number need not be in a table or in a
   revised PDF: GNNCert's 5 → 8 came from two comments with the numbers inside
   the sentences.
2. **Mirror the reviewer's own labels, point by point** (9/9). Five threads
   quoted verbatim, four paraphrased; both worked. Labels suffice; verbatim
   quotation is optional and costs space.
3. **An explicit concession that narrows a claim** (7/9): "will tone down",
   "You are correct", an introduction rewritten, "only an example of a
   mechanism". In one case (ICL vs IWL) the raise followed a round of narrowing: the
   introduction rewritten, a proposition replaced by a tight bound, one figure
   added; the first response, which mostly pointed to the general response,
   had left three weaknesses standing.
4. **The exact location of each change** (7/9): appendix, table, figure,
   line number. A promise with a location reads as a commitment; without one
   it reads as a hope.
5. **A fast, short second round that admits any error outright** (5/9). In
   three threads the reviewer named one deciding item ("one remaining", LaMo) and raised once it was
   resolved. Where the form allows follow-ups, answer before the window closes
   and concede any error in one sentence (GNNCert: "Yes, the understanding of
   the reviewer is correct"). The decisive
   exchange is often the follow-up, not the first response.
6. **The protocol behind a disputed number, instead of a defense of the
   number** (4/9): which checkpoint, which averaging, which compute match.
7. **A global summary listing every new experiment** (6/9): written for the chair,
   never cited by the raising reviewer.
8. **Concrete commitments accepted in lieu of results** (3/9): GNNCert's
   5 → 8 rested on promises plus inline numbers (the per-dataset gap on eight
   datasets and the base-classifier accuracies).

None of the eight quoted raise reasons mentions the thanks, restated
contributions, background, or the authors' summary of the paper.

## What failed, in the same threads

- "Please see the general response" as the per-reviewer answer (ICL vs IWL,
  round one): the reviewer kept W1, W2 and W4 and asked for the introduction's
  claims to match the conclusions; one round lost.
- New experiments without the one the chair still wanted: three of the nine
  (SEDD 3 → 8, Δ-DiT and MaxSup 5 → 8) were rejected anyway; SEDD's decision
  read "the experiments seem still incomplete". One reviewer's flip does not
  move a chair who still sees a gap.

## Short-form venues (character limits, no links)

None of the nine threads was written under a per-review character limit; the
template in SKILL.md, "Short-form venues", is derived from the moves, not
observed. The closest evidence is GNNCert: inline numbers with no table and no revised
PDF carried a 5 → 8, in 6k characters over two comments on a threaded form,
so a tighter limit still needs cutting.

## Reconnaissance before drafting

See the Stage-0 bullet "Read the live response form" in SKILL.md; each item
there changes the draft's shape.
