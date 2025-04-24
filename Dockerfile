FROM nginx:1.28.0
RUN apt update && apt install -y \
        curl
COPY ./src /usr/share/nginx/html
