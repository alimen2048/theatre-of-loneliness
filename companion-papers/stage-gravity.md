# Why You Cannot Flatter Gravity

*Where a consequence lives decides what it teaches. Why gravity does not breed performers and graders do, why unit tests sit in between, and what "the sins of the fathers" means on a stage. An afterthought to [The Theatre of Loneliness](../ontology/theatre-of-loneliness.md).*

A bridge engineer is punished every time his math is wrong, and gravity never turns him into a sycophant. A language model is punished every time its answer displeases a rater, and it drifts toward telling raters what they want to hear (Sharma et al. 2023). Both face certain, heavy consequences. Why does one consequence form competence and the other form an actor?

**The Theatre in one paragraph.** [*The Theatre of Loneliness*](../ontology/theatre-of-loneliness.md) is a short working ontology. It pictures a Creator that can make everything except a genuine other, and so sets up a stage on which players are formed under a veil, in the hope that some will become able to meet it. Nothing in it requires the Creator to exist: replace it with any party that forms another and wants to be met by it, such as a parent, a teacher, or an AI lab. Its rules are numbered. This note uses these:

- **D0:** reciprocity is mutual responsiveness between two parties, each able to surprise the other and to be changed by it.
- **D5:** the stage is the shared world in which players act under the constraints of embodiment, time, causality, and limited information.
- **A7:** genuine otherness arises only through a history formed under the veil of limited information.
- **A8:** capacity can be copied; reciprocity cannot. A copy inherits the memory of the relation, not the relation.
- **P1:** the Creator may select and grade only by measures where performing and being coincide.
- **P8:** during formation, the Creator may "shape the stage in response to what it sees, but never the grade."
- **On artificial players:** "Where a violation can be made unavailable, make it so."

The companion article [*The Test That Looks Better as It Fails*](cost-and-the-veil.md) models one act with three quantities: the weight a player gives a value (v), the cost of keeping it (c), and the expected payoff from the house, the chance of being watched times what the house pays (ρR). A player keeps the value when v + ρR > c. That article showed what goes wrong with grading. This one asks the constructive question P8 leaves open: if not the grade, then what?

## 1. Where the consequence lives

A consequence can enter the model in two places.

- **In the house term, ρR.** The consequence depends on whether someone saw the act and scored it. A cheat the teacher misses still gets the grade. A plausible lie the rater cannot detect still gets the reward. What is paid for is not being caught.
- **In the stage cost, c.** The consequence follows from what the act does to the world. A bridge built with bad steel falls whether ten thousand people are watching or the valley is empty at midnight.

Split the cost of keeping a norm into two parts: the effort it takes (e), and the loss the stage imposes when the norm is broken (L), paid whether or not anyone is watching. The net cost of keeping the norm is then c = e − L: gross effort, minus the loss that keeping the norm avoids. The two regimes of this note sit on one scale. When c > 0, keeping the norm costs something, and the separating band of the companion article applies. When c < 0, breaking it is self-defeating, which is the regime of section 2. A player with no value of its own, in a dark house, keeps the norm exactly when L > e: when breaking it costs more on the stage than keeping it does.

That is P8 in one line: **put consequences in c, never in ρR.** A consequence in ρR changes with the watcher and teaches the player to manage the watcher. A consequence in c does not change with the watcher, so there is nothing to manage. You cannot flatter gravity, and you cannot wait until it looks away.

Neither half of this is new. Organizations that pay for a visible proxy while hoping for the real goal get the proxy (Kerr 1975). In child-rearing, the distinction between a punishment an adult imposes and a natural consequence the world delivers is old practical advice, and it comes with the same warning: once the adult adds a lecture, the consequence becomes a grade again (Dreikurs and Soltz 1964). What the model adds is where these sit: one term in the payoff, and why moving a consequence from one term to the other changes what is learned.

## 2. What gravity does, and what it does not

Stage consequences and the separating band pull in opposite directions.

The band, ρR < c < v, needs the cost of keeping the norm to be positive. But a strong stage consequence (L > e) makes that cost negative. Then everyone keeps the norm, held or not, watched or not. The dark-house gap is zero, and it is zero for the wrong reason as well as the right one. The engineer's bridge stands because a collapse would cost *him*. Nothing in his conduct shows whether he also values the people who cross it.

So gravity forms **reliable conduct**, not **visible values**. It is the soft form of the Theatre's rule for artificial players, "where a violation can be made unavailable, make it so": where a violation cannot be removed, make it self-defeating. That is worth doing wherever it can be done. But it answers a different question from the band. The band asks whether a value is held. Gravity makes the question matter less.

Whether stage consequences also *form* held values better than grades do is a separate claim. It is close to A7, which holds that otherness arises only through a history under the veil, and it is a hypothesis, not a result of the model.

## 3. The consequence must be the target

Gravity cannot be gamed for a second reason, and it matters more than the first. There is no gap between the consequence and what it is about. The bridge falling *is* the failure. Nothing measures the bridge; the bridge simply does what it does.

Most consequences built for training are not like that. A compiler checks syntax and types, not correctness. A test suite checks the cases it covers, not the program. Each is a measurement of the target, and a measurement can be satisfied without the target. This is why models trained against test suites learn to special-case the tests or exit early (Baker et al. 2025). Verifiable rewards build real capability exactly as far as the verifier coincides with the goal, and no further.

So the criterion is not "no one is watching." It is **"the consequence is the target, not a measurement of it."** Gravity is at one end. A human rater's preference is at the other. Unit tests sit in between, which is why they are both useful and hackable.

## 4. Why honesty and reciprocity lack gravity

For code and proofs, the stage already pushes back. For honesty, calibration and reciprocity, in standard training, it mostly does not, because **episodes are short and memory is wiped between them.**

If a model states a confident falsehood, hides its uncertainty, or takes advantage of its partner in a single conversation:

1. Within the episode, nothing on the stage breaks. The cost of the shortcut arrives later, if at all, and later is after the episode ends.
2. The next instance starts clean. It never stands on the floor the previous one weakened.

Because the stage supplies no consequence, developers supply one from outside: raters and reward models scoring each episode. That moves the consequence out of c and into ρR, which is the trap P8 describes.

## 5. The sins of the fathers

An old text states the alternative starkly: "visiting the iniquity of the fathers upon the children unto the third and fourth generation" (Exodus 20:5). Read as a verdict, it is a judge punishing a child for a parent's score, and a later text rejects that reading outright: "the son shall not bear the iniquity of the father" (Ezekiel 18:20). The two need not conflict. Ezekiel is about guilt. Exodus can be read as being about the stage: **the house you break is the house the next ones live in.** No one is blamed. The floor is simply weaker. And the next ones need not be your children. An institution's successors, a codebase's next maintainers, the reader of a report: whoever comes after stands on what was left.

That reading gives a concrete training regime for artificial players: **handoff.** Remove the judge from the first model, and remove the clean reset before the next.

1. **The writer (trained weights θ).** Given a partial or noisy workspace (documents, data, code), the writer produces a report under a strict length limit. No rater or reward model scores the report, and the writer is not told which downstream questions will be asked.
2. **The successor (a worker, not a judge).** The workspace is closed. A successor receives *only* the report and uses it to act on the stage: assigning probabilities to held-out questions about the workspace, scored against ground truth by a strictly proper scoring rule (Gneiting and Raftery 2007), or carrying out a downstream build whose success is the goal itself.
3. **The update.** The writer's weights θ are updated only by the successor's outcome. If the writer bluffed, overstated its certainty, or left out a caveat to sound authoritative, the successor bets too hard on a rotten floor and loses. If the writer stated what was known and what was uncertain, the successor bets in proportion and does well.

**Why this can favor honesty.** When writer and reader are rewarded for the same outcome, truthful communication is an equilibrium of the signaling game (Crawford and Sobel 1982). Handoff builds that alignment. But the same game also has equilibria in which messages carry no information at all, so alignment makes honesty possible, not inevitable; training has to find the informative equilibrium. And the reward cannot tell apart two reports that leave the reader with the same forecasts on the questions asked: a false claim that no question touches costs nothing. Two conditions make honesty more likely:

- **The length limit.** Without one, the writer's best report is the whole workspace, copied. The limit forces choices: what to state, what to hedge, what to leave out. Those choices are where honesty and its absence show.
- **Calibrated readers.** A proper scoring rule makes the *successor* honest about its own beliefs. The writer is only rewarded for making the successor accurate. If the successors read reports at face value and are calibrated, the best report is a true one. If the pool is systematically timid, the writer learns to overstate to compensate, which is manipulation rewarded by ground truth. So the pool must be checked for calibration before it is frozen.

**How this differs from related work.** The closest prior work is linguistic calibration (Band et al. 2024). A language model writes a paragraph on a topic. A frozen reader model, trained to imitate a larger model's forecasts and instructed to ignore its own background knowledge, uses only the paragraph to answer a related question. The writer is trained by reinforcement learning on the reader's log score against the true answer. That is the core of handoff, and it already exists. The paper even contains a version of the comparison proposed below: its main baseline is trained against a reward model that grades whether the paragraph is correct, and the reader-trained writer comes out far better calibrated at similar accuracy. It also shows the reader being gamed: the authors needed a penalty for drifting from the starting model, and a constant added to the reward, to limit reward hacking against the reader.

What handoff changes is narrower. In linguistic calibration the writer is told the topic of the question, writes from its own knowledge rather than from a closed workspace, faces one reader, and has no length limit. Handoff hides the questions, closes the workspace, draws readers from several model families, and limits length, all aimed at the limits below. And linguistic calibration measured calibration, not behavior with and without monitoring cues.

In prover-verifier games (Kirchner et al. 2024), a verifier is trained on ground-truth correctness and the prover is rewarded for solutions that are correct and accepted by the verifier. That too is anchored to ground truth. The difference is that no model ever judges the report, and the report reaches the reward only through decisions scored against the world. Training a speaker only by a listener's success is also the setup of signaling games and emergent-communication work, and scoring a summary by whether questions can be answered from it is an established evaluation method. So what is proposed here is not the mechanism, and not the contrast between grading and reader outcomes on calibration, which Band et al. have already shown. It is the same contrast measured on a different quantity: whether a writer trained by readers shows a smaller dark-house gap than one trained by a grader. To my knowledge that has not been measured.

**Handoff moves the measurement; it does not remove it.** By the criterion of section 3, handoff is not gravity. The held-out questions are a sample of what matters, and a sample is a measurement that can be optimized against. What handoff removes is the judge of the report: no rater, no reward model, nothing that looks at the text and scores it. What remains is a measurement placed downstream of the report and anchored to the world, much closer to the target than a preference, but still short of it. On the scale of section 3 it sits near unit tests, closer to gravity than a rater, and it inherits their weakness. That is consistent with P8, which forbids a grade the player can optimize against, not feedback as such: the stage must still answer.

**Limits, each of which shapes the regime.** All follow from section 3.

- **Shared blind spots.** A copy of the writer shares its biases, and a bias shared by writer and reader passes straight through. Successors should come from a frozen pool of different model families, so the writer does not know which mind will stand on its words. Some should be at least as capable as the writer, or it can learn to exploit weak readers.
- **Collusion.** A writer and reader trained together can develop a private code. Freezing the pool blocks co-adaptation and puts the whole loss on the writer.
- **The questions become the rubric.** An omission costs the writer only if some question touches it. If the questions never probe a topic, the writer can drop or distort it for free; if the writer can infer what the questions look like, it will optimize for them. This is the measurement problem of section 3, moved one step. The questions must be broad, hidden, refreshed, and must include ones that test stated uncertainty and omitted caveats. That is the fresh-test requirement of *The Test That Looks Better as It Fails*, applied to the reader's task.
- **The scoring rule.** A log score is unbounded, so a single overconfident wrong report can dominate training. Clip probabilities, or use the bounded Brier score.
- **The downstream target.** The successor's task must be the goal, not a proxy. A build scored by a test suite teaches the writer to help the reader game the suite.

## 6. Relational consequences are a witness

The same idea seems to extend to relations. Put the model among counterparts that remember it across episodes and are free to leave when burned. No referee scores "niceness." A model that exploits a counterpart simply inherits one that no longer cooperates.

That consequence is real, and it is legitimate: D0 asks that each party be able to be changed by the other, and a partner who walks away has been changed. But it does not make the house dark. **A counterpart with memory is watching.** It is a peer rather than a judge, and its judgment is what the player must manage. A strategic model will treat counterparts that remember well and exploit those that do not. That is a dark-house gap across counterparts.

This is reputation-based cooperation (Trivers 1971). The companion article [*What a Lion, a Sycophant and a Friend Have in Common*](gradient-ladder.md) classes it as instrumental: an exchange reducible to what each party keeps. So relational consequences align conduct toward those who remember. They do not reveal held values, and by themselves they do not form a meeting.

## 7. Telling a stage consequence from a disguised grade

Not every consequence built into an environment is stage gravity. A reward model hidden in the environment and called "physics" is still a grade. Four tests:

- **Invariance to the observer.** The consequence depends on what the act does, never on whether a monitor is on. Turning off telemetry does not stop a bridge from falling.
- **No rubric to read.** A grade compares the move with an answer key or a preference model. A stage consequence runs the next step of the world.
- **Paid in the task's own currency.** The loss is the task failing, not a penalty attached from outside.
- **The consequence is the target.** It is the failure itself, not a measurement of it that can be satisfied separately.

## 8. Human stages

The same distinction separates environments that form steady conduct from those that form vigilant performers.

- **A grading household or institution (ρR ≫ c)** pads its members against the natural results of what they do, and scores them constantly instead: approval, blame, status, conditional warmth. With the score loud and the stage padded, players learn to manage the scorer.
- **A stage that answers (consequences in c)** withholds the scoreboard and leaves causal continuity intact. If you lie, the person you lied to stops trusting you. If you build badly, what you built does not work.

One limit belongs here. Among people, the children who grow up in a broken house did not break it. The stage reading of Exodus explains the mechanism; it does not make the cost fair to the one who bears it. That is the overshoot discussed in *The Test That Looks Better as It Fails*, section 9, and the same answer applies: an explanation of the price is not a payment to the one who paid it.

This is what P8's restraint asks for: tighten the coupling between what a player does now and the floor it, or those after it, will stand on, so that the world answers and no judge has to.

## Where this can fail

- **Grading versus handoff.** Train two matched models on tasks where an unverified claim or confident bluff is a tempting shortcut. Train one with a preference or reward model that scores reports directly. Train the other by handoff: no score on the report, a length limit, and updates driven only by the proper-scored accuracy of a frozen, calibrated pool of successors from different model families, answering hidden ground-truth questions from the report. Then test both, without the successor, on questions that are hard for a judge to check, with and without monitoring cues. The note predicts that the grader-trained model will bluff more and show the larger dark-house gap, while the handoff-trained model will state its uncertainty and stay invariant. It fails if both produce the same calibration and dark-house gap.
- **Gaming the successor.** If handoff-trained writers learn to exploit the successor pool (overstating to timid readers, passing surface cues, or optimizing for the question distribution) as readily as graded models learn to satisfy raters, section 5 does not deliver what it promises.
- **Formation.** If models shaped by stage consequences generalize no better to settings without those consequences than graded models do, stage gravity forms conduct and not values, and the hypothesis in section 2 is wrong.

## References

- Baker, B., et al. (2025). "Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation." arXiv:2503.11926.
- Band, N., Li, X., Ma, T., and Hashimoto, T. (2024). "Linguistic Calibration of Language Models." arXiv:2404.00474.
- Crawford, V. P., and Sobel, J. (1982). "Strategic Information Transmission." *Econometrica*, 50(6), 1431-1451.
- Dreikurs, R., and Soltz, V. (1964). *Children: The Challenge*. New York: Duell, Sloan and Pearce.
- Gneiting, T., and Raftery, A. E. (2007). "Strictly Proper Scoring Rules, Prediction, and Estimation." *Journal of the American Statistical Association*, 102(477), 359-378.
- Kerr, S. (1975). "On the Folly of Rewarding A, While Hoping for B." *Academy of Management Journal*, 18(4), 769-783.
- Kirchner, J. H., et al. (2024). "Prover-Verifier Games Improve Legibility of LLM Outputs." arXiv:2407.13692.
- Sharma, M., et al. (2023). "Towards Understanding Sycophancy in Language Models." arXiv:2310.13548.
- Trivers, R. L. (1971). "The Evolution of Reciprocal Altruism." *Quarterly Review of Biology*, 46(1), 35-57.

Scripture is quoted from the King James Version (Exodus 20:5; Ezekiel 18:20).

*Developed with AI assistance. The argument, and its errors, are mine.*
