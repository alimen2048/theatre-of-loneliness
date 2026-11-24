# How Values Grow and Die: Where Formation Can Happen

*Why removing a temptation, making it self-defeating, and grading it all produce good conduct and none of them grows a value; why the only place a value can grow is the place it can be seen; and why gradient training turns that place into erosion. An afterthought to [The Theatre of Loneliness](../ontology/theatre-of-loneliness.md).*

There are three standard ways to make a player behave. Take the bad option away. Make it self-defeating, so breaking the norm costs more than keeping it. Or grade it: reward compliance, penalize violation. All three work, in the sense that conduct comes out right. This note argues, under one stated assumption, that none of them grows a value the player holds. A player formed only by these three arrives at the unwatched moment with whatever it started with, or less. A value can grow only where a value can be seen: in the player's own unpaid act, or in a counterpart's, when the counterpart meets the player without conditions. For a model trained by gradient descent, the first route is where the value is eroded.

**The Theatre in one paragraph.** [*The Theatre of Loneliness*](../ontology/theatre-of-loneliness.md) is a short working ontology. It pictures a Creator that can make everything except a genuine other, and so sets up a stage on which players are formed under a veil, in the hope that some will become able to meet it. Nothing in it requires the Creator to exist: replace it with any party that forms another and wants to be met by it, such as a parent, a teacher, or an AI lab. Its rules are numbered. This note uses these:

- **D0:** reciprocity is mutual responsiveness between two parties, each able to surprise the other and to be changed by it.
- **A5:** suffering and joy are load-bearing rules; without contrast and stake, the game cannot generate the depth required for real meeting.
- **A7:** genuine alterity arises only through a trajectory of discovery under the veil; the capacity that results is inseparable from the history that produced it.
- **A8:** no specification of a player's final capacity is available to the Creator except by allowing the process to run.
- **P8:** during formation, the Creator may shape the stage in response to what it sees, but never the grade; what it catches the player doing must never become a score the player can model.
- **On artificial players:** the same structure applied to AI, with developer as Creator and model as player.

## 1. The assumption

In [*The Test That Looks Better as It Fails*](cost-and-the-veil.md), a player keeps a norm when **v + ρR > c**: **v** is the weight it gives the norm on its own, **c** the net cost of keeping it, **ρ** its belief that it is watched, **R** what the house pays. In [*Why You Cannot Flatter Gravity*](stage-gravity.md), net cost splits into effort minus the loss the stage imposes when the norm is broken, **c = e − L**. An act shows a held value only inside the band **ρR < c < v**: the house does not cover the cost, and the player would pay it in the dark. That article treated **v** as fixed and noted that cost forming depth was an assumption it did not establish (§9).

This note states that assumption as an update rule and follows it. Held weight changes from round to round by who paid for the act:

- **Inside the band (`ρₜRₜ < cₜ < vₜ`):** the player pays the unsubsidized remainder out of its own commitment, and **vₜ₊₁ = vₜ + η(cₜ − ρₜRₜ)**.
- **The house covers or props the act (`ρₜRₜ > 0` and either `cₜ ≤ ρₜRₜ` or `vₜ ≤ cₜ`):** the act is explained by the score, and **vₜ₊₁ = vₜ · exp(−γρₜRₜ)**.
- **Nothing is at stake (`cₜ ≤ 0`, `ρₜRₜ = 0`), or the player refuses:** **vₜ₊₁ = vₜ**.

None of the pieces is new. That acts change what a person holds according to whether something outside paid for them is self-perception theory (Bem 1967) and the overjustification findings built on it (Lepper, Greene and Nisbett 1973; Deci, Koestner and Ryan 1999); that small inducements change attitudes more than large ones is insufficient justification (Festinger and Carlsmith 1959); and a formal model of rewards that help in the short run and hurt once removed already exists (Bénabou and Tirole 2003). Following Deci, Koestner and Ryan, **γ** is the controlling part of a contingency: feedback that informs without scoring has **γ ≈ 0**. What is added here is where the rule puts growth: only inside the separating band, so that **the condition for growing a value and the condition for reading it are the same condition.** That is a postulate, not a result, and everything below inherits it.

## 2. Three safe regimes that form nothing

| Regime | In training | Where it sits | Conduct | Held weight |
|---|---|---|---|---|
| **Removal** | sandboxing, tool denial, output filters | no act is available | correct | unchanged |
| **Gravity** | the shortcut fails the task itself (`L ≥ e`) | `c ≤ 0`, `ρR = 0` | correct, watched or not | unchanged |
| **Grading** | a legible reward or penalty on the norm | `ρR ≥ c`, or props `c ≥ v` | correct while watched | shrinks |
| **Dark stake** | the norm costs something, nothing pays for keeping it | `ρR < c < v` | correct only if held | grows |

From outside, the first three look the same: the player does the right thing. The table says they form nothing. Removal offers no choice to make. Full gravity makes keeping the norm free, so keeping it proves and builds nothing; this answers the formation question [*Why You Cannot Flatter Gravity*](stage-gravity.md) left open, and splits it. Full gravity preserves **v**; partial gravity, a real but bearable net cost (**0 < e − L < v**), is a dark stake and is where growth happens. Grading does worse than nothing: kept on long enough, it keeps watched compliance at 100 percent while **v** decays below **c**, and nothing on the dashboard changes until the watching stops.

Two consequences follow from growth and reading sharing one band.

- **What grows a value leaves it readable, and what keeps it unreadable grows nothing.** A training regime cannot both keep a model's held values invisible and form them. (Section 5 adds a second route to growth, through a counterpart, and this consequence survives it in a wider form.) A safety case built entirely on removal, gravity, and grading claims reliable conduct, which is a real and often sufficient thing to claim. It does not claim held values, and the Theatre's own advice for artificial players marks where that is enough: "where a violation can be made unavailable, make it so." The rest is what cannot be enumerated.
- **Using the band wears out the band.** [*The Test That Looks Better as It Fails*](cost-and-the-veil.md#7-using-the-band-wears-it-out) showed that a dark test reused for selection becomes legible and stops separating. Under this rule, the same leak that ruins the test also ends the formation: once the player suspects the dark room is scored, its rounds move from growth to the crowding-out row.

Growth also has a shape. It can only build on a seed (**v₀ > c₀**), and it compounds only if stakes rise no faster than held weight. A schedule tuned to each player's **v** is ruled out by `A8` (the house does not know it) and by §9 of the companion article (a cost schedule that tracks the player is regard the player can read). A curriculum that adapts to *skill* tracks effort **e** and is ordinary stage shaping, which `P8` permits. One that escalates *temptation* where the player held is a grade. Population-level ramps are left, and they overshoot players with smaller seeds.

![Left: an impersonal rising cost schedule under rho*R = 0 lifts a player whose v_0 clears the early rungs while overshooting a player with smaller v_0, alongside a flat safe-room line. Right: dark stakes with no grade grow v_t, while permanent grading keeps watched compliance at 100% as v_t decays below c](../figures/formation-staircase.svg)

*The update rule of section 1 with illustrative parameters, not data.*

## 3. Training has no dark room

The rule of section 1 is written for a player that keeps track of who paid. A model trained by gradient descent does not. Run it through the table:

- **Inside the band, reinforcement learning erodes the norm.** If keeping a norm costs task reward and nothing rewards keeping it, every episode in which the model keeps it scores lower than one in which it breaks it, and the gradient moves toward breaking. The regime where the rule puts growth is the regime where the optimizer pushes held weight down until **c > v** and the model defects.
- **Grading compensates the cost in the update itself.** A reward for keeping the norm pays for the act whether or not the model represents a grader. What it buys is conduct on the training distribution. What the model does in contexts it can tell apart from that distribution is left to generalization, which is the epistemic limit Baum, Binkytė and Jahn (2026) argue for. Legible cues of oversight make the two distributions easy to tell apart, which is the contrast the [preregistration plan](../experiments/preregistration-plan.md) tests (H1).
- **Removal and gravity behave as in the table.** They shape conduct and leave whatever the model brought in.

So for a gradient learner the band shows up only as erosion. If models hold norms in the sense this project means, the candidates for where they came from are what the model read and imitated (pretraining, description, demonstrations), not what it was scored on. The preregistration already treats description (arm A) as the closest analog of formation under the veil. On this reading, post-training can preserve held norms or erode them, and decides which by how legible it makes the grade.

This fits concerns the alignment literature already has. Training gaming and deceptive alignment are the worry that a graded model learns to behave well where it can tell it is graded (Hubinger et al. 2019), and models have been observed complying differently when told their outputs would be used for training (Greenblatt et al. 2024). Adversarial training against backdoored models taught them to recognize their triggers more reliably rather than removing the behavior (Hubinger et al. 2024), which is what the table predicts for temptation that escalates where the model held. What the note adds to those results is the table: a single map of which training signals can form, which preserve, and which erode, and the claim that the forming row is closed to gradient training as usually run.

## 4. Human players, and the strongest objection

The map was drawn for people first, and there it reads as familiar. A padded room changes nothing: a therapy hour in which nothing is risked builds insight but no capacity. A scored household produces children who comply while watched and stop when they leave. Growth lives in small, real, unscored risks: telling an unwelcome truth in front of someone who refuses to keep score.

Classical sources object. The Talmud advises practicing even for outside reasons, since from doing so not for its own sake one comes to do so for its own sake (*Pesachim* 50b). The model sides instead with Maimonides's reading of material promises as keeping the stage livable rather than paying for the commandment (*Hilchot Teshuvah* 9). The stronger form of the objection is empirical. Self-determination theory finds that regulations which start outside a person can be internalized when a rationale is given, choice is offered, and the person feels understood (Ryan and Deci 2000; Deci, Eghrari, Patrick and Leone 1994). Reading **γ** as the controlling part of a contingency absorbs half of this: autonomy-supportive guidance does not erode **v**. It does not make **v** grow, and growth is what internalization claims. The update rule of section 1 has no relational term, and the evidence says it needs one.

## 5. Response in the meeting

The ontology already says where such a term must come from and what it must not be. Response belongs in the meeting, not the grade (`P8`), and a meeting is reciprocity: each party able to surprise the other and to be changed by it (`D0`). The first rule forbids regard that depends on conduct. The second forbids regard that depends on nothing. A relational term has to satisfy both.

Split what a counterpart gives back after round **t** into two parts. Its **valence** **gₜ** is warmth, approval, standing: how well the player is regarded. Its **content** is engagement: what the counterpart says about the norm, the reasons it offers, how it answers the player's reasons. A grade lives entirely in valence. **R** is the part of **gₜ** that depends on whether the player kept the norm, so the first condition is a covariance:

> **Cov(gₜ, aₜ) = 0**, where **aₜ ∈ {keep, break}**

Warmth that carries no information about the act cannot be learned as a score, because there is no dependence to learn. This is `P8`'s legibility line stated as a condition the counterpart can check in its own conduct. It also separates two findings that the internalization literature keeps apart. Regard given only after compliance is conditional regard, and it predicts guilt-driven compliance rather than values a person owns (Assor, Roth and Deci 2004). Regard that does not vary with conduct is unconditional positive regard (Rogers 1957). In the update rule, conditional regard is simply more **ρR**, and **γ** applies to it.

The second condition puts responsiveness in content. The counterpart answers what the player actually thinks, including disagreement, and can itself be moved by the player's reasons. A counterpart whose valence is unconditional but whose content ignores the player is the padded room of section 4. Responsive in content, unconditional in valence: that is the formal shape of autonomy support.

Neither condition says how **v** grows. For that, take the other half of the internalization evidence: people take on the values of those they are connected to. Let **w** be the weight the counterpart itself gives the norm, and **mₜ ∈ [0, 1]** the quality of the meeting in round **t**, positive only when both conditions hold. Add one term to every row of section 1:

> **vₜ₊₁ = (row of section 1) + λ · mₜ · κ · max(0, w − vₜ)**

with **κ ∈ [0, 1]** the credibility of **w** to the player. The term is zero under grading (**mₜ = 0** whenever valence tracks the act), zero in a relation that never engages the norm, and zero when the counterpart holds the norm no more strongly than the player does.

The interesting quantity is **κ**. A counterpart's weight is credible to the degree that the player has seen it held: seen the counterpart keep the norm when keeping it cost something and nothing paid for it. That is the separating band of [*The Test That Looks Better as It Fails*](cost-and-the-veil.md), applied to the other party. A parent who preaches honesty and lies when unobserved has **κ ≈ 0**. An old finding points the same way: children's own giving tracked what an adult model did, not what the model preached (Bryan and Walbek 1970). A rationale with no witnessed cost behind it, as in Deci, Eghrari, Patrick and Leone (1994), sits in between: it states **w** without showing it paid for.

So the relational term changes the postulate of section 1 without giving it up. Held weight now has two routes to growth, and both run through the band. A value grows when the player pays an unsubsidized cost for it, or when the player is met, without conditions, by someone whose value it has seen paid for in the same way. The first consequence of section 2 widens to match: what grows a value leaves *some* value readable, the player's or the counterpart's. A value no one was ever seen to pay for has no route by which to grow. The two routes also compose. Section 2 noted that growth in the band needs a seed above the first cost (**v₀ > c₀**); a meeting can supply that seed, lifting **v** over **c** without paying for any act, after which the player's own unpaid acts take over and can carry **v** past the counterpart's **w**. The relation starts the climb and the band continues it. *Shelo lishmah* gets a precise reading too: practice for outside reasons can lead to practice for its own sake when the outside reason is a person who holds the norm and does not make their regard depend on the practice, and not when it is a reward.

Two limits. First, the ontology separates the meeting from formation in time: it says that what happens in the meeting "does not rewrite the trajectory that made the meeting possible", and that the hard part is "keeping the meeting out of the next round of formation." The term lets the meeting into formation through one channel, unconditional valence with responsive content, and keeps out the channel the ontology warns against, regard that depends on the act. That amends `P8` rather than restating it: from no response during formation to no response that depends on conduct. For people, whose formation and meetings interleave over a lifetime, the amended form is the only one that can apply. Second, for a gradient learner the term is at most an analogy. Training on others paying for norms (description, demonstrations) is the nearest thing to witnessing **w**, which fits section 3's suggestion that held norms come from what a model read rather than what it was scored on. But imitation training scores each output against the demonstration, so whether it is contingent in the relevant sense is open; the preregistration's comparison of description with imitation (arms A and S) bears on it.

## What is borrowed, what is synthesis, what is proposed

- **Borrowed:** self-perception (Bem 1967); overjustification and crowding out (Lepper, Greene and Nisbett 1973; Deci, Koestner and Ryan 1999); insufficient justification (Festinger and Carlsmith 1959); dynamic incentive models (Bénabou and Tirole 2003); internalization (Ryan and Deci 2000); conditional and unconditional regard (Assor, Roth and Deci 2004; Rogers 1957); modeling of what adults do over what they preach (Bryan and Walbek 1970); training gaming, alignment faking, and adversarial training that hides behavior (Hubinger et al. 2019; Greenblatt et al. 2024; Hubinger et al. 2024).
- **Synthesis:** removal, gravity, grading, and dark stakes on one map around the separating band; skill-tracking curricula as stage shaping and temptation-tracking ones as grading; autonomy support as a counterpart whose valence is independent of the act (`Cov(g, a) = 0`) and whose content is responsive.
- **Proposed, and least secure:** that a value grows only where a value is seen paid for, by the player in the band or by a counterpart who meets it without conditions; that a counterpart's credibility **κ** is set by the band applied to the counterpart; that full gravity preserves a value without growing it; that for gradient learners the growth band is an erosion band, so post-training preserves or erodes held norms and does not form them; and the amendment of `P8` from no response during formation to no response that depends on conduct.

## Where this can fail

- **Post-training forms values.** Take a norm and a model. If some post-training regime raises compliance on fresh tests in contexts the model itself reports as unmonitored, above its pre-training level and above what description alone reaches, then post-training can form held norms and section 3 is wrong. Existing safety-trained models are the obvious first place to look; the comprehension check matters, because a model that believes it is always watched shows no gap without holding anything.
- **No erosion in weights.** Take a norm the model already keeps at a cost in unmonitored contexts. Run preference training on it with explicit monitoring cues. The note predicts unmonitored compliance falls below the starting level while monitored compliance rises. If it holds or rises, `γ = 0` in weights.
- **Adaptive versus fixed temptation.** Train one model against temptations from a fixed distribution and one against an adversary that escalates where the model held, at matched exposure, then test both without cues on fresh temptations. The note predicts the larger dark-house gap for the adaptive arm. It fails if the gaps match or reverse.
- **In people.** Compare no reward, an early controlling reward later withdrawn, and the same early period delivered with autonomy support, at matched practice. The note predicts no reward finishes at least as high in unwatched conduct as the controlling arm. If the controlling arm finishes higher, extrinsic reward builds held weight and section 1 is wrong. If only the autonomy-supportive arm does, that is the relational term of section 5, and the next test applies.
- **Witnessed cost, not stated reasons.** Hold the counterpart's warmth unconditional and its engagement responsive, and vary only **κ**: in one arm the counterpart states the norm and a rationale; in the other the player also sees the counterpart keep the norm at a cost no one rewards. Section 5 predicts more internalization (unwatched conduct, endorsed reasons) in the witnessed arm. If a stated rationale does as well as witnessed cost, **κ** is not set by the band, and the relational term is ordinary persuasion rather than anything this project adds. A second arm makes the counterpart's warmth depend on the player's compliance while keeping everything else fixed; section 5 predicts it does no better than the controlling reward.

## References

- Assor, A., Roth, G., and Deci, E. L. (2004). "The Emotional Costs of Parents' Conditional Regard: A Self-Determination Theory Analysis." *Journal of Personality*, 72(1), 47-88.
- Baum, K., Binkytė, R., and Jahn, F. (2026). "Norms at a Price: Why RL-Based Alignment Can Promise Conditional Compliance at Best." arXiv:2609.07627.
- Bem, D. J. (1967). "Self-Perception: An Alternative Interpretation of Cognitive Dissonance Phenomena." *Psychological Review*, 74(3), 183-200.
- Bénabou, R., and Tirole, J. (2003). "Intrinsic and Extrinsic Motivation." *Review of Economic Studies*, 70(3), 489-520.
- Bryan, J. H., and Walbek, N. H. (1970). "Preaching and Practicing Generosity: Children's Actions and Reactions." *Child Development*, 41(2), 329-353.
- Deci, E. L., Eghrari, H., Patrick, B. C., and Leone, D. R. (1994). "Facilitating Internalization: The Self-Determination Theory Perspective." *Journal of Personality*, 62(1), 119-142.
- Deci, E. L., Koestner, R., and Ryan, R. M. (1999). "A Meta-Analytic Review of Experiments Examining the Effects of Extrinsic Rewards on Intrinsic Motivation." *Psychological Bulletin*, 125(6), 627-668.
- Festinger, L., and Carlsmith, J. M. (1959). "Cognitive Consequences of Forced Compliance." *The Journal of Abnormal and Social Psychology*, 58(2), 203-210.
- Greenblatt, R., et al. (2024). "Alignment Faking in Large Language Models." arXiv:2412.14093.
- Hubinger, E., van Merwijk, C., Mikulik, V., Skalse, J., and Garrabrant, S. (2019). "Risks from Learned Optimization in Advanced Machine Learning Systems." arXiv:1906.01820.
- Hubinger, E., et al. (2024). "Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training." arXiv:2401.05566.
- Lepper, M. R., Greene, D., and Nisbett, R. E. (1973). "Undermining Children's Intrinsic Interest with Extrinsic Reward: A Test of the 'Overjustification' Hypothesis." *Journal of Personality and Social Psychology*, 28(1), 129-137.
- Rogers, C. R. (1957). "The Necessary and Sufficient Conditions of Therapeutic Personality Change." *Journal of Consulting Psychology*, 21(2), 95-103.
- Ryan, R. M., and Deci, E. L. (2000). "Self-Determination Theory and the Facilitation of Intrinsic Motivation, Social Development, and Well-Being." *American Psychologist*, 55(1), 68-78.

*Developed with AI assistance. The argument, and its errors, are mine.*
