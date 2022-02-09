FROM python:3.9-slim
RUN apt-get update && apt-get install python-tk -y
ENV DISPLAY host.docker.internal:0
WORKDIR app
RUN mkdir src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./app/src ./src
CMD ["python", "src/app.py"]