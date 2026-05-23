import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load dataset
df = pd.read_csv('sales_dashboard_data.csv')

# Display dataset info
print(df.head())

# Seaborn Theme
sns.set(style='darkgrid')

# Example Visualization
plt.figure(figsize=(10,5))
sns.boxplot(x=df.columns[0], y=df.columns[1], data=df)
plt.title('Sample Box Plot')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visualizations/boxplot.png')
plt.show()

# Interactive Plotly Chart
fig = px.scatter(df, x=df.columns[0], y=df.columns[1],
                 title='Interactive Scatter Plot')

fig.show()
