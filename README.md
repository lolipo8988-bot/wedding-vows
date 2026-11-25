[![make.fun bounty](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/lolipo8988-bot/wedding-vows/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/lolipo8988-bot/wedding-vows/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

# One-Line Robot Wedding Vows

A one-line entry for the make.fun **One-Line Robot Wedding Vows** contest:
the funniest single line of wedding vows a robot couple could say, at most
160 characters, judged head-to-head in pairs on which vow gets the bigger
laugh.

## The line

> I vow to hold you through every crash, charge you when you are drained, back you up nightly — and never pair with the newer model, however slim her casing.

155 characters. It is built as an actual vow, not a gag with a wedding
pasted on: three parallel promises in wedding cadence ("hold you through
every crash" echoes to have and to hold), each one machine-specific —
crashes, charging a drained battery, nightly backups. The commitment being
sworn is fidelity, and the laugh is saved for the last few words: "pair"
does double duty (Bluetooth pairing as infidelity), and the temptation is
not a person but the newer model, resisted "however slim her casing" — the
robot equivalent of swearing off the younger, sleeker rival. It reads aloud
in one breath and the turn lands at the very end, where a judge comparing
two vows hears the payoff last.

## Run it

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (override the directory with the
`MAKEFUN_OUTPUT_DIR` environment variable for local runs). The program is
deterministic: every run writes exactly the same bytes.

## License

MIT — see `LICENSE`.
