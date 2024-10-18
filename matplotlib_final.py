import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset/data.csv')

print("Information About Dataset: \n")
print(f"Dataset Head: {df.head()}\n")
print(f"Dataset Tail: {df.tail()}\n")
print(f"Dataset Shape: {df.shape}\n")
print(f"Dataset Columns: {df.columns}\n")
print(f"Dataset Index: {df.index}\n")
print(f"Dataset Info: {df.info()}\n")
print(f"Dataset Describe: {df.describe()}\n")
print(f"Dataset Null Values: {df.isnull().sum()}\n")
print(f"Dataset Duplicates: {df.duplicated().sum()}\n")
print(f"Dataset Correlation: {df.corr()}\n")
print(f"Dataset Sample: {df.sample(5)}\n")

df['Year'] = df['Date'] // 100
df['Month'] = df['Date'] % 100

df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'].astype(str) + '-01')
# df.drop(columns=['Year', 'Month'], inplace=True)

print(df.head())


# Line Plotting
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Anomaly'], color='red', linewidth=1.5)

plt.title('Global Temperature Anomalies (1880 - 2024)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature Anomaly (°C)', fontsize=12)

plt.grid(True)

plt.tight_layout()
plt.show()


# Scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(df['Date'], df['Anomaly'], color='blue', alpha=0.6, edgecolor='k')

plt.title('Scatter Plot of Global Temperature Anomalies (1880 - 2024)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature Anomaly (°C)', fontsize=12)

plt.grid(True)

plt.tight_layout()
plt.show()


# Histogram plot
plt.figure(figsize=(12, 6))
plt.hist(df['Anomaly'], bins=30, color='orange', edgecolor='black', alpha=0.7)

plt.title('Histogram of Global Temperature Anomalies', fontsize=16)
plt.xlabel('Temperature Anomaly (°C)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

plt.grid(axis='y', alpha=0.75)

plt.tight_layout()
plt.show()


# Box plot
plt.figure(figsize=(8, 6))
plt.boxplot(df['Anomaly'], vert=True, patch_artist=True, boxprops=dict(facecolor='lightblue'))

plt.title('Box Plot of Global Temperature Anomalies', fontsize=16)
plt.ylabel('Temperature Anomaly (°C)', fontsize=12)

plt.grid(axis='y', alpha=0.75)

plt.tight_layout()
plt.show()


# Heatmap plot
import seaborn as sns

heatmap_data = df.pivot_table(values='Anomaly', index='Year', columns='Month')

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='coolwarm', annot=False, cbar_kws={'label': 'Temperature Anomaly (°C)'})

plt.title('Heatmap of Global Temperature Anomalies (1880 - 2024)', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Year', fontsize=12)

plt.tight_layout()
plt.show()


# Animated plot
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(12, 6))
line, = ax.plot([], [], color='red', linewidth=2)

ax.set_xlim(df['Date'].min(), df['Date'].max())
ax.set_ylim(df['Anomaly'].min() - 0.5, df['Anomaly'].max() + 0.5)
ax.set_title('Animated Global Temperature Anomalies (1880 - 2024)', fontsize=16)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Temperature Anomaly (°C)', fontsize=12)
ax.grid(True)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    x = df['Date'][:frame]
    y = df['Anomaly'][:frame]
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(df), init_func=init, blit=True, interval=10)

plt.tight_layout()
plt.show()