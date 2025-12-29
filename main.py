# main.py

from memory import Memory
from brain import think

memory = Memory()

print("Study Agent started. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Agent: Goodbye!")
        break

    memory.add("User", user_input)

    response = think(user_input)

    memory.add("Agent", response)

    print("Agent:", response)
