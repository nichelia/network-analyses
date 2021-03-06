FROM python:3.7-slim AS compile-image

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ARG APP_VERSION=1.0.0
RUN /bin/bash -c "pip install 'nwa==${APP_VERSION}'"

# ----

FROM python:3.7-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR "/usr/src"
ENTRYPOINT ["nwa"]
