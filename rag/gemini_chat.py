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


    conversation = ""


    for msg in history:

        conversation += (

            f"{msg['role']}: "

            f"{msg['content']}\n"

        )


    prompt = f"""
You are an AI Business Advisor.

Your users are NOT data scientists.

They are business owners.

Use VERY SIMPLE language.

Never mention:
- embeddings
- vectors
- clustering
- machine learning
- segmentation algorithms

Always explain insights like talking to a beginner.

Use this EXACT structure:

📌 Main Finding
(1–2 sentences)

📊 What This Means
(simple explanation)

🚀 Recommended Action
(3 specific actions)

⚠️ Risk Level
(Low / Medium / High)

💡 Example
(real business example)

Keep answers:
- short
- practical
- clear
- beginner friendly

Business Data:

{context}

Previous Conversation:

{conversation}

User Question:

{question}

Generate answer.
"""


    response = model.generate_content(
        prompt
    )

    return response.text