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
from atarihns import calculate_hns
from atarihns import get_hns
from atarihns import get_human_score
from atarihns import get_random_score, hns
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

<div align="center">

| Symbol | Meaning |
| --- | --- |
| `S_agent` | Score achieved by your agent. |
| `S_random` | Published random-agent baseline for the environment. |
| `S_human` | Published human baseline for the environment. |

</div>

Interpretation:

<div align="center">

| HNS value | Meaning |
| --- | --- |
| `0.0` | Random-agent level. |
| `1.0` | Human-level score. |
| `> 1.0` | Above the human baseline. |
| `< 0.0` | Below the random-agent baseline. |

</div>

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

## Available Games

The package includes baselines for the following Atari games. Environment IDs
may also be passed with an `ALE/` prefix, such as `ALE/Pong-v5`.

<div align="center">

| Game | Environment ID | Alias |
| :---: | :---: | :---: |
| Alien | `Alien-v5` | `alien` |
| Amidar | `Amidar-v5` | `amidar` |
| Assault | `Assault-v5` | `assault` |
| Asterix | `Asterix-v5` | `asterix` |
| Asteroids | `Asteroids-v5` | `asteroids` |
| Atlantis | `Atlantis-v5` | `atlantis` |
| BankHeist | `BankHeist-v5` | `bankheist` |
| BattleZone | `BattleZone-v5` | `battlezone` |
| BeamRider | `BeamRider-v5` | `beamrider` |
| Berzerk | `Berzerk-v5` | `berzerk` |
| Bowling | `Bowling-v5` | `bowling` |
| Boxing | `Boxing-v5` | `boxing` |
| Breakout | `Breakout-v5` | `breakout` |
| Centipede | `Centipede-v5` | `centipede` |
| ChopperCommand | `ChopperCommand-v5` | `choppercommand` |
| CrazyClimber | `CrazyClimber-v5` | `crazyclimber` |
| Defender | `Defender-v5` | `defender` |
| DemonAttack | `DemonAttack-v5` | `demonattack` |
| DoubleDunk | `DoubleDunk-v5` | `doubledunk` |
| Enduro | `Enduro-v5` | `enduro` |
| FishingDerby | `FishingDerby-v5` | `fishingderby` |
| Freeway | `Freeway-v5` | `freeway` |
| Frostbite | `Frostbite-v5` | `frostbite` |
| Gopher | `Gopher-v5` | `gopher` |
| Gravitar | `Gravitar-v5` | `gravitar` |
| Hero | `Hero-v5` | `hero` |
| IceHockey | `IceHockey-v5` | `icehockey` |
| Jamesbond | `Jamesbond-v5` | `jamesbond` |
| Kangaroo | `Kangaroo-v5` | `kangaroo` |
| Krull | `Krull-v5` | `krull` |
| KungFuMaster | `KungFuMaster-v5` | `kungfumaster` |
| MontezumaRevenge | `MontezumaRevenge-v5` | `montezumarevenge` |
| MsPacman | `MsPacman-v5` | `mspacman` |
| NameThisGame | `NameThisGame-v5` | `namethisgame` |
| Phoenix | `Phoenix-v5` | `phoenix` |
| Pitfall | `Pitfall-v5` | `pitfall` |
| Pong | `Pong-v5` | `pong` |
| PrivateEye | `PrivateEye-v5` | `privateeye` |
| Qbert | `Qbert-v5` | `qbert` |
| Riverraid | `Riverraid-v5` | `riverraid` |
| RoadRunner | `RoadRunner-v5` | `roadrunner` |
| Robotank | `Robotank-v5` | `robotank` |
| Seaquest | `Seaquest-v5` | `seaquest` |
| Skiing | `Skiing-v5` | `skiing` |
| Solaris | `Solaris-v5` | `solaris` |
| SpaceInvaders | `SpaceInvaders-v5` | `spaceinvaders` |
| StarGunner | `StarGunner-v5` | `stargunner` |
| Surround | `Surround-v5` | `surround` |
| Tennis | `Tennis-v5` | `tennis` |
| TimePilot | `TimePilot-v5` | `timepilot` |
| Tutankham | `Tutankham-v5` | `tutankham` |
| UpNDown | `UpNDown-v5` | `upndown` |
| Venture | `Venture-v5` | `venture` |
| VideoPinball | `VideoPinball-v5` | `videopinball` |
| WizardOfWor | `WizardOfWor-v5` | `wizardofwor` |
| YarsRevenge | `YarsRevenge-v5` | `yarsrevenge` |
| Zaxxon | `Zaxxon-v5` | `zaxxon` |

</div>

## Baseline Data

Baseline scores are stored in `atarihns.constants.ATARI_SCORES` as `(random_score, human_score)` pairs. The table follows the standard Atari benchmark convention used by DQN-style evaluation.

## Gathering Data

I have gathered data regarding the games that were not originally present in the Atari 57 benchmark and am trying to complete the data. Contributions are welcomed. 

Random scores have been calculated using [EnvPool](https://pypi.org/project/envpool) with averaging the results of 10 completely random environments on random seeds using [this](./scripts/random_play.py) script.

### Air Raid

- [Electronic Rag](https://www.youtube.com/watch?v=IzJ_HjIgybs) achieved `4825`.
- [Retro Game On](https://www.youtube.com/watch?v=NiBeweH4YyY) shows a videos of somebody playing achieving `3825` 
- [Lenny's Longplays](https://www.youtube.com/watch?v=koiisyzAd1o) plays many times and achieves `5100`, `2225`, `2250`, `1375`, `825`, `150`, `650`, `675`, `875`.

The average of these scores is `1865.9909091`. 

The random score was calculated with an average of `571.25` and a median of `475.0`, as of 2026-04-30 13:50:19.

### Crossbow

- [Highretrogamelord](https://www.youtube.com/watch?v=3Q6RPYDSEfw) achieved `13600`.
- [The No Swear Gamer](https://www.youtube.com/watch?v=OrStTZUblOs) achieved `37350`.
- [The GamesBay](https://www.youtube.com/watch?v=KALIBQ6a8tM) plays twice and achieves `17250`, `17450`.
- [ArcadeUSA](https://www.youtube.com/watch?v=bbyvUj7Qqvo) achieves `14950`. 
- [BPN_GAMING](https://www.youtube.com/watch?v=FrrKArsZzb4) plays multiple times and achieves `24150`, `3350`, `13800`, `16400`, `30100`, `18150`, `19600`, `18450`, `55600`, `19650`, `50`, `250`, `30150`, `450`, `54700`

These numbers average at `20272.5`.

The random score was calculated with an average of `35.0` and a median of `0.0`, as of 2026-04-30 14:09:26.

## Citation

If this package helps your work, cite the repository:

```bibtex
@software{shieenavaz2025atarihns,
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
