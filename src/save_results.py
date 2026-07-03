def save_parameters(theta, m, x_shift, error):

    with open("results/parameters.txt", "w") as file:

        file.write("Estimated Parameters\n")
        file.write("----------------------\n\n")

        file.write(f"Theta   : {theta:.6f}\n")
        file.write(f"M       : {m:.6f}\n")
        file.write(f"X Shift : {x_shift:.6f}\n")
        file.write(f"L1 Error: {error:.6f}\n")