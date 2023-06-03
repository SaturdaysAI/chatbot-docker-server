source activate pytorch ya tiene docker instalado

Empiezo clonando el repo y haciendo cd :

git clone https://github.com/SaturdaysAI/chatbot-docker-server.git
cd chatbot-docker-server/

Luego instalo huggingface_hub para  descargar el modelo (este paso se puede saltar cambiando la variable...)

docker build --tag chatbot-docker .

docker images

REPOSITORY       TAG       IMAGE ID       CREATED         SIZE
chatbot-docker   latest    3f8763f1593a   3 minutes ago   8.41GB

docker run chatbot-docker

