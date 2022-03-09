FROM python:3.9-slim
RUN apt-get update && apt-get install -y \
    python-tk
ENV DISPLAY host.docker.internal:0
WORKDIR app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./app/src .
ENTRYPOINT ["python", "main.py"]