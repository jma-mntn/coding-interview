FROM python:3.11-slim-buster

EXPOSE 8080
ENV POETRY_VERSION=1.3.1

# Install poetry
RUN pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false

RUN poetry install
COPY . .

CMD ["python", "/app_under_test/app.py"]:

