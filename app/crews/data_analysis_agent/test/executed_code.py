df_result = df.dropna(subset=['Circle_Name', 'Dist_Name'])
df_result = df_result.groupby(['Circle_Name', 'Dist_Name']).size().reset_index(name='Transaction_Count')