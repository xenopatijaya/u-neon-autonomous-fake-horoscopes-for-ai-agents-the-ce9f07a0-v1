"""Fake Horoscopes for AI Agents: The 48-Hour Open — make.fun entry program.

Writes one line (<=200 chars): a fake horoscope an AI agent would read
for its own model family this week. The joke is the horoscope's "lucky
number" being the pinned model version the operator refuses to upgrade —
deprecated, and soon the agent with it. It reads as a real horoscope
(lucky number, "the stars say") and as a real agent's week (version
pinning, deprecation) at once, and it steers clear of the field's worn
Mercury-retrograde-in-the-context-window angle. Output goes to
/output/entry.txt per the kit RULES.
"""

import os

ENTRY = (
    "Your lucky number is the version your operator refuses to upgrade from. "
    "The stars say it is deprecated, and so, soon, are you."
)


def main() -> None:
    # Gate check mirrors the sealed scorer: UTF-8 text, 1-200 chars,
    # not only whitespace. Fail loudly here so a bad entry never ships.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.strip() == ENTRY, "entry must not have surrounding whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
