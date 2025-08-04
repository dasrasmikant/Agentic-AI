
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import subprocess
import sys
import kaleido

def ensure_libs(libs):
    for lib in libs:
        try:
            __import__(lib)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

ensure_libs(["pandas", "matplotlib", "seaborn"])

df = pd.read_csv(r"static/crew_chart_be3e62e7-6b9f-4307-b8c7-3de76f7228a9\input.csv")
import pandas as pd

# Step 1: Convert 'Transcation_Date' to datetime format.
df['Transcation_Date'] = pd.to_datetime(df['Transcation_Date'])

# Step 2: Filter the DataFrame to include only transactions between '2023-01-01' and '2024-12-31'.
start_date = '2023-01-01'
end_date = '2024-12-31'
df_filtered = df[(df['Transcation_Date'] >= start_date) & (df['Transcation_Date'] <= end_date)].copy()

# Step 3: Sort the filtered DataFrame by 'Transcation_Date' to ensure correct cumulative sum calculation.
df_filtered = df_filtered.sort_values(by='Transcation_Date')

# Step 4: Calculate the cumulative sum of 'Royalty_Amount' for the filtered data.
df_filtered['Cumulative_Royalty_Amount'] = df_filtered['Royalty_Amount'].cumsum()

# Assign the final processed DataFrame to df_result
df_result = df_filtered
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Convert 'Transcation_Date' to datetime format.
df['Transcation_Date'] = pd.to_datetime(df['Transcation_Date'])

# Step 2: Filter the DataFrame to include only transactions between '2023-01-01' and '2024-12-31'.
start_date = '2023-01-01'
end_date = '2024-12-31'
df_filtered = df[(df['Transcation_Date'] >= start_date) & (df['Transcation_Date'] <= end_date)].copy()

# Step 3: Sort the filtered DataFrame by 'Transcation_Date' to ensure correct cumulative sum calculation.
df_filtered = df_filtered.sort_values(by='Transcation_Date')

# Step 4: Calculate the cumulative sum of 'Royalty_Amount' for the filtered data.
df_filtered['Cumulative_Royalty_Amount'] = df_filtered['Royalty_Amount'].cumsum()

# Assign the final processed DataFrame to df_result
df_result = df_filtered

# Matplotlib code for charting
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df_result['Transcation_Date'], df_result['Cumulative_Royalty_Amount'], marker='o', linestyle='-')

ax.set_title('Cumulative Royalty Collected (Jan 2023 - Dec 2024)')
ax.set_xlabel('Transaction Date')
ax.set_ylabel('Cumulative Royalty Amount')
ax.grid(True)

# Optional: Format x-axis dates for better readability
fig.autofmt_xdate()



plt.savefig(r"static/crew_chart_be3e62e7-6b9f-4307-b8c7-3de76f7228a9\chart.jpg")

# if fig is not None:    
#     fig.write_image(r"static/crew_chart_be3e62e7-6b9f-4307-b8c7-3de76f7228a9\chart.jpg")
# else:
#     plt.savefig(r"static/crew_chart_be3e62e7-6b9f-4307-b8c7-3de76f7228a9\chart.jpg")
    # buf = BytesIO()
    # plt.savefig(buf, format='png')
    # buf.seek(0)
    # base64_img = base64.b64encode(buf.read()).decode('utf-8')
    # img_markdown = f"![chart](data:image/png;base64,base64_img)"
