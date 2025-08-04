
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

df = pd.read_csv(r"static/crew_table_4b87ee00-f052-42a2-9109-c2ecd0f29e47\input.csv")
df_result = df.dropna(subset=['Circle_Name', 'Dist_Name'])
df_result = df_result.groupby(['Circle_Name', 'Dist_Name']).size().reset_index(name='Transaction_Count')
df_result.to_csv(r"static/crew_table_4b87ee00-f052-42a2-9109-c2ecd0f29e47\output.csv", index=False)
