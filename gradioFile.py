import gradio as gr
import diffusion_inference as df

interface = gr.Interface(
    fn=df.generate_image,
    inputs="text",
    outputs="image"
)

interface.launch(auth=("zuma", "zuma"))
