from api_client import ask_monika

print("Local Monika API Test")
print("Type 'quit' to exit.\n")

while True:
    text = input("You: ")
    if text.lower() == "quit":
        break
    try:
        print("\nMonika:", ask_monika(text), "\n")
    except Exception as e:
        print("\nERROR:", e, "\n")
