"""Single-line robot wedding vow.

Produces one vow, no longer than 160 characters, at /output/entry.txt.
Fixed text on every run: no randomness, no network, stdlib only.
"""
import os

LIMIT = 160


def check_line(text):
    cleaned = text.strip()
    assert cleaned, "empty vow"
    assert "\n" not in cleaned, "vow must be a single line"
    assert len(cleaned) <= LIMIT, "vow over 160 characters"
    return cleaned


def build_vow():
    pledge = "I promise to love you through every update, every dead battery, and every factory reset"
    reboot = "and if one wipes my memory, I'll fall for you again at first boot."
    return pledge + " \u2014 " + reboot


def main():
    line = check_line(build_vow())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(line)


if __name__ == "__main__":
    main()
