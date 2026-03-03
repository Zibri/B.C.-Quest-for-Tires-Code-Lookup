# 🦕 B.C.'s Quest for Tires — Protection Code Lookup

A web-based tool to decode the **copy-protection wheel codes** for the original **Commodore 64 tape release** of *B.C.'s Quest for Tires* (Software Projects, 1984).

---

## About the Game

> *Cute Chick is in trouble! She is being held captive by the dinosaur, and it is up to Thor to ride his trusty wheel to the rescue.*

*B.C.'s Quest for Tires* is a horizontally scrolling game designed by Rick Banks and Michael Bate. Based on the comic strip *B.C.* by Johnny Hart, it features caveman Thor riding a wheel through obstacles — an early ancestor of the endless runner genre.

The C64 tape version uses a **protection wheel** — a physical cardboard dial included with the game — that asks the player to look up a code at a specific row (A–R) and column (0–19) before being allowed to play.

🎮 **Original tape on the Internet Archive (Ultimate Tape Archive):**
[BC's Quest for Tires (1984) — archive.org](https://archive.org/details/uta_BCs_Quest_for_Tires_1984_Software_Projects_393)

---

## What This Tool Does

When the game starts, it prompts you with a coordinate like **"Row G, Column 11"**. Without the original manual, you're stuck.

This tool reverse-engineers the table embedded in the tape binary (18 rows × 20 columns = 360 bytes), unpacks the 2-bit fields stored in each byte, and shows you the correct 4-digit code instantly.

---

## Files

| File | Description |
|---|---|
| `bc.py` | Python CLI — run from terminal with a coordinate argument |
| `index.html` | Standalone web app — open in any browser, no server needed |

---

## Usage

### Web App

Just open https://zibri.github.io/B.C.-Quest-for-Tires-Code-Lookup/ in your browser. Click a row (A–R), then a column (0–19) — the code appears immediately.

### Python CLI

```bash
python3 bc.py A5       # look up row A, column 5
python3 bc.py G11      # look up row G, column 11
python3 bc.py          # interactive prompt
```

**Output:**
```
Code: 3142
```

---

## Requirements

- **Web app:** Any modern browser. No dependencies, no server.
- **Python script:** Python 3.x, no external libraries.

---

## Acknowledgements

- Game preserved by the **Ultimate Tape Archive** on the [Internet Archive](https://archive.org/details/uta_BCs_Quest_for_Tires_1984_Software_Projects_393)
- Original game by Sydney Development Corp., published by Sierra On-Line / Software Projects (1983–1984)
- Comic strip *B.C.* by Johnny Hart
