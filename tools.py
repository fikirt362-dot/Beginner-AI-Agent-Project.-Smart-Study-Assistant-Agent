# tools.py

def calculator(expression):
    try:
        return f"Result: {eval(expression)}"
    except:
        return "Error in calculation."

def explain(topic):
    explanations = {
        "python": "Python is a programming language used for web, AI, automation, and more.",
        "ai": "AI means Artificial Intelligence. It allows machines to think and learn.",
        "loop": "A loop repeats code until a condition is met."
    }
    return explanations.get(topic.lower(), "I don't know that topic yet.")
