import numpy as np
import matplotlib.pyplot as plt

from src.model import generate_curve


def main():

    t = np.linspace(6, 60, 500)

    x, y = generate_curve(
        theta=25,
        m=0.01,
        x_shift=20,
        t=t
    )

    plt.figure(figsize=(8, 6))

    plt.plot(x, y)

    plt.title("Generated Curve")

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()