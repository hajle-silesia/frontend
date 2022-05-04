FROM python:3.9
RUN apt update && apt install -y \
    curl
ENV DISPLAY host.docker.internal:0
WORKDIR app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./app/src .
ENTRYPOINT ["python", "main.py"]