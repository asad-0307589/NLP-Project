# 🖼️ Text-to-Image Microservice

A microservice that generates images from text prompts using state-of-the-art diffusion models like **Stable Diffusion** and **Stable Diffusion XL**. It exposes a gRPC API for production use and a Gradio web UI for local testing and demos.

## 🚀 Features

- 🔮 Text-to-image generation using Stable Diffusion & SDXL  
- 🧠 GPU acceleration (via CUDA) for faster inference  
- 🛠️ gRPC-based backend for scalable microservice architecture  
- 🌐 Gradio interface for local testing and visualization  

## 🧰 Prerequisites

- [Docker](https://www.docker.com/)  
- [Python 3.9+](https://www.python.org/)  
- NVIDIA GPU + CUDA (optional but recommended for performance)  

## 📦 Installation

### 🔁 Clone the Repository
```bash
git clone <your_repo_url>
cd text2image_microservice
```

### 🐍 Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

## 🐳 Run with Docker
```bash
docker build -t text2image-service .
docker run -p 7860:7860 text2image-service
```

## 🧪 Run Locally (Without Docker)
```bash
python app.py
```
> This will start the Gradio interface at `http://localhost:7860`

## 📡 gRPC API

The backend supports gRPC calls for integration into other services. See the `proto/` folder for `.proto` definitions and usage examples.

## 📁 Project Structure
```
text2image_microservice/
├── app.py                  # Main application
├── models/                 # Model loading and generation code
├── proto/                  # gRPC definitions
├── interface/              # Gradio interface files
├── requirements.txt        # Python dependencies
└── Dockerfile              # Docker container setup
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments

- [Stability AI](https://stability.ai/) for the diffusion models  
- [Gradio](https://www.gradio.app/) for the web interface  
- [grpc.io](https://grpc.io/) for the API layer
