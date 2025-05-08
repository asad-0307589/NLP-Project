from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="stabilityai/stable-diffusion-xl-base-1.0",
    local_dir="./models/stable-diffusion-xl-base-1.0",
    local_dir_use_symlinks=False,
    resume_download=True,
    max_workers=2
)
