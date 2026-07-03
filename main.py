import pandas as pd

from src.model import generate_points
from src.evaluation import l1_distance


def main():

    data = pd.read_csv("data/xy_data.csv")

    x_pred, y_pred = generate_points(
        theta=25,
        m=0.01,
        x_shift=20
    )

    score = l1_distance(
        data["x"],
        data["y"],
        x_pred,
        y_pred
    )

    print(f"L1 Error : {score:.4f}")


if __name__ == "__main__":
    main()