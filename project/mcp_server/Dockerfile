FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache- -r requirements.txt

RUN rm -rvf requirements.txt

COPY *.py key.pub .

COPY flag.txt /

RUN chmod +x mcp_server.py

CMD ["python", "mcp_server.py"]
