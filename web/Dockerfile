FROM python:3.9-alpine

ARG APP_ENV
WORKDIR /app

ENV APP_ENV=${APP_ENV}}
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH=$POETRY_HOME/bin:$VENV_PATH/bin:$PATH

RUN apk update && apk add postgresql-dev gcc g++ python3-dev musl-dev libffi-dev curl

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi $(test $APP_ENV == prod && echo "--no-dev")

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
