# app/text2image.py
import os
import torch
from diffusers import StableDiffusionPipeline, StableDiffusionXLPipeline
import grpc
from grpc_api.generated import text2image_pb2_grpc
from grpc_api.generated import text2image_pb2

class TextToImageGenerator(text2image_pb2_grpc.TextToImageServiceServicer):
    def __init__(self):
        self.pipe = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def load_model(self, model_name: str):
        model_dir = os.path.join(os.path.dirname(__file__), "..", "models", model_name)

        if not os.path.exists(model_dir):
            raise FileNotFoundError(f"Model directory '{model_dir}' does not exist.")
        if model_name == "stable-diffusion-v1-4":
            self.pipe = StableDiffusionPipeline.from_pretrained(
                model_dir,
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
            )
        elif model_name == "stable-diffusion-xl-base-1.0":
            self.pipe = StableDiffusionXLPipeline.from_pretrained(
                model_dir,
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                safety_checker=None
            )
        else:
            raise ValueError(f"Unsupported model: {model_name}")

        self.pipe = self.pipe.to(self.device)

    def generate(self, prompt: str, model_name: str, output_dir: str = "outputs", output_name: str = "output.png") -> str:
        """
        Generate an image based on the given prompt, model, output directory, and output name.

        :param prompt: The text prompt to generate the image from.
        :param model_name: The model name to use ('stable-diffusion-v1-4' or 'stable-diffusion-xl-base-1.0').
        :param output_dir: The directory where the output image will be saved.
        :param output_name: The name of the output image file.
        :return: The path to the saved image.
        """
        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Load the selected model
        self.load_model(model_name)

        # Generate the image
        image = self.pipe(prompt).images[0]

        # Save the image to the specified path
        output_path = os.path.join(output_dir, output_name)
        image.save(output_path)

        return output_path

    def GenerateImageFromPrompt(self, request, context):
        """
        Handle incoming gRPC requests to generate images based on the provided prompt.
        """
        try:
            # Generate the image
            image_path = self.generate(request.prompt, request.model_name, request.output_dir, request.output_name)
            return text2image_pb2.GenerateImageResponse(output_path=image_path)
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return text2image_pb2.GenerateImageResponse(output_path="")
