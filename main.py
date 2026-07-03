import pandas as pd

from src.optimizer import estimate_parameters
from src.model import generate_points
from src.plots import compare_curves
from src.save_results import save_parameters


def main():

    data = pd.read_csv("data/xy_data.csv")

    print("Estimating parameters...\n")

    result = estimate_parameters(data)

    theta, m, x_shift = result.x

    print("Best Parameters Found\n")

    print(f"Theta   : {theta:.6f}")
    print(f"M       : {m:.6f}")
    print(f"X Shift : {x_shift:.6f}")
    print(f"\nL1 Error : {result.fun:.6f}")

    # Save the estimated parameters
    save_parameters(
        theta,
        m,
        x_shift,
        result.fun
    )

    # Generate the fitted curve
    predicted_x, predicted_y = generate_points(
        theta,
        m,
        x_shift
    )

    # Plot the comparison
    compare_curves(
        data,
        predicted_x,
        predicted_y
    )

    print("\nResults saved successfully.")
    print("-> results/parameters.txt")
    print("-> results/final_curve.png")


if __name__ == "__main__":
    main()