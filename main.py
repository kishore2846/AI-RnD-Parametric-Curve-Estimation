import pandas as pd
import matplotlib.pyplot as plt


def load_points(file_path):
    points = pd.read_csv(file_path)
    return points


def plot_curve(points):

    plt.figure(figsize=(8, 6))

    plt.scatter(
        points["x"],
        points["y"],
        s=8,
        alpha=0.7
    )

    plt.title("Given Points")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.grid(True)

    plt.savefig("results/input_points.png", dpi=300)

    plt.show()


def main():

    points = load_points("data/xy_data.csv")

    plot_curve(points)


if __name__ == "__main__":
    main()