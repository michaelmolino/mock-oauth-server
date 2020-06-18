FROM python:3
RUN pip install git+https://github.com/pypa/pipenv.git
WORKDIR /opt/mock-oauth-server/
COPY src/ ./
RUN pipenv install --system
EXPOSE 4444
CMD gunicorn --config /opt/mock-oauth-server/gunicorn.conf.py wsgi:app
