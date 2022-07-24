FROM python:3-alpine

RUN apk add alpine-sdk

RUN mkdir -p /opt/antispam/
WORKDIR /opt/antiSpam/

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pip install pipenv \
    && pipenv install --system --deploy

COPY . .

CMD ["python3", "antiSpam.py"]
