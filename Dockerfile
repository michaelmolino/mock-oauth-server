FROM python:3-slim
ENV PIP_NO_CACHE_DIR=off
# Need to install pipenv from master until this is released
# https://github.com/pypa/pipenv/issues/4337
RUN apt-get update && apt-get install -y git
RUN pip install --no-cache-dir git+https://github.com/pypa/pipenv.git
WORKDIR /opt/mock-oauth-server/
COPY src/ ./
RUN pipenv install --system
RUN pip uninstall -y pipenv
RUN apt-get --purge remove -y git
RUN apt-get autoremove -y
EXPOSE 4444
CMD gunicorn --config /opt/mock-oauth-server/gunicorn.conf.py wsgi:app
