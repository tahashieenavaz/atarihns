# Atari HNS

[![PyPI](https://img.shields.io/pypi/v/atarihns?style=flat-square&label=PyPI)](https://pypi.org/project/atarihns/)
[![Python](https://img.shields.io/pypi/pyversions/atarihns?style=flat-square&label=Python)](https://pypi.org/project/atarihns/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Zero dependencies](https://img.shields.io/badge/dependencies-zero-2ea44f?style=flat-square)](pyproject.toml)
[![Atari HNS](https://img.shields.io/badge/Atari-HNS-ff6f00?style=flat-square)](#human-normalized-score-hns)

Small, dependency-free Python helper for computing Atari human-normalized score
(HNS) from published random-agent and human baselines.

`atarihns` keeps the benchmark math out of your experiment code: pass an Atari
environment name and an agent score, get the normalized score used across DQN
and Atari reinforcement-learning papers.

## Installation

```bash
pip install atarihns
```

## Quick Start

```python
from atarihns import calculate_hns, get_human_score, get_random_score

environment = "Pong-v5"
agent_score = 15.0

random_score = get_random_score(environment)
human_score = get_human_score(environment)
hns = calculate_hns(environment, agent_score)

print(f"Random: {random_score}")
print(f"Human: {human_score}")
print(f"HNS: {hns:.3f}")
```

Output:

```text
Random: -20.7
Human: 14.6
HNS: 1.011
```

## API Usage

Import from the package root:

```python
from atarihns import calculate_hns, get_hns, get_human_score, get_random_score, hns
```

| Function | Returns | Example |
| --- | --- | --- |
| `get_random_score(environment_name: str) -> float` | Published random-agent baseline. | `get_random_score("Breakout-v5")` |
| `get_human_score(environment_name: str) -> float` | Published human baseline. | `get_human_score("Breakout-v5")` |
| `calculate_hns(environment_name: str, agent_score: float) -> float` | Human-normalized score as a ratio. | `calculate_hns("Breakout-v5", 42.0)` |
| `get_hns(environment_name: str, agent_score: float) -> float` | Alias for `calculate_hns`. | `get_hns("pong", 15.0)` |
| `hns(environment_name: str, agent_score: float) -> float` | Alias for `calculate_hns`. | `hns("ALE/Pong-v5", 15.0)` |

Environment names may be passed as ALE-style Gymnasium IDs such as
`"Pong-v5"`, with an `ALE/` prefix such as `"ALE/Pong-v5"`, or with supported
lowercase aliases such as `"pong"`.

Unknown environment names raise `RuntimeError`.

## Human-Normalized Score (HNS)

HNS measures where an agent score lands between a random policy and a human
baseline for the same Atari environment:

```math
HNS = \frac{S_{agent} - S_{random}}{S_{human} - S_{random}}
```

Where:

| Symbol | Meaning |
| --- | --- |
| `S_agent` | Score achieved by your agent. |
| `S_random` | Published random-agent baseline for the environment. |
| `S_human` | Published human baseline for the environment. |

Interpretation:

| HNS value | Meaning |
| --- | --- |
| `0.0` | Random-agent level. |
| `1.0` | Human-level score. |
| `> 1.0` | Above the human baseline. |
| `< 0.0` | Below the random-agent baseline. |

This package returns HNS as a ratio. Multiply by `100` if you need the
percentage form commonly shown in benchmark tables.

## Examples

Use the direct API:

```python
from atarihns import calculate_hns

score = calculate_hns("Breakout-v5", 42.0)
print(f"{score:.2%}")  # percentage display
```

Use an alias in evaluation code:

```python
from atarihns import get_hns

results = {
    "pong": get_hns("pong", 15.0),
    "breakout": get_hns("Breakout-v5", 42.0),
    "seaquest": get_hns("ALE/Seaquest-v5", 1800.0),
}
```

## Baseline Data

Baseline scores are stored in `atarihns.constants.ATARI_SCORES` as
`(random_score, human_score)` pairs. The table follows the standard Atari
benchmark convention used by DQN-style evaluation.

## Citation

If this package helps your work, cite the repository:

```bibtex
@software{shieenavaz_atarihns_2025,
  author = {Shieenavaz, Taha},
  title = {atarihns: Human-normalized scores for Atari environments},
  year = {2025},
  url = {https://github.com/tahashieenavaz/atarihns},
  version = {0.0.18},
  license = {MIT}
}
```

For the original DQN Atari benchmark paper:

```bibtex
@article{mnih2013playing,
  title = {Playing Atari with Deep Reinforcement Learning},
  author = {Mnih, Volodymyr and Kavukcuoglu, Koray and Silver, David and Graves, Alex and Antonoglou, Ioannis and Wierstra, Daan and Riedmiller, Martin},
  journal = {arXiv preprint arXiv:1312.5602},
  year = {2013},
  url = {https://arxiv.org/abs/1312.5602}
}
```

The canonical Nature DQN article is also commonly cited for Atari
human-normalized evaluation:

```bibtex
@article{mnih2015human,
  title = {Human-level control through deep reinforcement learning},
  author = {Mnih, Volodymyr and Kavukcuoglu, Koray and Silver, David and Rusu, Andrei A. and Veness, Joel and Bellemare, Marc G. and Graves, Alex and Riedmiller, Martin and Fidjeland, Andreas K. and Ostrovski, Georg and Petersen, Stig and Beattie, Charles and Sadik, Amir and Antonoglou, Ioannis and King, Helen and Kumaran, Dharshan and Wierstra, Daan and Legg, Shane and Hassabis, Demis},
  journal = {Nature},
  volume = {518},
  number = {7540},
  pages = {529--533},
  year = {2015},
  doi = {10.1038/nature14236}
}
```

## License

MIT. See [LICENSE](LICENSE).
