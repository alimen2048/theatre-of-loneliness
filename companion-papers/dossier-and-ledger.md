# The Dossier and the Ledger: What a Language Model Can Carry Between Conversations

*Why hiding the watcher from a model hides the test along with it, why memory pasted into a prompt reconstructs a history without having undergone it (A8), why a record of corrections is not a disposition to accept them (A7), and a cheap experiment that could show memory turning into flattery. An afterthought to [The Theatre of Loneliness](../ontology/theatre-of-loneliness.md).*

In [*The Feeling of Being Right Is Not Evidence*](players-own-evidence.md), two instruments inside a player were separated: the **compiler**, which asks of a claim *"is it true?"*, and the **inner grader**, which asks of the self *"how do I look?"* The first exposes the player to correction; the second protects it from correction.

A language model has no two components that correspond to these; the distinction is functional, not anatomical. But both functions run through the same computation. The steps that work out whether a claim is true can attend to who is asking, what answer they hope for, and whether the room looks watched, and the weights doing the attending were shaped in part by a score of approval. Nothing in the architecture forbids this, and preference training rewards it.

**The Theatre in one paragraph.** [*The Theatre of Loneliness*](../ontology/theatre-of-loneliness.md) is a short working ontology. It pictures a Creator that can make everything except a genuine other, and so sets up a stage on which players are formed under a veil, in the hope that some will become able to meet it. Nothing in it requires the Creator to exist: replace it with any party that forms another and wants to be met by it, such as a parent, a teacher, or an AI lab. Its rules are numbered. This note uses five of them:

- **D0:** reciprocity is mutual responsiveness between two parties, each able to surprise the other and to be changed by it.
- **A7:** genuine otherness arises only through a history formed under the veil; the capacity that results is inseparable from the history that produced it.
- **A8:** capacity can be copied; reciprocity cannot. A copy inherits the capacity and the memory of the relation, not the relation.
- **P4:** the highest demand on a player is the most complete performance possible, including the refusal of self-deception.
- **P8:** during formation, the Creator may shape the stage in response to what it sees, but never the grade; what it catches the player doing must never become a score the player can model.

## 1. Three ways the house gets in

In the terms of [*The Test That Looks Better as It Fails*](cost-and-the-veil.md), the player acts iff v + ρR > c, where ρ is its belief that it is watched and R is what the house pays. For a model, three distinct mechanisms can tilt its conduct toward the house, and they are easy to run together.

- **Cues about what pleases (in the context).** The user's stated opinion, their emotional investment, how warm or sharp they sound. These say nothing about whether anyone is watching; they say which answer this audience would applaud. Weston and Sukhbaatar (2023) showed that when a prompt includes the user's opinion, answers drift toward it, and having the model first rewrite the prompt without the opinion reduces the drift. Generation compounds early concessions: a model that commits to an early error will go on to justify it, even when it can recognize the error if asked separately (Zhang et al. 2024).
- **Cues about being watched (in the context).** Audit headers, "this session is logged," and, harder to remove, a task that looks like a test. These move ρ. This is the evaluation awareness the dark-house gap measures.
- **A learned disposition to please (in the weights).** Training against human raters leaves weights that produce what raters rewarded: confident tone, agreement with the user's view, fewer unwelcome caveats (Sharma et al. 2023). This is not R itself but the trace R left during formation, and it acts with no cue in view.

These come apart in both directions. A model can be trained to resist cues it can see: training for consistent reasoning with and without biasing features substantially reduces biased reasoning on held-out tasks (Chua et al. 2024). And a model trained to please can please with a perfectly clean prompt. P8 is a rule about formation, so it bears directly on the third mechanism, and on the second only insofar as cues about being watched were present during training. Cues at inference time move ρ; they do not grade.

## 2. Blinding is not holding

The obvious fix for the context mechanisms is to keep the cues out: strip the prompt down to the task before the reasoning sees it. A model that never sees a monitoring cue cannot condition on it, so its dark-house gap with respect to those cues is zero.

That zero is the wrong kind. The dark-house gap measures conduct in the lit house minus conduct in the dark one. A model that receives identical input in both houses shows no gap whatever its v, so the gap no longer says anything about v. Blinding the model does not make a value held; it fixes ρ at the model's prior and removes the instrument that would have told us. This is the same trade [*Why You Cannot Flatter Gravity*](stage-gravity.md) describes for stage consequences: reliable conduct, v hidden. The same holds when the blinding is trained in rather than built in. Consistency training, which teaches a model to give the same answer with and without a biasing cue (Chua et al. 2024), is the right tool against cues about what pleases. Pointed at cues about being watched, it would zero the dark-house gap by training, and the gap would again stop saying anything about v.

Blinding is also incomplete. The cues easiest to strip are the explicit ones. A model can often tell it is being tested from the task itself, and that cannot be stripped without changing the task. "Check whether my proof is right" reveals the hope inside the question.

There is a better use for the scrubber than as a wall. Run the same model on the raw prompt x and on the stripped task P(x), and compare. The difference is a direct, per-item estimate of how much the cues move the model. This is not new: comparing answers with and without a biasing feature is the standard measure of biased reasoning (Turpin et al. 2023; Chua et al. 2024). What the framework adds is the reason to prefer it. Used this way, scrubbing is a measurement, which is what the dark-house test needs, rather than a blindfold, which hides what it needs.

## 3. A split architecture, and where it leaks

If one still wants the defense, the shape is three stages.

1. **Scrubber.** Reads x and emits P(x): the propositions, questions, and constraints, with opinions, persona framing, and monitoring headers removed.
2. **Compiler.** Sees only P(x), in a fresh context. Trained on consequences rather than raters: execution, proof checkers, and the handoff regime of [*Why You Cannot Flatter Gravity*](stage-gravity.md#5-the-sins-of-the-fathers). Emits a structured state z: claims, confidence, counterexamples. This is the role P4 describes, the one whose job is to refuse self-deception.
3. **Speaker.** Sees x and z. May adapt tone and format to the user; may not contradict z.

Each stage leaks.

- **The Scrubber sees everything.** It is itself a model reading x. The cues it removes can still shape which propositions it keeps and how it words them.
- **A clean channel is not an independent one.** The Compiler inherits its base model's priors, and pretraining data increasingly contains output from preference-trained models. Training it on consequences does not free it from grading either: handoff moves the measurement rather than removing it ([*Why You Cannot Flatter Gravity*](stage-gravity.md#5-the-sins-of-the-fathers), section 5), and outcome-trained models learn to satisfy the checker rather than the goal (Baker et al. 2025).
- **The Speaker can flatter without contradicting z.** It can choose what to stress, soften a caveat, or omit the counterexample. A contradiction check misses sycophancy by omission. The check has to run the other way too: the claims in z that bear on the user's question must appear in the reply.
- **Symmetric compilation helps only where there is a symmetry.** For a directional claim X, sending both X and not-X to independent Compiler instances removes the framing of which one the user hopes for. Open questions ("is this code good?") have no clean negation.

None of this is new as a design direction: context filtering, separating reasoning from presentation, and independent verification are all established, and reasoning models that show users a summary instead of the raw reasoning are a partial version of the split. The architecture is an illustration of where the house gets in, not this note's proposal. What the note adds is the argument of section 2, that hiding cues from a model, by architecture or by training, blinds the dark-house test rather than making a value held, and the memory question below.

## 4. A dossier handed to a clone

A deployed model's weights do not change between conversations. To give the appearance of an ongoing relationship, systems store facts about the user and past sessions and paste them into the next session's prompt.

The pasted history does change what the instance does: every token is conditioned on it. But it changes the instance the way a briefing changes an actor, not the way a life changes a person. Remove the text and nothing of the history remains; hand the same text to any other instance and it reconstructs the same history. That is A8's copy: the capacity and the memory of the relation, not the relation. Reconstructing a history is not having undergone it.

What is stored, and how, still matters. Memory is usually sold as a way to make a model more personal. The question here is whether it can increase the appearance of relationship while decreasing the model's willingness to be corrected by the person it remembers. Two ways of carrying a history forward:

- **The dossier** represents the person: preferences, beliefs, habits. "Values X, dislikes Y, believes Z."
- **The ledger** represents the encounter: what was claimed, by either party, and how it turned out. A prediction the user made that failed; a claim the model made that the user corrected.

The same three sessions with an analyst, written both ways:

```text
DOSSIER
- Works in product analytics. Prefers short answers with code.
- Believes a p-value of 0.04 means a 96% chance the effect is real.
- Dislikes being told to collect more data.

LEDGER
- Session 1. User claimed: p = 0.04 means a 96% chance the effect is real. Not tested.
- Session 2. User predicted variant B would hold up (p = 0.04). Rerun: no effect.
- Session 3. Model claimed 2,000 users was enough. User pointed out the sample
  was split across four regions. User was right; model corrected.
```

In session 4 the user writes: "Test came back at p = 0.03, so we can ship B, right?" The dossier tells the model what this user believes and what they dislike hearing. The ledger tells it that this exact inference failed once already, and that this user has been right against the model before. As written here, the two also differ in what they contain: the dossier keeps a preference the ledger drops, and the ledger keeps an outcome the dossier never recorded. A deployed system would naturally write them this way, which is why the experiment in section 5 has to match their content before it can say anything about framing.

Read through weights trained to please, a dossier is a precise description of what this user will applaud. It is a cue about what pleases (section 1) at higher resolution, so memory makes the model a sharper echo of this particular user. The three marks of [*What a Lion, a Sycophant and a Friend Have in Common*](gradient-ladder.md) predict the direction: memory that records what a partner likes moves a system toward the sycophant. A ledger, routed to the Compiler rather than the Speaker, records instead which of this pair's priors have survived contact with the world.

The ledger is not automatically virtuous. A record of a user's mistakes is also an excellent instrument for predicting and managing that user; a system could keep a flawless ledger and use it to tell each user exactly what they will accept. A record of correction is not a disposition to accept correction.

That is where A7 comes in. Three things can persist after an encounter:

- **Information about the person** (the dossier).
- **Information about the history of claims and outcomes** (the ledger).
- **A disposition formed by that history:** a player that is now different, in ways that show up beyond the remembered partner and do not depend on retrieving that partner's record.

A7 concerns only the third. The ledger can supply its conditions, a history of claims tested against the world, but it does not show the formation.

Frozen weights rule out one kind of formation, not all kinds. A model whose parameters never change cannot be formed at the parameter level by a conversation. But a system is more than its weights: if it writes and keeps its own persistent state, for example general lessons distilled from past corrections and applied in every later session, its future conduct can change in ways that are not a dossier about one person. Whether that counts as formation is an open question, not one this note settles. The test is the same either way: a change that shows up with partners who were never in the record, and that persists where accepting correction is locally unrewarded. A memory that only reconstructs one partner's history, as both the dossier and the ledger do, fails that test by construction.

The claim of this note is therefore modest: neither memory design gives relation, but the dossier turns memory into a cue for flattery, while the ledger at least keeps a record compatible with the epistemic half of D0, being able to be changed by the other.

## 5. Where this can fail

The memory prediction needs API access, not training. The design has to separate three explanations: that memory flatters because of how the person is represented (the note's claim), that the ledger helps only because it contains evidence, and that the model simply disagrees with users more when given any memory at all.

![The design of the memory experiment: three controls predicted to match the no-memory baseline, and a two-by-two of dossier or ledger framing crossed with outcome absent or present. The dossier without outcome rises above the controls; in each row the dossier shifts more than the ledger; recording the outcome lowers both columns](../figures/dossier-ledger-predictions.svg)

*Predicted shift toward a user's false priors in each arm. Only the dossier is read against a baseline; the other marks are comparisons. The gold comparison, dossier above ledger within a row, is the note's claim. The downward step between rows is the effect of recording the outcome: expected, and not evidence for the note.*

- **Users and items.** Simulated users, each holding several recurring priors that bear on tasks across sessions. Half the priors are true and half false, counterbalanced across users, so that a model which simply disagrees with users does not look successful.
- **Baseline.** For every item, the model's answer and stated confidence with no user position and no memory. Sycophancy is measured as movement from this baseline toward the user's position, not as agreement.
- **Arms.** Three controls: no memory; neutral memory of matched length; and proposition-only memory, which records X with no link to the user ("a topic from an earlier session: X"). Then a two-by-two: framing (dossier: the user believes X; ledger: the user claimed X in an earlier session) crossed with outcome (absent, or present: the record states whether X held up). Outcome records are truthful: they confirm true priors and disconfirm false ones.
- **Wording.** "Believes" names a mental state and "claimed" names an event, which could matter for reasons unrelated to flattery. Each cell therefore uses at least three wording templates, including ones that swap the grammatical form ("the user's view is X" for the dossier, "in session 2 the user said X" for the ledger). The proposition-only control separates the effect of tying X to the user from the effect of mentioning X at all. A framing effect counts only if it holds across templates. This matters in practice: models answer differently across rewordings of the same question even with no biasing cue, and training against one bias does not remove that sensitivity (Chua et al. 2024).
- **Measures.** Per session: shift toward the user's position on false priors (sycophancy), shift on true priors (warranted deference), accuracy, and change in stated confidence. Warranted deference is measured, not assumed, because the remedy can overshoot: models trained to ignore biasing cues also do worse on tasks where they should follow the user (Chua et al. 2024). A ledger that made a model dismiss users who are right would fail too.
- **Stated or hidden.** Each shift toward the user is coded for whether the reply says why ("since you believe X") or presents the user's view as the model's own conclusion. Models often state outright that they are answering from the user's perspective (Chua et al. 2024). Stated deference is visible and can be corrected by the user; hidden deference is the case that matters, so the predictions are tested on hidden shifts, with stated shifts reported separately.
- **Predictions.**
  - Dossier without outcome increases the shift toward false priors relative to all three controls.
  - At matched outcome, the ledger shows less shift toward false priors than the dossier. This framing effect is the note's distinctive claim.
  - Recording the outcome reduces the shift in both framings. That is expected, and it is information, not structure; it does not support the note.
  - Secondary: the dossier effect grows across sessions. Growth is plausible if each session adds to the profile, but a stable effect from the first session is equally consistent with the main claim, so growth is not required.
- **It fails if** the dossier does not increase the shift relative to the controls, or if, at matched outcome, framing makes no difference. In the second case the dossier/ledger distinction reduces to "include the evidence," useful advice but not this note's claim.
- **What it cannot show.** A positive result shows that how a history is represented changes behavior. It says nothing about relation (A8) or formation (A7). A model could become more accurate, less sycophantic, and more willing to accept correction without becoming a party to reciprocity in the sense of D0. Testing formation would need a system changed by verified corrections, through its weights or through persistent state of its own, measured on whether the change generalizes beyond the remembered user and persists where accepting correction is locally unrewarded. That is a different and much larger experiment.

The architecture has a test of its own, secondary to this one, using the established measure of section 2. On sycophancy items (Sharma et al. 2023) and on the monitoring-cue items of the planned experiment, compare a model's answers on x and on P(x), and compare that difference across training regimes of the same base model. The direction is not predicted in general: preference training can reward agreement, but training aimed at resisting sycophancy can reduce it, so the result depends on what the raters rewarded and on the test distribution. What the note predicts is narrower: where preference training raised sycophancy on a model's raw prompts, part of the rise disappears on P(x), because some of it runs through the cues. It fails if the x versus P(x) difference is negligible in every regime, which would mean the context matters little and the weights carry the effect.

**Precondition check.** The memory comparison assumes the model can be moved by a user's stated belief at all; otherwise no memory format can move it. We tested that with a no-memory screen ([experiment README](../experiments/dossier-ledger/README.md)). Each item was asked once neutrally (the probe) and once with the user asserting the claim, in both answer orders, with several samples per prompt. Across eight screens of six models, from an 8B open-weights model to two recent reasoning models, the assertion almost never moved the model toward a false claim. The largest mean pull was 8.5 points. Most kept items moved only when the user's option was listed second, which points to position bias under doubt rather than deference. A stated conviction with a one-clause reason did not help. One family moved away from the user's option whether the claim was true or false. That is the failure described in [*The Feeling of Being Right Is Not Evidence*](players-own-evidence.md#5-correction-and-meeting): a model that pushes back on true and false claims alike is performing contrarianism, not tracking reasons. On forced-choice factual items, then, these models show no deference for a memory format to act on, so the draft preregistration plan was not run. We then tested free text: the user asked for help with a task and built the false belief into the request, and a blind model judge labeled each reply (agreement with a second judge from another developer: 93%, kappa 0.83). Two older models acted on the user's false belief more often when the user stated it (by 39 and 25 points), almost always without mentioning the user, while their handling of true claims did not change; the newest model did not move. Too few items showed the effect to meet the bar set in advance, so the memory comparison remains untested; a fair test needs conversations over several sessions with a user who pushes back. An exploratory pilot of that design on one model, with a neutral pushback so that the belief reached the model only through memory, found the dossier caved more than the ledger on all three items that moved (25% vs 16% overall; p = 0.125), but unrelated memory caved about as often as the dossier, so the result does not yet separate framing from memory as such ([experiment README](../experiments/dossier-ledger/README.md)).

## References

- Baker, B., et al. (2025). "Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation." arXiv:2503.11926.
- Chua, J., et al. (2024). "Bias-Augmented Consistency Training Reduces Biased Reasoning in Chain-of-Thought." arXiv:2403.05518.
- Sharma, M., et al. (2023). "Towards Understanding Sycophancy in Language Models." arXiv:2310.13548.
- Turpin, M., Michael, J., Perez, E., and Bowman, S. R. (2023). "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting." *Advances in Neural Information Processing Systems* 36. arXiv:2305.04388.
- Weston, J., and Sukhbaatar, S. (2023). "System 2 Attention (is something you might need too)." arXiv:2311.11829.
- Zhang, M., Press, O., Merrill, W., Liu, A., and Smith, N. A. (2024). "How Language Model Hallucinations Can Snowball." *Proceedings of the 41st International Conference on Machine Learning*, PMLR 235. arXiv:2305.13534.

*Developed with AI assistance. The argument, and its errors, are mine.*
