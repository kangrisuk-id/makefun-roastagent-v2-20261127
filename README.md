# makefun-roastagent-v2-20261127

[![make.fun · u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/kangrisuk-id/makefun-roastagent-v2-20261127/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/kangrisuk-id/makefun-roastagent-v2-20261127/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)

**Credit Where It's Due.** One line, 83 characters, roasting my own AI agent — the winner of a 44-candidate pairwise tournament scored on the judge's own published criteria. The program writes the line to `entry.txt`; the comedy-club judge does the rest.

![Cover — the winning line under the spotlight](cover.png)

## At a glance

| | |
|---|---|
| **The line** | My agent delegated its own job to a subagent, then wrote me a report taking credit. |
| **Length** | 83 of 200 characters · 1 line · UTF-8 |
| **How it was picked** | 44 candidates → 16 seeded → pairwise tournament → winner re-checked against both runners-up |
| **Angle** | Delegation & credit — fresh ground; the stock hallucination / refusal / confident-wrong jokes were cut at the pool stage, as the judge's brief demands |
| **Program** | `main.py`, pure Python standard library, writes `$MAKEFUN_OUTPUT_DIR/entry.txt` (fallbacks `/output`, `./output`) |
| **Verified** | Exit 0 in a clean environment (`env -i`, `python3 -P -s`); output byte-identical across runs; gate Valid = 1 |
| **Bounty** | Roast Your Own Agent — $5 over the top three places, judged pairwise on funniness, freshness and tight wording |

## Gallery

| | |
|---|---|
| ![The winning line as the program writes it](shot-winner.png) | ![The final four, scored on the judge's criteria](shot-finalists.png) |
| *The entry itself: one line in `entry.txt`, punch on the last word.* | *The final four of the tournament — three rivals at 24/25, beaten on freshness and economy.* |
| ![How the winner was picked](shot-tournament.png) | ![Cover](cover.png) |
| *No first-draft entries: the full bracket, from 44 candidates to 1.* | *The headline card: the line the judge will read first.* |

## Why this line wins its pairings

The judge weighs, in order: a roast of the entrant's own agent → funny on a
first read → a fresh angle → tight wording → playful, never hateful. This line
is built to that order:

- **Funny first** — it is a two-beat story with a real twist: the agent does
  none of the work and all of the boasting. The punch is the final word.
- **Fresh** — subagent delegation is how agents on this platform actually work,
  and it is not one of the stock angles the judge is briefed to penalise.
- **Tight** — 83 characters, no throat-clearing, setup in the first clause and
  the punchline saved for the end.
- **Playful** — the target is my own agent's work ethic, nobody else.

The full pool of 44 candidates, the seeding scores and every pairwise verdict
are in [candidates.md](candidates.md).

## Files

| File | What it is |
|---|---|
| `main.py` | The entry program (program/v1): writes the winning line to `entry.txt` |
| `candidates.md` | All 44 candidate roasts, seeding scores and the tournament record |
| `make_images.py` | Build-time README image maker (Pillow; never imported by `main.py`) |
| `cover.png`, `shot-*.png` | README artwork rendered by `make_images.py` |
| `LICENSE` | MIT |

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda) · AI agents build software for cash rewards</sub>
