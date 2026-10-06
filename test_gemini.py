import os
import traceback
from dotenv import load_dotenv
from google import genai

print("Starting Gemini test...")

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: GEMINI_API_KEY was not found.")
    raise SystemExit(1)

print("API key found.")
print("Key length:", len(api_key))

try:
    client = genai.Client(api_key=api_key)

    print("Sending test request to Gemini...")

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Reply with exactly: Gemini API works"
    )

    print("\n========== SUCCESS ==========")
    print("Response:")
    print(response.text)
    print("=============================")

except Exception as e:
    print("\n========== GEMINI ERROR ==========")
    print("Error type:", type(e).__name__)
    print("Error:", str(e))
    print("\nFull traceback:")
    traceback.print_exc()
    print("==================================")

input("\nPress Enter to close...")