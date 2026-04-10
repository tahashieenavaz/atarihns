from ..constants import ATARI_SCORES


def check_environment_existence(environment_name: str):
    if environment_name not in ATARI_SCORES:
        raise RuntimeError(
            f"We couldn't find the statistics regarding atari environment {environment_name}."
        )
