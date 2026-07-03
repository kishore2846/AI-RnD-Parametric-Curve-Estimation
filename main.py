import pandas as pd


def load_points(file_path):
    points = pd.read_csv(file_path)
    return points


def main():
    points = load_points("data/xy_data.csv")

    print("\nFirst 5 points:\n")
    print(points.head())

    print("\nDataset information:\n")
    print(points.info())

    print("\nBasic statistics:\n")
    print(points.describe())


if __name__ == "__main__":
    main()