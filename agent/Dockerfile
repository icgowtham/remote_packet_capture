FROM python:3.9-slim

WORKDIR /agent

COPY . ./

RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt

CMD ["python", "./agent_rest_server.py"]
