FROM ubuntu:latest
LABEL authors="adh"

ENTRYPOINT ["top", "-b"]