#!/usr/bin/env python3
"""
coord_to_code.py

Enter a coordinate (row A..R and column 0..19) and get the 4-choice code
derived from the packed byte stored at that coordinate in the $5500 table.

Usage:
  python3 coord_to_code.py A5
  python3 coord_to_code.py r19
  python3 coord_to_code.py        # interactive prompt

The table bytes (360 bytes = 18 rows × 20 cols) are embedded below.
"""

HEX_BYTES = """
A2 DF 9A A2 FF 4C 1F 70 03 CA 10 F7 58 A2 08 BD
00 80 DD 90 57 F0 03 4C 55 5A CA 10 F2 A9 CF 85
FC A9 00 85 FB A9 AA A0 FF 91 FB 88 D0 FB C6 FC
A6 FC E0 BF D0 F3 A9 00 8D 15 D0 8D 4F 57 8D 18
D4 8D 20 D0 8D 21 D0 AD 02 DD 09 03 8D 02 DD AD
00 DD 29 FC 09 03 8D 00 DD A9 04 8D 88 02 A9 14
8D 18 D0 A9 00 8D 60 57 8D 61 57 A5 A2 0A 0A 0A
2E 60 57 0A 2E 60 57 AE 60 57 8E 5F 57 0A 2E 60
57 0A 2E 60 57 AD 60 57 18 6D 5F 57 8D 60 57 AD
12 D0 29 3F 0A 0A 0A 2E 61 57 AE 61 57 8E 5F 57
0A 2E 61 57 0A 2E 61 57 0A 2E 61 57 AD 61 57 18
6D 5F 57 8D 61 57 A9 55 85 FE A9 00 A2 14 18 6D
61 57 90 02 E6 FE CA D0 F5 85 FD AC 60 57 B1 FD
85 02 AD 60 57 0A AA BD 62 57 8D 2E 57 E8 BD 62
57 8D 2F 57 AC 61 57 C8 8C 2D 57 A9 00 85 FB A8
A9 04 85 FC A9 20 91 FB 88 D0 F9 E6 FC A5 FC C9
08 D0 F1 A2 20 BD 0F 57 9D 90 05 A9 0E 9D 90 D9
CA 10 F2 A2 0E BD 30 57 9D E0 05 9D 30 06 9D F2
05 9D 1A 06 9D 42 06 A9 00 9D F2 D9 9D 1A DA 9D
42 DA BD 3F 57 9D 08 06 BD 50 57 9D E0 D9 9D 08
DA 9D 30 DA CA 10 CE A2 00 8E 4E 57 A2 03 A5 C5
C9 40 F0 FA C9 01 D0 08 AD 4E 57 F0 F1 4C A1 56
C9 38 D0 25 A9 00 9D 03
"""

from sys import argv, exit

def hex_to_bytes(s):
    parts = [p for p in s.strip().split() if p]
    return bytes(int(p, 16) for p in parts)

def choices_from_packed(packed):
    d3 = (packed >> 6) & 0x03
    d2 = (packed >> 4) & 0x03
    d1 = (packed >> 2) & 0x03
    d0 = packed & 0x03
    return [d3 + 1, d2 + 1, d1 + 1, d0 + 1]

def parse_coord(s):
    s = s.strip().upper()
    if len(s) < 2:
        raise ValueError("Coordinate must be letter+number, e.g. A0 or R19.")
    row_char = s[0]
    if not ('A' <= row_char <= 'R'):
        raise ValueError("Row must be A..R.")
    try:
        col = int(s[1:])
    except ValueError:
        raise ValueError("Column must be an integer 0..19.")
    if not (0 <= col <= 19):
        raise ValueError("Column must be 0..19.")
    row = ord(row_char) - ord('A')
    return row, col

def coord_to_index(row, col, cols=20):
    return row * cols + col

def main():
    data = hex_to_bytes(HEX_BYTES)
    if len(data) != 18 * 20:
        raise SystemExit("Embedded table length mismatch; expected 360 bytes.")
    if len(argv) >= 2:
        coord = argv[1]
    else:
        coord = input("Enter coordinate (A..R and 0..19), e.g. A5: ").strip()
    try:
        row, col = parse_coord(coord)
    except ValueError as e:
        print("Error:", e)
        exit(2)
    idx = coord_to_index(row, col)
    packed = data[idx]
    choices = choices_from_packed(packed)
    choices_str = ''.join(str(x) for x in choices)
    row_label = chr(ord('A') + row)
    print(f"Code: {choices_str}")

if __name__ == "__main__":
    main()
