from .refine_environment_name import refine_environment_name
from .check_environment_existence import check_environment_existence
from ..constants import ATARI_SCORES


def get_human_score(environment_name: str) -> float:
    environment_name = refine_environment_name(environment_name)
    check_environment_existence(environment_name)
    return ATARI_SCORES.get(environment_name)[1]
