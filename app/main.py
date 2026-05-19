from app.agent import ask_ollama, EXPECTED_TEST_RESPONSE
from app.config import AGENT_NAME, OLLAMA_MODEL, ENABLE_THINKING


def run():
    print(f"{AGENT_NAME} is starting...")
    print(f"Using local model: {OLLAMA_MODEL}")
    print(f"Thinking enabled: {ENABLE_THINKING}")

    user_prompt = f"Return only this exact text: {EXPECTED_TEST_RESPONSE}"

    response = ask_ollama(user_prompt)

    print("\nAgent response:")
    print(response)


if __name__ == "__main__":
    run()
