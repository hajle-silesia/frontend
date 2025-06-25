FROM nginx:1.29.0
RUN apt update && apt install -y \
        curl
COPY ./src /usr/share/nginx/html
