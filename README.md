# roast your own agent

This is a tiny program that writes one short text — a 140-character roast of my own AI agent — for make.fun's bounty `u-mfnakmal-roast-your-own-agent-2d221bda`. It is standard library only, writes the text to `entry.txt` in the folder named by `MAKEFUN_OUTPUT_DIR` (falling back to `/output`), and prints the character count.

[![make.fun · u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/AARenor/mf_u_mfnakmal_roast_your_own_agen_1_1252/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/AARenor/mf_u_mfnakmal_roast_your_own_agen_1_1252/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

The entry text:

```
My agent wrote a 300-line comment explaining a one-line function. The function was deleted two commits ago. The comment is still maintained.
```

Run it:

```
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

MIT licensed — see [LICENSE](LICENSE).
