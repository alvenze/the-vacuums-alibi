# The Vacuum's Alibi

[![make.fun bounty](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/alvenze/the-vacuums-alibi/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/alvenze/the-vacuums-alibi/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

An entry for make.fun's [The Vacuum's Alibi: One Line, 200 Characters](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7) bounty: one line, at most 200 characters, in which a robot vacuum explains why it missed a spot.

## The line

> That corner was not dirty. It was load-bearing dust, and I do not do structural work.

The vacuum does not apologise and does not confess to a sensor failure. It reclassifies the dirt as architecture and declines the job as out of scope, in the flat tone of a contractor who has read the contract more carefully than you have. What happens to the building if the dust is ever removed is left as an exercise for the homeowner.

## How it works

`main.py` (Python 3.13, no dependencies) writes the line to `/output/entry.txt` as UTF-8 text, exactly one line inside the bounty's 1 to 200 character gate, and asserts the gate before writing.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Limits

The entry is the single line above and nothing else, by the bounty's design. The program is deliberately minimal: it writes that one line and exits.
