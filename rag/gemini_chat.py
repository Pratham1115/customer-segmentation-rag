import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()


genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)


model = genai.GenerativeModel(
    "gemini-2.5-flash"
)



def ask_ai(

    context,

    question,

    history

):


    chat = ""


    for m in history:

        chat += (

            f"{m['role']}: "

            f"{m['content']}\n"

        )


    prompt = f"""

You are an expert business analyst.

Business Data:

{context}

Conversation:

{chat}

User:

{question}

Rules:

Explain clearly.

Use business language.

Give recommendations.

"""


    response = (

        model.generate_content(
            prompt
        )

    )


    return response.text