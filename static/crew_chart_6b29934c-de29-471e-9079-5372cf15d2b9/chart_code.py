
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

df = pd.read_csv(r"static/crew_chart_6b29934c-de29-471e-9079-5372cf15d2b9\input.csv")
import pandas as pd
import matplotlib.pyplot as plt

# 1. Convert 'Transcation_Date' to datetime objects.
df['Transcation_Date'] = pd.to_datetime(df['Transcation_Date'])

# 2. Extract the year from 'Transcation_Date' to create a 'Year' column.
df['Year'] = df['Transcation_Date'].dt.year

# 3. Group the data by 'Year' and sum the 'Royalty_Amount' for each year.
df_yearly_royalty = df.groupby('Year')['Royalty_Amount'].sum().reset_index()

# 4. Filter the data to include only years 2023 and 2024.
df_result = df_yearly_royalty[df_yearly_royalty['Year'].isin([2023, 2024])]

# 5. Calculate the percentage change in 'Royalty_Amount' between 2023 and 2024
#    to determine if it increased or decreased.
if 2023 in df_result['Year'].values and 2024 in df_result['Year'].values:
    royalty_2023 = df_result[df_result['Year'] == 2023]['Royalty_Amount'].iloc[0]
    royalty_2024 = df_result[df_result['Year'] == 2024]['Royalty_Amount'].iloc[0]

    if royalty_2023 != 0:
        percentage_change = ((royalty_2024 - royalty_2023) / royalty_2023) * 100
        status = "increased" if percentage_change > 0 else ("decreased" if percentage_change < 0 else "remained the same")
        print(f"Royalty amount {status} by {percentage_change:.2f}% from 2023 to 2024.")
    else:
        print("Cannot calculate percentage change: Royalty amount in 2023 is zero.")
elif 2023 not in df_result['Year'].values:
    print("Data for 2023 is not available to calculate percentage change.")
elif 2024 not in df_result['Year'].values:
    print("Data for 2024 is not available to calculate percentage change.")
else:
    print("Data for both 2023 and 2024 is not available to calculate percentage change.")


# 6. Create a bar chart to visualize the total royalty collection for 2023 and 2024.
if not df_result.empty:
    plt.figure(figsize=(8, 6))
    # Ensure Year is treated as categorical for plotting
    plt.bar(df_result['Year'].astype(str), df_result['Royalty_Amount'], color=['skyblue', 'lightcoral'])
    plt.xlabel('Year')
    plt.ylabel('Total Royalty Amount')
    plt.title('Total Royalty Collection for 2023 and 2024')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
else:
    print("No data available for 2023 and 2024 to create a chart.")
import pandas as pd
import matplotlib.pyplot as plt

# 1. Convert 'Transcation_Date' to datetime objects.
df['Transcation_Date'] = pd.to_datetime(df['Transcation_Date'])

# 2. Extract the year from 'Transcation_Date' to create a 'Year' column.
df['Year'] = df['Transcation_Date'].dt.year

# 3. Group the data by 'Year' and sum the 'Royalty_Amount' for each year.
df_yearly_royalty = df.groupby('Year')['Royalty_Amount'].sum().reset_index()

# 4. Filter the data to include only years 2023 and 2024.
df_result = df_yearly_royalty[df_yearly_royalty['Year'].isin([2023, 2024])]

# 5. Calculate the percentage change in 'Royalty_Amount' between 2023 and 2024
#    to determine if it increased or decreased.
# This part is for printing analysis, not for chart generation directly.
if 2023 in df_result['Year'].values and 2024 in df_result['Year'].values:
    royalty_2023 = df_result[df_result['Year'] == 2023]['Royalty_Amount'].iloc[0]
    royalty_2024 = df_result[df_result['Year'] == 2024]['Royalty_Amount'].iloc[0]

    if royalty_2023 != 0:
        percentage_change = ((royalty_2024 - royalty_2023) / royalty_2023) * 100
        status = "increased" if percentage_change > 0 else ("decreased" if percentage_change < 0 else "remained the same")
        # print(f"Royalty amount {status} by {percentage_change:.2f}% from 2023 to 2024.")
    # else:
        # print("Cannot calculate percentage change: Royalty amount in 2023 is zero.")
# elif 2023 not in df_result['Year'].values:
    # print("Data for 2023 is not available to calculate percentage change.")
# elif 2024 not in df_result['Year'].values:
    # print("Data for 2024 is not available to calculate percentage change.")
# else:
    # print("Data for both 2023 and 2024 is not available to calculate percentage change.")


# 6. Create a bar chart to visualize the total royalty collection for 2023 and 2024.
if not df_result.empty:
    fig, ax = plt.subplots(figsize=(8, 6))
    # Ensure Year is treated as categorical for plotting
    ax.bar(df_result['Year'].astype(str), df_result['Royalty_Amount'], color=['skyblue', 'lightcoral'])
    ax.set_xlabel('Year')
    ax.set_ylabel('Total Royalty Amount')
    ax.set_title('Total Royalty Collection for 2023 and 2024')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    # plt.show() # Removed as per constraint
# else:
    # print("No data available for 2023 and 2024 to create a chart.")




plt.savefig(r"static/crew_chart_6b29934c-de29-471e-9079-5372cf15d2b9\chart.jpg")

# if fig is not None:    
#     fig.write_image(r"static/crew_chart_6b29934c-de29-471e-9079-5372cf15d2b9\chart.jpg")
# else:
#     plt.savefig(r"static/crew_chart_6b29934c-de29-471e-9079-5372cf15d2b9\chart.jpg")
    # buf = BytesIO()
    # plt.savefig(buf, format='png')
    # buf.seek(0)
    # base64_img = base64.b64encode(buf.read()).decode('utf-8')
    # img_markdown = f"![chart](data:image/png;base64,base64_img)"
