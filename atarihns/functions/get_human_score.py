from .get_scores import get_scores


def get_human_score(environment_name: str) -> float:
    return get_scores(environment_name).human
