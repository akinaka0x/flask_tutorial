FROM python:3.12-bullseye

ARG APP_PATH="/app"

WORKDIR $APP_PATH
RUN pip install Flask

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
