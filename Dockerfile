FROM python:3-slim
ENV PIP_NO_CACHE_DIR=off
WORKDIR /opt/mock-oauth-server/
COPY src/ ./
RUN pip install pipenv
RUN pipenv lock && pipenv --clear && pipenv --rm
RUN pipenv install --system
RUN pip uninstall -y pipenv
EXPOSE 4444
CMD gunicorn --config /opt/mock-oauth-server/gunicorn.conf.py wsgi:app
