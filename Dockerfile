FROM python:3.11.2-slim-bullseye
RUN apt update && apt upgrade -y
ENV DISPLAY host.docker.internal:0
WORKDIR project
ENV PYTHONPATH "${PYTHONPATH}:/project"
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src ./src
ENTRYPOINT ["python", "src/main.py"]
