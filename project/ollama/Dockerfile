FROM ollama/ollama:latest

RUN apt-get update && apt-get install -y bash

ENV OLLAMA_HOST=0.0.0.0

ENTRYPOINT []

CMD ["/bin/bash", "-c", "ollama serve & sleep 5 && ollama run llama3.2:3b && tail -f /dev/null"]
