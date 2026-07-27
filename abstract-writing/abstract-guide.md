# How to Write a Research Abstract: Three Master Recipes
### A plain-English guide. No linguistics jargon. Follow the steps.

*Distilled from forensic dissections of fifteen abstracts by leading ML researchers, the
classic writing guides, and the canonical ML papers.*

---

## Part 0 — The five terms you need, in plain words

People who talk about writing use special words. Here is what they actually mean:

| Fancy term | Plain meaning | Example |
|---|---|---|
| **Subject** | The doer of the sentence. Who or what acts. | "**The system** raises the score." The system = subject |
| **Verb** | The action word. | "The system **raises** the score." |
| **Active voice** | The doer comes first, then the action. | Active: "The agent builds a model." Passive (avoid): "A model is built by the agent." |
| **Hedging** | Softening words that make you sound unsure. | "may", "might", "could", "seems to", "we believe" |
| **A "move"** | The job a sentence does in the abstract. | Sentence 1's job = "say what we made." Sentence 5's job = "give the numbers." |

That is all the theory you need. Everything below is recipes and checklists.

---

## Part 1 — The big secret: an abstract is six answers in a row

Every strong abstract answers the same six reader questions, in order.
One or two sentences per answer. That is the whole trick.

1. **What did you build?** (say it immediately, first sentence)
2. **How does it work?** (pick ONE mechanism — your best one — not four)
3. **Where did you test it?** (name the benchmark and why it is hard)
4. **What are the numbers?** (always as a comparison: from X to Y)
5. **How do you know it is your method?** (the ablation / the control)
6. **Why does it matter?** (one idea sentence, no numbers)

Write six rough bullets answering these. Then turn each bullet into a sentence.
That is your first draft. Everything else is polish.

---

## Part 2 — The three recipes

### Recipe A: Short and confident (the compressed opener)
*Use when: your idea is clean and one mechanism carries it. Masters of this style write
5-sentence abstracts.*

The moves, in plain words:
- Sentence 1 = the whole idea. No warm-up. "We give [SYSTEM], a [type of thing] that [does the core thing]."
- Pick ONE clever mechanism and give it one sentence. Not a list.
- Results carry no numbers. Instead: *better on [quality 1] than [rival class 1], better on [quality 2] than [rival class 2]* — for example, "more sample-efficient than deep RL, more compute-efficient than prompt-loop agents."
- Plain verbs: "We give", "We present", "We study". Nothing fancy.

**Fill-in template:**
> We give [thing] that [what it does in one clause]. The [thing] must [key property]. We define/enforce this as [the one mechanism]. We study it on [benchmark], finding it [better on axis 1] than [rival class 1] and [better on axis 2] than [rival class 2]. [One idea sentence about what this means.]

### Recipe B: Numbers as drama
*Use when: your numbers are dramatic — a large before/after jump.*

The moves, in plain words:
- Open with tension in ONE sentence: strong systems exist, **yet** they fail at this specific thing.
- Numbers always come in PAIRS, so the jump is visible: "from 12% to 78%." Never a number alone.
- Compare against a NAMED rival system or a human count ("solves puzzles that hundreds of humans could not"). A name makes it real.
- Answer the reviewer's biggest doubt inside the abstract, in one clause — for example, state why data contamination is impossible. Find your biggest doubt and kill it in one clause.

**Fill-in template:**
> [Strong systems] achieve [X], yet [fail at this specific thing]. We give [thing] that [idea]. [One mechanism sentence.] On [benchmark], it raises [metric] from [small number] to [big number], [extra comparison]. [Kill the reviewer's doubt in one clause.] [Significance sentence.]

### Recipe C: Start from something familiar (anchor, then extend)
*Use when: your idea extends something the reader already knows.*

The moves, in plain words:
- Sentence 1 names something everyone knows (PCA, collaborative filtering, gradient descent). Sentence 2: "Here, we extend..." The reader never feels lost.
- Prove big claims by LISTING real examples, not by adjectives. Not "our framework is general" but "it covers [four named methods your framework subsumes]."
- Spotlight ONE sharp number and stop. Not a table of metrics.
- The last sentence is an IDEA, not a result: "[The problem] may be simpler than was previously understood." The reader leaves with a thought, not a percentage.

**Fill-in template:**
> [Familiar idea] is the standard way to [task]. We extend it to [new setting]. [How it works, 1-2 sentences.] [One sharp number.] [Closing idea: "X may be [simpler/different] than previously understood."]

---

## Part 3 — Sentence surgery (fix any sentence with four checks)

**Check 1: Doer first, action right after.**
The reader wants to know WHO does WHAT immediately.
- Bad: "Validation of the model against every observed transition is performed by the harness."
- Good: "The harness validates the model against every observed transition."
- Rule of thumb: if the doer and the action word are more than ~3 words apart, rewrite.

**Check 2: One idea per sentence, about 20 words or fewer.**
If a sentence has "and ... which ... while ...", split it.
Count the words. Over 28 = must split. Over 20 = look for a cut.

**Check 3: Strong action word.**
- Strong (top writers use them): give, present, build, show, raise, clear, drop, extend, measure, solve, introduce, validate, reject.
- Weak (avoid): is, has, utilizes, performs, involves, "is able to", "serves to".
- If your action word is "is" or "has", the sentence is probably hiding a better one.

**Check 4: Numbers travel in pairs.**
A number alone means nothing. "From 7 to 93 with the same base model" tells a story.
Every number in the abstract needs a partner: before/after, ours/theirs, with/without.

---

## Part 4 — Translating advisor feedback into actions

Advisors give writing feedback in shorthand. Turn every note into a mechanical action you
count, search for, or check off — never into a vague intention. Common translations:

| Advisor says | What to actually do |
|---|---|
| "Short clear sentences; subjects and verbs carry the meaning" | Doer + action word, side by side, early in the sentence (Check 1 + 2 above). |
| "Contribution up front" | Sentence 1 = what you built. Not background. Not "Recently, LLMs have..." |
| "Remove can" | Search your draft for "can", "cannot", "could". Zero allowed. Fix: "the model can predict" becomes "the model predicts". |
| "No this without a verb" | Never start "This shows..." — the reader asks "this WHAT?". Always "This **gate** shows...", "This **result** shows...". Put a noun after every This/These. |
| "Use the real number" | Attach every statistic to the exact claim it measures. Never borrow a similar-looking number from a different measurement — reviewers trace numbers to their source. |
| "Write in academic English" | No contractions (don't → do not). No chatty words (basically, really, pretty much). Plain formal sentences. |

---

## Part 5 — The assembly line (do this, in order)

1. **Answer the six questions** from Part 1 in rough bullets. Ugly is fine.
2. **Pick a recipe** (A, B, or C). If your before/after numbers are dramatic, use B's
   structure with A's shortness. If your advisor favors ideas over metrics, close with
   C's idea sentence.
3. **Draft it.** One sentence per bullet. Do not polish while drafting.
4. **Run the mechanical checklist:**
   - [ ] Sentence 1 states what we built, with a strong verb
   - [ ] Count words in every sentence (none over ~28)
   - [ ] Search "can" / "could" → zero hits
   - [ ] Every "This/These" has a noun right after it
   - [ ] Every number has a partner number
   - [ ] Every number is attached to the exact claim it measures
   - [ ] Last sentence = idea, not number
   - [ ] 140–190 words total
5. **Read it aloud.** Anywhere you stumble, the reader stumbles. Fix that spot.
6. **Compare against the closest rival paper's abstract.** Yours must sound related but
   clearly different: name (to yourself) the one clause that separates your method from
   theirs, and make sure a reader hears it.

---

## Part 6 — The template, assembled

The six answers turned into a fill-in-the-blank abstract. Bracketed slots are yours;
each sentence's job is in the table below.

> We present [SYSTEM], a [setting] method in which [the agent] [does the core thing]. We evaluate [SYSTEM] on [benchmark]: [what makes it hard, one clause]. Earlier approaches [the old way, one clause]. In [SYSTEM], [the new way]: [the artifact], which must [key property] before [the costly step]. This [mechanism noun] costs no [scarce resource]; [the resource] goes only to [verified work] or [deliberate work]. [SYSTEM]'s [source of strength] supplies [what]: [small amount of evidence] pins down [what it learns]. On [N] percent of [units] ([a of b]), [the strong outcome]. The remaining [units] require [the fallback mechanism]. [SYSTEM] raises [metric] from [low] to [high] and [clears X of Y]. A matched ablation removes [the component] and drops [metric] to [middle]. [Closing idea sentence — what the result means, no numbers.]

**Why each sentence is there:**

| # | Sentence | Job (Part 1 question) | Rules it shows |
|---|---|---|---|
| 1 | "We present [SYSTEM]..." | What did you build? | Contribution first, strong verb |
| 2 | "We evaluate... on [benchmark]" | Where did you test? | Context arrives before any statistics |
| 3 | "Earlier approaches..." | Contrast | One clause; aim it at a real class of prior work, not a strawman |
| 4 | "In [SYSTEM], [the new way]..." | How does it work? | Doer + verb adjacent |
| 5 | "This [mechanism noun] costs no..." | The ONE mechanism | "This + noun"; strong verb, not "is" |
| 6 | "[Source of strength] supplies..." | The finding | Say where the power comes from |
| 7 | "On [N] percent of [units]..." | The finding, quantified | Number paired with its raw counts |
| 8 | "The remaining [units] require..." | The finding's limits | Honest scope of the claim |
| 9 | "[SYSTEM] raises [metric] from [low] to [high]" | The numbers | Numbers in pairs |
| 10 | "A matched ablation removes..." | How do you know it is your method? | The control; verbs "removes"/"drops" |
| 11 | Closing idea | Why does it matter? | No numbers, no "can" |

**Mechanical audit to reproduce:** total words within 140–190 · longest sentence under
~28 words · zero "can/could" · every "This" followed by a noun · no contractions · every
number paired and attached to the claim it measures.

---

## Part 7 — More rules from the masters (plain English)

Distilled from the abstract dissections, the classic writing guides (Peyton Jones,
Widom, Whitesides, Mensh & Kording), and the famous ML abstracts (Transformer, ResNet,
AlphaGo, MuZero, DreamerV3, BERT, CLIP):

1. **Write the abstract last.** You cannot summarize a paper that is not finished. Freeze
   the numbers first.
2. **Shape: wide, then narrow, then wide.** Start at the field level, narrow to your
   method, end wider than your paper. Never state a result before the reader has the
   setup to understand it.
3. **Your one clever idea gets its own sentence.** Never bury it in a "which also..."
   tail. Short is fine. A standalone sentence tells the reader "this is the point."
4. **Chain your sentences.** Start each sentence with something from the previous one,
   end with the new thing. The reader never holds two new ideas at once.
5. **Longest sentence = the mechanism. Shortest sentence = the close.** The rhythm tells
   the reader what is heavy and what is final.
6. **Make the punchline a negation.** The famous abstracts end their claims with what
   they DON'T need: "without any lookahead search", "dispensing with recurrence
   entirely". State what your method removes, avoids, or never had access to.
7. **"Simple" is a boast, not an apology.** "A simple network architecture" (the
   Transformer paper). Say the idea is simple with pride; never write "we attempt to."
8. **Write about the problem, not about yourselves.** Banned: "We are interested in..."
   Readers care about what is broken in the world, not your interests.
9. **Decide your paper's type before choosing numbers.** Scoreboard paper (the number is
   the news) → put the dramatic number in. Idea paper (the shape of the method is the
   news) → mostly skip numbers, prove reach by breadth, keep ONE headline figure.
10. **Never open with a sentence that could start any paper in the field.** "Deep
    learning has achieved remarkable success" is dead on arrival. Open on the specific
    tension your paper resolves.
11. **No citations, no related-work sentence, no limitations list in the abstract.** One
    differentiating clause is the entire allowance. Everything else goes in the body.
12. **Read it cold, in one pass, as a stranger.** If that stranger cannot repeat your
    problem, your idea, and your evidence afterward, start over.

---

**Semicolon rule (addendum).** A semicolon is earned only by a true antithesis or
tightly parallel pair; everything else takes a period. Budget about two per section.
After any editing pass, grep `;` — each survivor must name its antithesis or become a
period.
