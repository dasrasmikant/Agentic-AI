# import sys
# sys.path.append("E:/Rasmikant/projects/2025/analyst-agent/backend2/app/crews/lang-graph-chatbot")

from langchain.schema import HumanMessage
from app.crews.lang_graph_chatbot.graph.chat_graph import graph
def main():
    print ("This is the main entry point for the LangGraph Chatbot application.")
    
    # Starting state
    initial_state = {"messages": [HumanMessage(content="Hi! Who are you?")]}

    # Run graph
    final_state = graph.invoke(initial_state)

    # See result
    for msg in final_state["messages"]:
        print(f"{msg.type}: {msg.content}")

    
if __name__ == "__main__":
    main()