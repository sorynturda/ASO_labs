FROM python:3.13-slim

WORKDIR /app/multi_tool_agent

COPY requirements.txt .

RUN pip install --no-cache- -r requirements.txt

RUN rm -rvf requirements.txt

COPY *.py .env .

WORKDIR /app

CMD ["adk", "web", "--host", "0.0.0.0", "--port", "8080"]
#CMD ["tail", "-f", "/dev/null"]
