from app.crews.data_analysis_agent.pipeline import run_pipeline
if __name__ == "__main__":
    user_question = input("Enter your question: ")
    run_pipeline(user_question)
