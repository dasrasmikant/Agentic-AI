import sys
sys.path.append("E:/Rasmikant/projects/2025/analyst-agent/backend2/app/crews/data_analysis_agent")
from app.crews.data_analysis_agent.crew.crew_setup import (
    data_loading_crew,
    data_analysis_crew,
    table_generation_crew,
    chart_generation_crew
)
from app.crews.data_analysis_agent.lib.log_buffer import log_queue
from app.crews.data_analysis_agent.lib.csv_context import CSVContext, ResultContext,DataPathContext
import pandas as pd

import asyncio
sleep_time = 0.1 # Adjust this value as needed


async def run_pipeline(user_question: str):
    # print(f"\n User Question: {user_question}")
    result={ "success": False,"response": "No result returned from pipeline."}
    await log_queue.put("Data Loading Started...")
    await asyncio.sleep(sleep_time)  # Simulate loading time
    # # Step 1: Data Loading
    # await log_queue.put("Loading Data...")
    loading_crew = data_loading_crew(user_question)
    load_result = loading_crew.kickoff().raw
    await log_queue.put(f"Data loading Completed\n {load_result}")
    await asyncio.sleep(sleep_time)

    if  CSVContext.get_result() is None :
        await log_queue.put("Data loading failed or returned no data.")
        await asyncio.sleep(sleep_time)
        exit()
    else:
        await log_queue.put("Proceeding for analysis...")
        await asyncio.sleep(sleep_time)
        # print(" Data loaded successfully. Proceeding to analysis...")

    # Step 2: Data Analysis
    
    analysis_crew = data_analysis_crew(user_question)
    analysis_result = analysis_crew.kickoff()
    await log_queue.put(f"Data analysis Completed\n\n{analysis_result.raw}")
    await asyncio.sleep(sleep_time)
    action=analysis_result.raw   
    # Step 3: Decision Making Based on Analysis Results   

    if action.lower().strip() == "table_generation":
        await log_queue.put("Preparing to generate table...")
        await asyncio.sleep(sleep_time)
        table_crew = table_generation_crew(user_question)
        table_result = table_crew.kickoff()
        tbl=f"Table Generation Result:\n\n {table_result}"
        # Extract data from the CSV file at the path provided by DataPathContext
        csv_path = DataPathContext.get_path()
        try:
            df = pd.read_csv(csv_path)
            # Convert DataFrame to markdown format
            md_table = df.to_markdown(index=False)
            tbl += f"\n CSV Data Preview:\n {md_table}"
        except Exception as e:
            tbl += f"\n\nFailed to load CSV data: {e}"
        await log_queue.put(f"Table generation result")
        await asyncio.sleep(sleep_time)
        result={ "success": True,"response": tbl,"img": ""}

    elif action.lower().strip() == "chart_generation":
        await log_queue.put("Preparing to generate chart...")
        await asyncio.sleep(sleep_time)
        chart_crew = chart_generation_crew(user_question)
        chart_result = chart_crew.kickoff()
        cht=f"Chart Generation Result:\n\n {chart_result}\n"
        chart_path = DataPathContext.get_path()
        # try:
            # with open(chart_path, "rb") as img_file:
                # img_data = img_file.read()
                # base64_img = base64.b64encode(img_data).decode('utf-8')
                # cht += f" ![chart](data:image/jpg;base64,{base64_img})"              
               
        # except Exception as e:
        #     result = {
        #         "success": False,
        #         "response": f"\n\nFailed to load image: {e}"
        #     }
        img_url= f"/{chart_path}"
        await log_queue.put(f"Displaying the chart...") 
        await asyncio.sleep(sleep_time)    
        result={ "success": True,"response": cht, "img": f"http://localhost:8000{img_url}"}

    else:
        await log_queue.put(f"Unknown action received: '{action}'")
        await asyncio.sleep(sleep_time)
        result={ "success": False,"response": f"Unknown action: {action}"}
    return result