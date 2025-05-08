import sys
import os
import grpc
import gradio as gr
from grpc_api.generated import text2image_pb2, text2image_pb2_grpc

# Add the project root to the Python path (only once)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# gRPC client setup
def generate_image_from_prompt(prompt, model_name, output_dir, output_name):
    # Set up the gRPC channel
    channel = grpc.insecure_channel('localhost:50051')
    stub = text2image_pb2_grpc.TextToImageServiceStub(channel)

    # Prepare the request message
    request = text2image_pb2.GenerateImageRequest(
        prompt=prompt,
        model_name=model_name,
        output_dir=output_dir,
        output_name=output_name
    )

    # Call the gRPC API
    response = stub.GenerateImageFromPrompt(request)
    return response.output_path

def launch_gradio_interface():
    # Define the Gradio interface
    gr.Interface(
        fn=generate_image_from_prompt,
        inputs=[
            gr.Textbox(label="Enter Text Prompt"),  # User enters a text prompt
            gr.Dropdown(["stable-diffusion-v1-4", "stable-diffusion-xl-base-1.0"], label="Select Model"),  # Model selection
            gr.Textbox(label="Output Directory", value="outputs"),  # Output directory (default 'outputs')
            gr.Textbox(label="Output File Name", value="output.png")  # Output file name (default 'output.png')
        ],
        outputs="text",  # Display the output image path as text
        title="Text-to-Image Generation",  # Title of the Gradio interface
        description="Select the model, specify the prompt, output directory, and image name."  # Interface description
    ).launch(server_name="0.0.0.0", server_port=7860)  # Launch the Gradio interface
