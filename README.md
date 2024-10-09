# Matplotlib Progress Tracker

This repository is designed to track my progress with Matplotlib, a powerful plotting library in Python.
The main purpose is to practice and understand how to create visualizations using Matplotlib, save them as image files, and document each step of the learning process.

## Basic Example Code

The following is a basic example of how to plot a simple line graph using Matplotlib and save it to a file.

```python
# Importing matplotlib.pyplot
# Saving it in the memory as plt
import matplotlib.pyplot as plt

# Creating a list of 4 integer values for x and y axis
x_axis = [1, 2, 3, 4]
y_axis = [4, 3, 2, 1]

# Creating a figure and axis object using subplots
fig, ax = plt.subplots()

# Plotting the graph using axis object
# It plots a graph with x and y values
ax.plot(x_axis, y_axis)

# Saving the created graph in a file
fig.savefig("plots/basic_plot.png")
```

### Code Explanation

1. **Importing Matplotlib**:
   - `import matplotlib.pyplot as plt`: This line imports the `pyplot` module from Matplotlib and assigns it the alias `plt`. This allows you to easily refer to the module throughout the code.

2. **Defining Data**:
   - Two lists `x_axis` and `y_axis` contain the values that will be plotted on the graph. These represent the points on the x-axis and y-axis, respectively.

3. **Creating a Figure and Axis**:
   - `fig, ax = plt.subplots()`: This line creates a figure (`fig`) and an axis (`ax`). The figure is the container that holds the plot, while the axis is where the data points will be plotted.

4. **Plotting the Data**:
   - `ax.plot(x_axis, y_axis)`: This line takes the data from the x and y lists and plots them on the axis using a line plot.

5. **Saving the Plot**:
   - `fig.savefig("plots/basic_plot.png")`: This line saves the plot as an image in the "plots" folder with the name `basic_plot.png`.

## Repository Structure

This repository contains two main folders:

1. **Explanations**:
   - This folder contains text files that provide detailed explanations for each code sample. Each file is named according to the program it explains.
   - Example: For the `basic_mat.py` above, the explanation would be in a file named `basic_mat_ex.txt` in the `Explanations` folder.

2. **Plots**:
   - This folder stores the output images generated by the code. Each plot is saved as a `.png` file and named according to the corresponding program.
   - Example: The plot for the code above is saved as `basic_plot.png` in the `Plots` folder.

3. **Descriptions_Examples**:
   - This folder contains text files that provide explanations for functions used till now. Each file is named according to the library the function belongs to and name of the function.
   - Example: matplotlib_pyplot_plot.txt contains description and example for the `plot` function of the `myplotlib.pyplot` library.

## How to Use

- Clone or download this repository.
- Navigate to the folder containing the code examples.
- Run the Python scripts to generate plots.
- Refer to the `Explanations` folder for a detailed breakdown of how each script works.
- The generated plots will be saved in the `Plots` folder.
- The descriptions of the functions used are saved in the `Descriptions_Examples` folder.

## Progress Tracking

As I continue learning and experimenting with Matplotlib, I will update this repository with more complex visualizations and explanations.
Stay tuned for new additions!
