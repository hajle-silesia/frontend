FROM nginx:1.27.4
RUN apt update && apt install -y \
        curl
COPY ./src /usr/share/nginx/html
