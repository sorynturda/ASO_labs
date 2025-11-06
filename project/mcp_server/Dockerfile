FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-chache-dir -r requirements.txt

COPY *.py .

CMD ["python", "mcp_server.py"]
