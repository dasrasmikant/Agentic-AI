from crewai.tools import tool
import pandas as pd
import tempfile
import subprocess
import uuid
import os
import sys
from app.crews.data_analysis_agent.lib.csv_context import CSVContext, ResultContext, CodeContext,DataPathContext,ChartCodeContext

@tool("Python Chart Generator")
def generate_chart_from_code() -> str:
    """
    Executes Python code to generate chart(s) from DataFrame.Use this tool if you want to generate charts from the DataFrame.
    Returns JPG chart path and logs.
    """
    code = CodeContext.get_code()
    chart_code=ChartCodeContext.get_code()
    run_id = str(uuid.uuid4())
    dir_path=f"static/crew_chart_{run_id}"   
    # temp_dir = tempfile.mkdtemp(prefix=f"crew_chart_{run_id}_")
    os.makedirs(dir_path, exist_ok=True)
    temp_dir = dir_path

    code_file = os.path.join(temp_dir, "chart_code.py")
    input_csv = os.path.join(temp_dir, "input.csv")
    chart_path = os.path.join(temp_dir, "chart.jpg")
    stdout_file = os.path.join(temp_dir, "stdout.txt")
    stderr_file = os.path.join(temp_dir, "stderr.txt")

    dataframe = CSVContext.get_result()    
    dataframe.to_csv(input_csv, index=False)

    wrapped_code = f"""
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

df = pd.read_csv(r"{input_csv}")
{code}
{chart_code}



plt.savefig(r"{chart_path}")

# if fig is not None:    
#     fig.write_image(r"{chart_path}")
# else:
#     plt.savefig(r"{chart_path}")
    # buf = BytesIO()
    # plt.savefig(buf, format='png')
    # buf.seek(0)
    # base64_img = base64.b64encode(buf.read()).decode('utf-8')
    # img_markdown = f"![chart](data:image/png;base64,base64_img)"
"""

    with open(code_file, "w") as f:
        f.write(wrapped_code)

    subprocess.run([sys.executable, code_file],
                   stdout=open(stdout_file, "w"),
                   stderr=open(stderr_file, "w"))
    DataPathContext.set_path(chart_path)
    stdout = open(stdout_file).read()
    stderr = open(stderr_file).read()

    return str({
        "stdout": stdout,
        "stderr": stderr,
        "chart_path": chart_path if os.path.exists(chart_path) else None
    })
