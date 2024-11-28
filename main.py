from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def main():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Write a one paragraph story about 'Ryan' learning Python and OpenAI!"}
        ]
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()