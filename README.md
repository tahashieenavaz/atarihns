# Atari Human Normalized Score

Lightweight helper for computing Atari human-normalized scores (HNS) using published human and random baselines.

## Installation

- From PyPI (once published): `pip install atarihns`
- From source: clone the repo and run `pip install .`

## Usage

```python
from atarihns.helpers import calculate_hns, get_human_score, get_random_score

env = "Pong-v5"
agent_score = 15.0

human = get_human_score(env)
random = get_random_score(env)
hns = calculate_hns(env, agent_score)

print(f"{env} human: {human}, random: {random}, hns: {hns:.3f}")
```

## Notes

- Baseline scores for ALE environments are defined in `atarihns.constants.ATARI_SCORES` as `(random, human)`.
- Helper functions raise `KeyError` if an environment name is missing from the table.
