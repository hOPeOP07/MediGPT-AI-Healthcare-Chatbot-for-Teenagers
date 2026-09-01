import gradio as gr
from backend import answer_question


def medigpt_reply(message, history):
    return answer_question(message)


with gr.Blocks(title="MEDIGPT") as demo:

    gr.Markdown("# 🧠 MEDIGPT")
    gr.Markdown("### Your Teen Healthcare Assistant")

    gr.ChatInterface(
        fn=medigpt_reply,
        textbox=gr.Textbox(placeholder="Ask about sleep, stress, diet, puberty..."),
        chatbot=gr.Chatbot(height=500)
    )

import os

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)
