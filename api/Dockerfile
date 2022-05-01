# production environment Uvicorn
FROM python:3.9

COPY . /src

WORKDIR src

EXPOSE 3001

# do the python things
RUN pip3 install 'poetry==1.1.6'
RUN pip3 install --no-cache-dir "uvicorn[standard]" gunicorn

ENV PYTHONPATH "${PYTHONPATH}:./app"

# do the app things
COPY ./pyproject.toml /tmp/
COPY ./poetry.lock /tmp/
RUN cd /tmp && poetry export --without-hashes -f requirements.txt > requirements.txt
RUN pip3 install -r /tmp/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3001"]