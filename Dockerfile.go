FROM golang:latest

COPY publisher.go /app/main.go

WORKDIR /app

RUN go mod init example.com/m

RUN go mod tidy

CMD ["go","run","main.go"]
