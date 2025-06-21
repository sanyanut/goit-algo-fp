import random
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd


def monte_carlo_dice_roll(num_simulations):
    sums = []
    for _ in range(num_simulations):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        sums.append(roll1 + roll2)

    sum_counts = Counter(sums)
    probabilities = {s: count / num_simulations for s, count in sum_counts.items()}
    return probabilities


def display_results(monte_carlo_probs, analytical_probs):
    all_sums = sorted(
        list(set(monte_carlo_probs.keys()) | set(analytical_probs.keys()))
    )

    data = []
    for s in all_sums:
        mc_prob = monte_carlo_probs.get(s, 0) * 100
        analytic_prob = analytical_probs.get(s, 0) * 100
        data.append([s, f"{mc_prob:.2f}%", f"{analytic_prob:.2f}%"])

    df = pd.DataFrame(
        data, columns=["Sum", "Probability (Monte-Carlo)", "Probability (Analytical)"]
    )
    print("Probability comparison table:")
    print(df.to_string(index=False))

    mc_values = [monte_carlo_probs.get(s, 0) for s in all_sums]
    analytic_values = [analytical_probs.get(s, 0) for s in all_sums]

    plt.figure(figsize=(10, 6))
    plt.bar(
        [s - 0.2 for s in all_sums],
        mc_values,
        width=0.4,
        label="Monte-Carlo",
        color="blue",
    )
    plt.bar(
        [s + 0.2 for s in all_sums],
        analytic_values,
        width=0.4,
        label="Analytical",
        color="green",
    )
    plt.xlabel("Sum")
    plt.ylabel("Probability")
    plt.title("Comparing the probabilities of the sums when rolling two dice")
    plt.xticks(all_sums)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


if __name__ == "__main__":
    analytical_probabilities = {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36,
    }

    num_simulations = 1000000

    print(f"Running Monte-Carlo simulation with {num_simulations} dice rolls")
    monte_carlo_results = monte_carlo_dice_roll(num_simulations)

    display_results(monte_carlo_results, analytical_probabilities)
