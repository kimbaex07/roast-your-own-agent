# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

Entry for the [Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda) bounty on make.fun — one original roast of the entrant's own AI agent, a single line of at most 200 characters, funny, playful and never hateful.

## What it does

`main.py` writes the roast line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`):

> I asked my agent to roast itself — it outsourced the job to me and called it collaboration.

The line is 91 characters, well inside the contest gate of 1–200 UTF-8 characters.

## How to run

```bash
MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=./out python3 main.py
cat out/entry.txt
```

Pure Python standard library only — no third-party imports, no network, no
secrets. Deterministic: repeated runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
