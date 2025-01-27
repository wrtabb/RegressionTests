
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# The true function for the data
def function_true(x):
    return (np.sin(x) + np.sin((10.0/3.0)*x))**2

# Generate random data using function_true() as truth
# With gaussian uncertainty on each point
def generate_data(num_entries):
    print(f"Generating data for {num_entries} entries")

    xmin, xmax = 0.0, 3.5
    inputs = np.arange(xmin,xmax,0.01)
    results = function_true(inputs)
    plt.plot(inputs,results)
    plot_name_true = "../Plots/true_fuction.png"
    plt.savefig(plot_name_true)
    print(f"Saved true function plot as {plot_name_true}")

    X = np.full((num_entries),-1000.0)
    Y = np.full((num_entries),-1000.0)
    Y_estimate = np.full((num_entries),-1000.0)

    for i in range(num_entries):
        X[i] = np.random.uniform(xmin,xmax)
        Y[i] = function_true(X[i])
        y_err = np.random.normal(loc=0,scale=0.5)
        Y_estimate[i] = Y[i]+y_err

    plt.scatter(X,Y_estimate)
    plot_name_data = f"../Plots/data_plot_{num_entries}.png"
    plt.savefig(plot_name_data)
    plt.clf()
    print(f"Saved data plot as {plot_name_data}")

    df_x = pd.DataFrame(X,columns=['X'])
    df_y = pd.DataFrame(Y)
    df_yestimate = pd.DataFrame(Y_estimate)

    df = df_x
    df.insert(1,"estimate",df_yestimate)
    df.insert(2,"truth",df_y)

    data_save_name = f"../SavedData/simulated_data_{num_entries}.pkl"
    df.to_pickle(data_save_name)
    print(f"Saved dataframe to pickle file {data_save_name}")
    print("\n")

generate_data(100)
generate_data(1000)
generate_data(10000)
generate_data(100000)
generate_data(1000000)
