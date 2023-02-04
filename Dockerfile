# Copyright (C) 2023 Yazdan Ranjbar<yazdanra@icloud.com>


# Build stage
FROM python:3.9-slim AS builder

WORKDIR /

RUN apt-get update && apt-get install -y gcc git libpq-dev

# install production requirements
COPY requirements.txt .
RUN pip install --use-deprecated=legacy-resolver -r requirements.txt ||  \
    pip install --disable-pip-version-check --no-cache-dir -r requirements.txt

# Final image
FROM python:3.9-slim

# set common work directory
WORKDIR /usr/app

# Install required dependencies
RUN apt-get update
RUN apt-get install -y --fix-missing --no-install-recommends nginx libpq-dev procps cron vim netcat gettext graphviz

# Copy pip installed packages
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
RUN pip install gunicorn --upgrade --disable-pip-version-check --no-cache-dir
RUN pip install ipython --upgrade --disable-pip-version-check --no-cache-dir


# Mount sourse code
COPY . .

# Configure Timezone
ENV TZ=CST

RUN echo "Configuring timezone:" $TZ \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezonero


# Set Environment configs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Make entrypoint executable and run the entrypoint to start jobs, gunicorns, liveness
#RUN chmod +x /usr/app/docker-entrypoint.sh
ENTRYPOINT ["bash", "docker-entrypoint.sh"]

# Expose the port that Django use it
EXPOSE 8000
