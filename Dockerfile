FROM nginx:1.30.0
RUN apt update && apt install -y \
        curl
COPY ./src /usr/share/nginx/html
