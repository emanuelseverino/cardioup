FROM nginx:1.25.4-alpine
LABEL  authors="Emanuel Severino <emanuelsmseverino@gmail.com>"
ENV PYTHONBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
COPY /docker/nginx/nginx.conf /etc/nginx/nginx.conf
COPY . /var/www
RUN rm -rf /etc/nginx/conf.d/default.conf
EXPOSE 80 443
ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]