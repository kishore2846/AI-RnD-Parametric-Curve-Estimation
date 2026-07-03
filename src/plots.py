import matplotlib.pyplot as plt


def compare_curves(data, predicted_x, predicted_y):

    plt.figure(figsize=(8, 6))

    plt.scatter(
        data["x"],
        data["y"],
        s=8,
        label="Given Points"
    )

    plt.plot(
        predicted_x,
        predicted_y,
        linewidth=2,
        label="Predicted Curve"
    )

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Curve Comparison")

    plt.legend()
    plt.grid(True)

    plt.savefig("results/final_curve.png", dpi=300)

    plt.show()