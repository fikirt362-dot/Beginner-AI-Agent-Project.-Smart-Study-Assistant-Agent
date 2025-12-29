# brain.py

from tools import calculator, explain

def think(user_input):
    user_input = user_input.lower()

    if user_input.startswith("calculate"):
        expression = user_input.replace("calculate", "").strip()
        return calculator(expression)

    elif user_input.startswith("explain"):
        topic = user_input.replace("explain", "").strip()
        return explain(topic)

    elif "hello" in user_input:
        return "Hello! I am your study assistant."

    elif "bye" in user_input:
        return "Goodbye! Study well."

    else:
        return "I can explain topics or calculate. Try: explain python"
