FROM python:3.9-slim

WORKDIR /server

COPY rest/ .

RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt

CMD ["python", "./rest_file_api_server.py"]
