import sys
import os
# Add parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from tools.python_executor import python_executor
from app.dependencies.csv_context import CSVContext,ResultContext

# Load CSV into shared context
df = pd.read_csv("E:\\Rasmikant\\projects\\2025\\analyst-agent\\backend2\\app\\crews\\data_analysis_agent\\data\\sales_data.csv")  # Adjust path as needed
CSVContext.set_result(df)

# Define your code to run
code = """
summary = df.describe()
print(summary)
result = summary  # Store result in ResultContext
"""

# Run tool
tool_output = python_executor(code)
print("\n🖨️ Tool Output:\n", tool_output)

# Get stored result
stored_result = ResultContext.get_result()
print("\n📦 Stored Result from Execution:\n", stored_result)
