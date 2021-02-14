FROM python:3.8-alpine

WORKDIR /app/

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements*.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
