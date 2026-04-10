from .get_human_score import get_human_score
from .get_random_score import get_random_score


def calculate_hns(environment_name: str, agent_score: float) -> float:
    human_score = get_human_score(environment_name)
    random_score = get_random_score(environment_name)
    return (agent_score - random_score) / (human_score - random_score)
