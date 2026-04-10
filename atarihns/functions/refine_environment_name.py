def refine_environment_name(environment_name: str):
    if environment_name.startswith("ALE/"):
        return environment_name[4:]

    return environment_name
