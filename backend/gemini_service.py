import os
import time

from dotenv import load_dotenv
from fastapi import HTTPException
from google import genai

load_dotenv()


def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=503,
            detail="GEMINI_API_KEY is missing. Please set it in your environment or .env file before generating a document."
        )

    return genai.Client(api_key=api_key)


def generate_legal_document(document_type, user_details):

    prompt = f"""
Generate a professional legal document draft.

Document Type:
{document_type}

User Details:
{user_details}

Create a clear, well-structured document with appropriate
sections, clauses, dates, parties, and signature sections
where applicable.

Important:
This is an AI-generated draft and must be reviewed by
a qualified legal professional before use.
"""

    client = get_gemini_client()
    max_retries = 4

    for attempt in range(max_retries):

        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            error_text = str(e)

            # Retry temporary Gemini server/capacity errors
            if "503" in error_text or "UNAVAILABLE" in error_text:

                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt

                    print(
                        f"Gemini temporarily unavailable. "
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

                else:
                    raise Exception(
                        "Gemini is currently experiencing high demand. "
                        "Please try again in a few minutes."
                    )

            else:
                raise e