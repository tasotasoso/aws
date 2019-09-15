FROM golang:1.12
ENV PKG_PATH /go/src/
ENV GO111MODULE on
WORKDIR $PKG_PATH
RUN go mod download
COPY ./ $PKG_PATH
RUN go install .

FROM golang:1.12
COPY --from=0 /go/bin /go/bin/
ENV AWS_ACCESS_KEY_ID=アクセスキーID
ENV AWS_SECRET_ACCESS_KEY=シークレットアクセスキー
ENV AWS_REGION=リージョン
ENTRYPOINT ["/go/bin/main"]