"""Make the AI judge happy - entry program.

Writes one image to /output/entry.png by copying the image bundled
with this repository: a warm digital painting of a small friendly
robot offering a bright sunflower to a tiny orange kitten in golden
sunrise light. Deterministic: no network, no randomness, both runs
write identical bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "art.png")
DST = "/output/entry.png"


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
