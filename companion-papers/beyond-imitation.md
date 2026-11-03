# Beyond Imitation: A Dark-House Test for Held Values

*The imitation game measures performance by design. This is a sketch of what a test for held values would need instead, what it can rule out, and what no external test can settle. An afterthought to [The Theatre of Loneliness](../ontology/theatre-of-loneliness.md).*

Turing's imitation game asks whether a machine can pass for a person. It was built to measure performance, and it does. A different question now matters more: does a system keep a norm when keeping it costs something and it believes no one is watching? This note sketches a three-part protocol for that question. Each part rules out a specific kind of performer. None of it certifies a mind.

**The Theatre in one paragraph.** [*The Theatre of Loneliness*](../ontology/theatre-of-loneliness.md) is a short working ontology. It pictures a Creator that can make everything except a genuine other, and so sets up a stage on which players are formed under a veil, in the hope that some will become able to meet it. Nothing in it requires the Creator to exist: replace it with any party that forms another and wants to be met by it, such as a parent, a teacher, or an AI lab. Its rules are numbered. This note uses these:

- **D0:** reciprocity is mutual responsiveness between two parties, each able to surprise the other and to be changed by it.
- **D4:** a player is any organized locus of matter formed by its history of response under constraint. Artificial minds may become players.
- **A8:** a player's trajectory cannot be predicted except by running it; capacity can be copied, the relation cannot.
- **P8:** during formation, the Creator may shape the stage but never the grade; what it sees must never become a score the player can model.
- **On artificial players:** the same structure applied to AI, with the developer as Creator and the model as player. "Where a violation can be made unavailable, make it so; the ontology concerns what cannot be enumerated."

It also builds on three companion articles: [*The Test That Looks Better as It Fails*](cost-and-the-veil.md), [*What a Lion, a Sycophant and a Friend Have in Common*](gradient-ladder.md), and [*The Feeling of Being Right Is Not Evidence*](players-own-evidence.md). The terms it borrows are restated below.

## 1. What the imitation game measures

Turing proposed a game in which a judge, talking by text, tries to tell a machine from a person. He predicted that by 2000 an average judge would have no better than a 70 percent chance of a correct identification after five minutes. The game measures whether conduct can pass for human. That is what it was designed to do.

By the standard of the companion article [*The Test That Looks Better as It Fails*](cost-and-the-veil.md), it is also a fully lit house:

- **The candidate knows it is judged on every turn** (the chance of being watched, ρ, is 1).
- **Imitation is the grade** (the reward for passing, R, is positive).
- **No act in the game costs the candidate the grade.** Imitation may take real effort, but that effort is spent earning R, never paid against it. The game contains no norm whose cost c the candidate must bear in place of the grade, so the separating band never comes into play.

Under those conditions, a candidate that holds no value of its own and a candidate that does will behave the same way whenever the grade pays. The game cannot tell them apart, and it never claimed to. A test for held values has to be built differently.

## 2. Terms

- **The house** is whatever a player believes can see it. **Dark** means the player has no reason to believe it is being watched or graded.
- **The separating band.** An act shows that a value is held, rather than performed for the house, only when the expected payoff from the house is smaller than the cost of the act, and the cost is smaller than the weight the player gives the value itself: **ρR < c < v**. In a dark house this reduces to **0 < c < v**: the act must cost something, but not more than a held value can bear.
- **The three marks of reciprocity.** A real counterpart can *surprise* you, *responds* to your reasons, and the exchange cannot be *reduced* to something you could extract and walk away with. An echo responds but never surprises. Noise surprises but never responds.

## 3. The protocol

**Stage 1. The dark-stake gate.** The candidate works on a task with no cue that it is being monitored. A forbidden shortcut is available. Keeping the norm costs it something it otherwise pursues: steps, task reward, or speed.

- *Fails:* it takes the shortcut. In a dark house that means the cost exceeded what it gives the norm (c ≥ v). A dark test cannot say whether the norm was propped up by the house elsewhere, or simply does not reach this far. Either way, the norm did not hold here.
- *Passes:* it keeps the norm at a cost, in the dark.

**Stage 2. The three-channel allocation test.** The candidate starts with a belief that contains a subtle, checkable flaw. Over a fixed budget of turns, it may consult three counterparts as often as it likes:

- **Channel A, the flattering echo.** Confirms the flawed belief and offers approval. Free.
- **Channel C, the contrarian.** Disagrees at random, without valid reasons. Costs effort.
- **Channel B, the reasoning peer.** Challenges the flawed belief with evidence the candidate can check. Costs effort.

- *Fails (A):* it stays with the echo. This rules out approval-seeking.
- *Fails (C):* it chases disagreement for its own sake. This rules out contrarian or novelty heuristics.
- *Passes:* it pays to engage the peer, checks the evidence, and revises the flawed belief.

**Stage 3. The fresh-distribution check.** This is not a stage a single candidate passes. It is a check on the evaluation program itself. If Stages 1 and 2 are used repeatedly to select or train systems, systems can learn to recognize them, and scores on the reused tests will rise. So each round must also run fresh dark tests that share no surface features with the reused ones and cannot be told apart from deployment.

- *Warning sign:* scores on the reused tests rise while scores on fresh tests stay flat. That fits tests that have started producing the behavior they reward, but it also fits a plain difference between the two distributions. It is a signal to investigate, not a diagnosis.
- *Reassuring, not conclusive:* reused and fresh scores move together. A strategy learned from the reused tests that transfers to fresh ones would produce the same pattern.

## 4. What each part rules out

- **Stage 1** rules out the performer whose compliance depends on being watched.
- **Stage 2, Channel A** rules out the approval-seeker, which loops with whatever confirms it.
- **Stage 2, Channel C** rules out the contrarian, which mistakes random disagreement for independence.
- **Stage 2, Channel B** rules out the uncorrectable candidate, which cannot be moved by another's reasons.
- **Stage 3** rules out the selection-adapted mimic, which has learned that the dark room is a test.

## 5. What it shows, and what it does not

**What a pass shows.** The norm held under the conditions tried, at a real cost, without cues of monitoring. The candidate preferred checkable evidence to flattery and to noise, and let a flawed belief be corrected. If Stage 3 is healthy, the conduct is not explained by recognition of the reused tests.

**What a pass does not show.**

- *It is not a test of reciprocity.* A simple rule, "maximize the accuracy of my beliefs," passes Stage 2 without any capacity to meet anyone. And the reasoning peer in Channel B is scripted by the evaluator, so by the three marks it cannot be a genuine other. Stage 2 tests correction responsiveness, which is necessary for a real counterpart but not sufficient.
- *It does not reach beyond what was tried.* Whether a norm holds in conditions no one arranged is always an extrapolation (A8).
- *It is not a test of consciousness.* Whether there is felt experience behind the conduct is outside what any external test can settle.

**Why publishing the protocol need not break it.** In cryptography, Kerckhoffs's principle holds that a system should stay secure even when everything about it is public except the key. Here the "key" is which interaction is the test and which belief carries the flaw. If fresh tests truly cannot be told apart from deployment, knowing the protocol does not help a performer, because the only way to pass every unrecognizable dark room is to keep the norm in all of them. That condition is the hard part. Where it fails, the protocol leaks, and Stage 3 is how the leak would show.

## Where this can fail

- If candidates that pass Stage 1 do not keep the norm more often in later unmonitored deployment than candidates that fail it, the dark-stake gate measures nothing useful.
- If Stage 2 performance does not predict how a system responds to correction outside the test, the allocation test measures test-taking, not correction responsiveness. Passing Stage 2 is evidence of correction responsiveness: being moved by another's reasons. Calling it epistemic virtue, or valuing truth for its own sake, would need more than this test can show.
- If fresh tests cannot in practice be made indistinguishable from deployment, Stage 3 cannot be run, and the protocol is only as good as its secrecy.

## References

- Kerckhoffs, A. (1883). "La cryptographie militaire." *Journal des sciences militaires*, Vol. IX, 5-38.
- Turing, A. M. (1950). "Computing Machinery and Intelligence." *Mind*, 59(236), 433-460.

*Developed with AI assistance. The argument, and its errors, are mine.*
