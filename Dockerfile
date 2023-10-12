FROM nginx:1.25.2
RUN apt update && apt install -y \
    curl \
    python3 \
    python3-pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src /usr/share/nginx/html
