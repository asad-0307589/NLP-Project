import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grpc_api.generated import text2image_pb2, text2image_pb2_grpc
from app.text2image import TextToImageGenerator

class TextToImageServicer(text2image_pb2_grpc.TextToImageServiceServicer):
    def __init__(self):
        self.generator = TextToImageGenerator()

    def GenerateImageFromPrompt(self, request, context):
        try:
            output_path = self.generator.generate(
                prompt=request.prompt,
                model_name=request.model_name,
                output_dir=request.output_dir,
                output_name=request.output_name
            )
            return text2image_pb2.GenerateImageResponse(output_path=output_path)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return text2image_pb2.GenerateImageResponse(output_path="")
