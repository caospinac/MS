FROM python:3.8-alpine

RUN mkdir /app/
WORKDIR /app/

COPY ./requirements*.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

COPY . /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
