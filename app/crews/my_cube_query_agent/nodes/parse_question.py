def parse_question_node(state):
    question = getattr(state, "question", "") or ""
    return {"question": question}
