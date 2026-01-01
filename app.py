import sys
from decision import decide
from response import render_response

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py \"<your question>\"")
        sys.exit(1)

    user_question = sys.argv[1]

    print("REQUEST RECEIVED")
    print(f"Question: {user_question}")

    decision = decide(user_question)
    output = render_response(decision)

    print(output)

if __name__ == "__main__":
    main()