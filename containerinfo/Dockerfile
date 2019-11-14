FROM alpine:latest
LABEL maintainer="https://github.com/eaksel"
RUN apk add --no-cache python3
COPY ./app/ /app
WORKDIR /app
RUN pip3 --no-cache-dir install -r requirements.txt
EXPOSE 5000/tcp
ENTRYPOINT ["python3"]
CMD ["app.py"]