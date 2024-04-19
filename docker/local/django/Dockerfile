ARG PYTHON_VERSION=3.11-bullseye

FROM python:${PYTHON_VERSION} as python

FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=local

# Ensure APT uses IPv4 for better compatibility
RUN echo 'Acquire::ForceIPv4 "true";' | tee /etc/apt/apt.conf.d/99force-ipv4

# Retry mechanism for APT update
RUN set -e; \
    retries=5; \
    until apt-get update || [ "$retries" -eq 0 ]; do \
        echo "APT update failed. Retrying..."; \
        retries=$((retries - 1)); \
        sleep 1; \
    done; \
    if [ "$retries" -eq 0 ]; then \
        echo "APT update failed after multiple retries, exiting."; \
        exit 1; \
    fi

RUN apt-get install --no-install-recommends -y \
    apt-transport-https \
    ca-certificates \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove && rm -rf /var/lib/apt/lists/*

COPY ./requirements .

RUN pip wheel --wheel-dir /usr/src/app/wheels -r ${BUILD_ENVIRONMENT}.txt


FROM python as python-run-stage
ARG BUILD_ENVIRONMENT=local

ARG APP_HOME=/app

ENV PYHTONDONTWRITEBYTECODE 1
ENV PYHTONUNBUFFERED 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# Ensure APT uses IPv4 for better compatibility
RUN echo 'Acquire::ForceIPv4 "true";' | tee /etc/apt/apt.conf.d/99force-ipv4

# Retry mechanism for APT update
RUN set -e; \
    retries=5; \
    until apt-get update || [ "$retries" -eq 0 ]; do \
        echo "APT update failed. Retrying..."; \
        retries=$((retries - 1)); \
        sleep 1; \
    done; \
    if [ "$retries" -eq 0 ]; then \
        echo "APT update failed after multiple retries, exiting."; \
        exit 1; \
    fi

RUN apt-get install -y --no-install-recommends \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove && rm -rf /var/lib/apt/lists/*

COPY --from=python-build-stage /usr/src/app/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./docker/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower


COPY . ${APP_HOME}

ENTRYPOINT ["/entrypoint"]
