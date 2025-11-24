from .constants import ATARI_SCORES


def get_human_score(environment: str) -> float:
    return ATARI_SCORES.get(environment)[1]


def get_random_score(environment: str) -> float:
    return ATARI_SCORES.get(environment)[0]


def calculate_hns(environment: str, agent_score: float) -> float:
    human_score = get_human_score(environment)
    random_score = get_human_score(environment)
    return (agent_score - random_score) / (human_score - random_score)
