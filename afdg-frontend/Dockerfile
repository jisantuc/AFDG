FROM node:8-slim

RUN npm install -g elm

RUN mkdir /app
WORKDIR /app
ADD . /app

RUN elm-package install
RUN elm-make src/Main.elm --yes --warn

ENTRYPOINT elm-reactor

CMD ["-p", "9091"]
