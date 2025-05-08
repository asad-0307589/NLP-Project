import os
import grpc
from concurrent import futures
import time
import threading
from grpc_api.generated import text2image_pb2_grpc
from app.text2image import TextToImageGenerator
from frontend.interface import launch_gradio_interface
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'grpc_api', 'generated'))


def serve():
    # Initialize the gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Register the TextToImageService with the server
    text2image_pb2_grpc.add_TextToImageServiceServicer_to_server(
        TextToImageGenerator(), server)

    # Set the server to listen on port 50051
    server.add_insecure_port('[::]:50051')
    print("✅ gRPC server started on port 50051...")

    # Start the server
    server.start()

    try:
        while True:
            time.sleep(86400)  # Keep the server running
    except KeyboardInterrupt:
        server.stop(0)

# Start gRPC server in a separate thread
grpc_thread = threading.Thread(target=serve)
grpc_thread.start()

# Start Gradio interface on the main thread
launch_gradio_interface()
