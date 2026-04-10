# Atari HNS (Human Normalized Score)

Lightweight helper for computing Atari human-normalized scores (HNS) using published human and random baselines.

## Installation

You can simply install this package using pip package manager.

```
pip install atarihns
```

## Usage

```python
from atarihns import get_human_score, get_random_score
from atarihns import calculate_hns, get_hns

environment = "Pong-v5"
agent_score = 15.0

human = get_human_score(environment)
random = get_random_score(environment)
hns = calculate_hns(environment, agent_score)

print(f"{environment} human: {human}, random: {random}, hns: {hns:.3f}")
```

## Notes

- Baseline scores for ALE environments are defined in `atarihns.constants.ATARI_SCORES` as `(random, human)`.
- Helper functions raise `KeyError` if an environment name is missing from the table.
