# Text-to-Image Microservice

This is a microservice that generates images from text prompts using models like Stable Diffusion and Stable Diffusion XL. The backend uses gRPC to handle requests, and a Gradio interface allows for easy testing and interaction with the models.

## Prerequisites

- Docker
- Python 3.9 or later
- CUDA (optional, for GPU support)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repo_url>
   cd text2image_microservice
