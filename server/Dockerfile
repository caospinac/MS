FROM python:3.9-alpine

WORKDIR /app

RUN apk update && apk add postgresql-dev gcc g++ python3-dev musl-dev libffi-dev curl
RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile Pipfile.lock /app/

RUN pipenv install --system --deploy

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
