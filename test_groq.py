import os
from dotenv import load_dotenv
load_dotenv()

print("Importing ChatGroq...")
from langchain_groq import ChatGroq
print("ChatGroq imported.")

print("Initializing model...")
model = ChatGroq(model="llama-3.1-8b-instant")
print("Model initialized.")

print("Calling model...")
try:
    response = model.invoke("Hello!")
    print("Response received:")
    print(response.content)
except Exception as e:
    print("Error during invoke:", e)
