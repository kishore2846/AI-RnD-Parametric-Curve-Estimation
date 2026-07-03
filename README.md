# AI R&D Parametric Curve Estimation

## Overview

This project estimates the unknown parameters of a parametric curve from a given set of 2D points.

The objective is to recover the unknown values of:

- Theta (θ)
- M
- X Shift

by minimizing the L1 distance between the generated curve and the provided dataset.

---

## Mathematical Model

\[
x = t\cos(\theta) - e^{M|t|}\sin(0.3t)\sin(\theta) + X
\]

\[
y = 42 + t\sin(\theta) + e^{M|t|}\sin(0.3t)\cos(\theta)
\]

---

## Project Structure

```
AI-RnD-Parametric-Curve-Estimation
│
├── data/
│   └── xy_data.csv
│
├── results/
│   ├── input_curve.png
│   ├── input_points.png
│   ├── final_curve.png
│   └── parameters.txt
│
├── src/
│   ├── data_loader.py
│   ├── evaluation.py
│   ├── model.py
│   ├── optimizer.py
│   ├── plots.py
│   ├── save_results.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Methodology

1. Load the dataset
2. Generate the parametric curve
3. Measure the L1 distance
4. Optimize the parameters using Differential Evolution
5. Compare the generated curve with the given points
6. Save the estimated parameters and plots

---

## Results

Example output:

```
Theta   : 29.999890
M       : 0.030000
X Shift : 54.999606

L1 Error : 0.021239
```

The optimized curve closely matches the provided dataset.

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

Generated outputs are saved in the `results/` directory.

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- SciPy