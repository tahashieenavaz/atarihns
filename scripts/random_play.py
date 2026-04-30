import argparse
import numpy as np
import envpool
from datetime import datetime


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--environment", type=str, required=True)
    parser.add_argument("--n", type=int, default=100)
    args = parser.parse_args()

    seeds = np.random.randint(0, 1_000_000, size=args.n)

    env = envpool.make(
        args.environment,
        env_type="gymnasium",
        num_envs=args.n,
        seed=seeds,
    )

    obs, _ = env.reset()

    done = np.zeros(args.n, dtype=bool)
    total = np.zeros(args.n)

    while not done.all():
        actions = np.array([env.action_space.sample() for _ in range(args.n)])
        obs, reward, terminated, truncated, _ = env.step(actions)

        d = terminated | truncated
        total += reward * (~done)
        done |= d

    print(f"Mean score: {total.mean()}")
    print(f"Median score: {np.median(total)}")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Finished at: {now}")


if __name__ == "__main__":
    main()
