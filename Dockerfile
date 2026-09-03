FROM nginx:1.31.5
RUN apt update && apt install -y \
        curl
COPY ./src /usr/share/nginx/html
