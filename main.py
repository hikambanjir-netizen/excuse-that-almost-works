"""The Excuse That Almost Works - a make.fun one-line entry.

Writes a single excuse to /output/entry.txt: the text a gamer sends
their boss to skip work during GTA 6 launch week. The excuse itself
never mentions the game; it survives on one boring, specific detail -
a root canal that got moved because somebody else cancelled.
"""

import os

def excuse_line() -> str:
    """The excuse, exactly as it would be thumbed into a phone at 7am.

    Two short sentences: the moved appointment does the believing,
    the numb face does the laughing. Kept plain on purpose - a long
    excuse sounds rehearsed, and a rehearsed one is a confession.
    """
    return (
        "Sorry, dentist just rang: my root canal moved to today, "
        "someone cancelled. Face numb by nine, useless to everyone."
    )


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(excuse_line())


if __name__ == "__main__":
    main()
