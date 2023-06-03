from huggingface_hub import snapshot_download
dir="./model/"
# This configuration avoid having symlinks
snapshot_download(repo_id="HuggingFaceH4/starchat-alpha", local_dir=dir, local_dir_use_symlinks=False, force_download=True)