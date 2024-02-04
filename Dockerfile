FROM python:3.11-bullseye

COPY docker/entrypoint.sh /entrypoint.sh
WORKDIR /action

COPY . .

ENTRYPOINT ["/entrypoint.sh"]
