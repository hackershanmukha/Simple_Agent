import gradio as gr
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def chat(message):
    response = model.generate_content(message)
    return response.text

demo = gr.Interface(
    fn=chat,
    inputs="textbox",
    outputs="textbox",
    title="Simple Gemini Agent"
)

demo.launch()