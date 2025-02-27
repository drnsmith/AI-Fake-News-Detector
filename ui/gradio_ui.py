import gradio as gr
from app.fact_checker import check_fact
from app.bias_analysis import analyse_bias

def process_text(content):
    credibility = check_fact(content)
    bias = analyse_bias(content)
    return credibility, bias

iface = gr.Interface(
    fn=process_text,
    inputs=gr.Textbox(label="Enter News Article or Text"),
    outputs=[gr.Textbox(label="Credibility Score"), gr.Textbox(label="Bias Analysis")],
    title="AI Fake News Detector",
)

iface.launch()
