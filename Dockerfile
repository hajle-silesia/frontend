FROM nginx:1.29.1
RUN apt update && apt install -y \
        curl
COPY ./src /usr/share/nginx/html
