from dotenv import load_dotenv
import os
load_dotenv()
key=os.getenv("GROQ_API_KEY")
if key:
    print("GROQ API key loaded succesfully")
else:
    print("API key not found")
