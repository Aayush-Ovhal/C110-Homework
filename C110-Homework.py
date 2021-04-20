import pandas as pd
import plotly.figure_factory as pff
import plotly.graph_objects as go
import random as rn
import statistics as st
import csv

df = pd.read_csv("average.csv")
data = df["average"].tolist()

def mean_set(sample_counter):
    dataset = []
    for i in range(0, sample_counter):
        random_index = rn.randint(0, len(data) - 1)
        data_value = data[random_index]
        dataset.append(data_value)

    mean_of_data = st.mean(dataset)
    return mean_of_data

def plot_graph(mean_list):
    df = mean_list
    meandf = st.mean(df)
    fig = pff.create_distplot([df], ["Avg."], show_hist = False)
    fig.add_trace(go.Scatter(x = [meandf, meandf], y = [0, 1], name = "Mean", mode = "lines"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_mean = mean_set(30)
        mean_list.append(set_of_mean)
    plot_graph(mean_list)

    population_mean = st.mean(mean_list)
    sampling_mean = st.mean(data)

    population_stdev = st.stdev(mean_list)
    sampling_stdev = st.stdev(data)

    print("Your population mean is: " + str(population_mean))
    print("Your sampling mean is: " + str(sampling_mean))
    print("Your population standard deviation is: " + str(population_stdev))
    print("Your sampling standard deviation is: " + str(sampling_stdev))

setup()
