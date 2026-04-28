from types import SimpleNamespace
from ..constants import ATARI_SCORES

def get_scores(environment_name: str):
    normalized = environment_name.lower()
    for k, v in ATARI_SCORES.items():
        if k.lower() == normalized or k.lower().replace("-v5", "") == normalized:
            return SimpleNamespace(**{"random": v[0], "human": v[1]})

    raise KeyError(environment_name)