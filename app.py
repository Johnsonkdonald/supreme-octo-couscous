import gradio as gr
from generator import generate_image

def prompt_to_image(prompt):
    image = generate_image(prompt)
    return image

gr.Interface(
    fn=prompt_to_image,
    inputs="text",
    outputs="image",
    title="Creative AI Generator",
    description="Type a prompt like 'Design a wedding dress for a moon queen'."
).launch()
