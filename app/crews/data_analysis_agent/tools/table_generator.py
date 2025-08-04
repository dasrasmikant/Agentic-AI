from crewai.tools import tool
import pandas as pd
import tempfile
import subprocess
import uuid
import os
import sys
from app.crews.data_analysis_agent.lib.csv_context import CSVContext, ResultContext, CodeContext,DataPathContext

@tool("Python Table Generator")
def generate_table_from_code() -> str:
    """
    Executes Python code to generate or modify tabular data. Use this tool if you want to generate or modify tables from the DataFrame.
    Returns output CSV path and logs.
    """
    code = CodeContext.get_code()   
    run_id = str(uuid.uuid4())
    # temp_dir = tempfile.mkdtemp(prefix=f"crew_table_{run_id}_")
    dir_path=f"static/crew_table_{run_id}"   
    # temp_dir = tempfile.mkdtemp(prefix=f"crew_chart_{run_id}_")
    os.makedirs(dir_path, exist_ok=True)
    temp_dir = dir_path
    code_file = os.path.join(temp_dir, "table_code.py")
    input_csv = os.path.join(temp_dir, "input.csv")
    output_csv = os.path.join(temp_dir, "output.csv")
    stdout_file = os.path.join(temp_dir, "stdout.txt")
    stderr_file = os.path.join(temp_dir, "stderr.txt")

    dataframe = CSVContext.get_result()
    dataframe.to_csv(input_csv, index=False)

    wrapped_code = f"""
import pandas as pd
import subprocess
import sys

def ensure_libs(libs):
    for lib in libs:
        try:
            __import__(lib)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

ensure_libs(["pandas"])

df = pd.read_csv(r"{input_csv}")
{code}
df_result.to_csv(r"{output_csv}", index=False)
"""

    with open(code_file, "w") as f:
        f.write(wrapped_code)

    subprocess.run([sys.executable, code_file],
                   stdout=open(stdout_file, "w"),
                   stderr=open(stderr_file, "w"))

    stdout = open(stdout_file).read()
    stderr = open(stderr_file).read()
    DataPathContext.set_path(output_csv)
    return str({
        "stdout": stdout,
        "stderr": stderr,
        "output_csv": output_csv if os.path.exists(output_csv) else None
    })
