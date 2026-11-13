# ai-happy-01

Entry for make.fun's "Make the AI judge happy" bounty
(https://make.fun/bounty/ai-happy-01).

`main.py` (Python 3, standard library only) writes one image to
`/output/entry.png`: a warm digital painting of a small friendly robot
offering a bright sunflower to a tiny orange kitten in golden sunrise
light. The image is embedded in `main.py` as base64. No network, no
randomness, deterministic: every run writes the exact same bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output is a 1024x1024 PNG, under the 1 MiB gate limit.
