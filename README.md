# Deploying [HuggingFaceH4/starchat-alpha](https://huggingface.co/HuggingFaceH4/starchat-alpha) Large Language Model on AWS EC2 Instance

## Table of Contents
1. [Choosing an AMI and Instance](#choosing-an-ami-and-instance)
2. [Setting up the Environment](#setting-up-the-environment)
3. [Dockerization](#dockerization)

## Choosing an AMI and Instance <a name="choosing-an-ami-and-instance"></a>
I've chosen the AMI "Deep Learning AMI GPU PyTorch 2.0.0 (Ubuntu 20.04) 20230530" and the instance type "g5.4xlarge", which comes with a 24 GiB GPU. This is because the model requires approximately 20GiB of GPU memory to run it in 8-bit mode.

## Setting up the Environment <a name="setting-up-the-environment"></a>

First, we need to activate the preinstalled virtual environment, that comes with Docker by default with our chosen AMI.

```bash
source activate pytorch
```

Next, we clone the repository and navigate into the folder:

```bash
git clone https://github.com/SaturdaysAI/chatbot-docker-server.git
cd chatbot-docker-server/
```

Next, we download the model locally:

```bash
pip install huggingface_hub
python download_model.py
```

The `pip install huggingface_hub` command installs the Hugging Face hub, a Python library that allows you to download and use models from Hugging Face. `python download_model.py` runs the Python script that downloads the model into a folder named "model" in the current directory.

## Dockerization <a name="dockerization"></a>

Now we need to create an image from the Dockerfile. We do this by running the following command:

```bash
docker build --tag chatbot-docker .
```

The `docker build --tag chatbot-docker .` command builds a Docker image from the Dockerfile located in the current directory and tags it as "chatbot-docker".

Once the image is created, we can verify it with the following command:

```bash
docker images
```

This command lists all Docker images currently on your machine.

The output should be something like this:

|REPOSITORY|TAG|IMAGE ID|CREATED|SIZE|
|---|---|---|---|---|
|chatbot-docker|latest|3f8763f1593a|3 minutes ago|8.41GB|

Now we can run the image in a container with the following command:

```bash
docker run -d -p 5000:5000/tcp --gpus all --mount type=bind,src=/home/ubuntu/chatbot-docker-server/model,dst=/model chatbot-docker:latest
```

The `docker run -d --gpus all --mount type=bind,src=/home/ubuntu/chatbot-docker-server/model,dst=/model chatbot-docker:latest` command runs a Docker container in detached mode (`-d`), enabling access to all GPUs (`--gpus all`), and binds the "model" directory from your local machine to the "/model" directory inside the Docker container (`--mount type=bind,src=...dst=...`).