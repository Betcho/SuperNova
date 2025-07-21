import gradio as gr
from PIL import Image

def generate_video(prompt, image):
    # Simulated placeholder for actual video generation logic
    return f"🎬 Video generated from prompt: '{prompt}' and uploaded image!"

with gr.Blocks() as demo:
    gr.Markdown("## 🎥 SuperNova AI - Text & Image to Video Generator")

    with gr.Row():
        prompt = gr.Textbox(label="Enter Description", placeholder="e.g. A futuristic city at sunset", lines=2)
        image = gr.Image(label="Upload an Image", type="filepath")

    generate_button = gr.Button("Generate Video")
    output = gr.Textbox(label="Generation Output")

    generate_button.click(fn=generate_video, inputs=[prompt, image], outputs=output)

demo.launch()