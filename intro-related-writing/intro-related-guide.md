# How to Write an Introduction and Related Work
### A plain-English guide. No linguistics jargon. Follow the steps.

*Distilled from forensic dissections of fifteen papers by leading ML researchers, the
classic writing guides, and the canonical ML papers. Sibling of `abstract-writing/`.*

---

## Part 0 — The terms you need, in plain words

| Fancy term | Plain meaning |
|---|---|
| **Hook** | The first sentence's job: make the reader care before anything technical. |
| **Funnel** | The intro's shape: wide (field) → narrow (your method) → forward (contributions). |
| **The gap** | What is missing in the world, stated as a COST ("without X, systems waste Y"), not as "little work has studied...". |
| **Artifact** | The thing you built, named once, at the pivot of the intro. |
| **Citation as subject** | "SystemX introduced the idea that..." — the cited work is the doer. Use for rivals you engage. |
| **Citation in parentheses** | "...is well studied [1,2,3]." — the citations are evidence, not actors. Use for background. |
| **Credit-then-contrast** | The two-beat pattern for rivals: say warmly what they did, then state your one difference and its consequence. |
| **Annotated bibliography** | The failure mode: a list of paper summaries with no relation to YOUR work. Reviewers hate it. |

---

## Part 1 — The big secret: an intro is a funnel of seven answers

A strong introduction answers seven reader questions, in order, roughly one paragraph
each. The reader never has to hold an unanswered question for long.

1. **Why should I care?** (the hook — a capability, a cost, or a puzzle)
2. **What world are we in?** (one or two sentences of shared ground)
3. **What is missing, and what does it cost?** (the gap, as named concrete costs)
4. **What did you build?** (the artifact, named, with its one-sentence idea)
5. **How does it work?** (ONE mechanism, concept only — constants and per-step details go in Method)
6. **What did you find?** (contributions + your headline number — stated HERE, never saved for a surprise ending)
7. **How does it differ from the nearest work?** (one clause; the full treatment is Related Work's job)

Two rules that outrank all others:
- **Write the contributions first, then build the intro backwards from them.** Every
  paragraph exists to earn a bullet.
- **Never keep the result for a surprise.** Papers are not mystery novels; the reader
  decides whether to continue based on the intro, so the payoff goes in the intro.

---

## Part 2 — The three intro recipes

### Recipe A: The quiet build (short and confident)
*Use when the idea itself is the star.*
- Open on a human skill or a vivid, familiar capability ("Consider learning a new
  device with no manual...").
- Silhouette the problem fully before naming the artifact — the reader should almost
  invent your solution themselves, then meet it.
- One mechanism paragraph, humble plain verbs, no chest-beating.
- Contributions may be prose rather than bullets when there are two or three.

**Template:** [Human skill or vivid scenario]. [Why machines lack it]. [The cost of
lacking it]. We present [ARTIFACT], which [one-sentence idea]. [One mechanism
paragraph]. [Findings + headline number]. [One-clause differentiation.]

### Recipe B: The answer-first opener (numbers as drama)
*Use when your headline number is dramatic.*
- State the result in the FIRST paragraph — the intro then explains how it was earned.
- Pre-empt the reader's biggest doubt (contamination, leakage, unfair baseline) within
  the intro, in one clause.
- Order everything by importance, not chronology: the most important claim first.

**Template:** [Strong systems] achieve [X], yet [fail at this]. We present [ARTIFACT],
which raises [metric] from [low] to [high]. [How, in two paragraphs]. [Doubt killed in
one clause]. [Contributions as bullets.]

### Recipe C: The familiar anchor (patient extension)
*Use when your idea extends something the reader already knows.*
- Open on a familiar object or method everyone uses.
- Frame the gap as a paradox: "everyone relies on X, yet nobody has explained/solved Y."
- Build patiently — each paragraph adds exactly one idea — and let the artifact appear
  as the natural resolution.
- Close on an idea the reader keeps, not only a number.

**Template:** [Familiar thing] is the standard way to [task]. Yet [the paradox]. We
extend [familiar thing] to [new setting]: [ARTIFACT]. [Mechanism]. [One sharp number].
[The idea the reader keeps.]

---

## Part 3 — The Related Work recipe

**Placement and shape.** Group by THEME, not by paper. Order the groups far-to-near:
distant background first, the closest rival group LAST, immediately before your
differentiation — so the section ends by sharpening what is new about yours. Never open
the paper with a wall of citations before your own idea has been stated.

**Citation grammar — two modes, used deliberately:**
- Background: parenthetical clusters. "Learned world models are well established
  [1, 2, 3]." The papers are evidence.
- Engaged rivals: the system is the sentence subject. "SystemX introduced the
  constraint that..." The paper is an actor you answer.

**The credit-then-contrast pattern** (one per rival, two beats):
> "[Rival] introduced [their real idea, stated warmly]. We keep [the shared part] but
> [your one difference], so [the consequence for the reader]."

Three invented worked examples of the shape:
1. "SystemX synthesizes the controller and the verifier jointly. We keep its
   program-repair loop but split verification into a separate free check, so no action
   issues from an unverified model."
2. "SystemY verifies its model against past data in an advisory pass. We make the same
   check an unbypassable gate, so verification is a precondition rather than a signal."
3. "Concurrent SystemZ separates acting and modeling across two agents; we use one
   agent and adopt SystemZ's published metric for direct comparison."

Note the manners: each rival's idea is stated as a genuine achievement; the contrast is
one clause; a concurrent system is labeled concurrent and its metric adopted where
possible. Your closest rival's authors are your likeliest reviewers.

**The failure mode to avoid:** paragraph after paragraph of "Paper A did this. Paper B
did that." with no sentence relating any of them to your work. Every related-work
paragraph must end in a clause about YOUR method.

---

## Part 4 — Mechanical checklists

**Introduction:**
- [ ] Contributions written first; every intro paragraph earns a bullet
- [ ] The seven questions answered in order; none held open for more than a paragraph
- [ ] The gap stated as named costs, not "little work has..."
- [ ] The artifact named exactly once at the pivot
- [ ] ONE mechanism, concept only; constants and step mechanics deferred to Method
- [ ] Headline number appears in the intro
- [ ] One named axis for the key idea, coined once, reused verbatim thereafter
- [ ] No "can/cannot/could"; no bare This/These; numbers in pairs; sentences ~<=28 words

**Related Work:**
- [ ] Grouped by theme, ordered far-to-near, closest rival last
- [ ] Rivals as sentence subjects; background as citation clusters
- [ ] Every rival: credit-then-contrast, contrast in one clause
- [ ] Concurrent work labeled concurrent
- [ ] Every paragraph ends by relating the group to YOUR method
- [ ] No annotated bibliography; no rival dismissed without credit

**Tense, in plain words:**
| Use | For |
|---|---|
| "X has shown..." | what the field established (still true) |
| "X introduces..." / "we present..." | what a specific system or your paper does |
| "It was believed..." | a belief your paper overturns |

---

## Part 5 — The assembly line

1. **Write the contribution bullets** (refutable claims, bold first lines).
2. **Pick a recipe** (A quiet build / B answer-first / C familiar anchor) by what your
   paper's star is: the idea, the number, or the extension.
3. **Draft the seven funnel paragraphs**, one per question, ugly first pass.
4. **Weave the rivals**: group by theme far-to-near, apply credit-then-contrast, end
   each group on your method.
5. **Run both checklists.** Fix every unchecked box.
6. **Read intro + related work cold, in one pass.** A stranger should finish knowing
   your problem, your idea, your evidence, and exactly how you differ from the nearest
   system.
