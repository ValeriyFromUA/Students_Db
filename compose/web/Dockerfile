FROM python:3.14-slim
WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install --upgrade pip \
    && pip install pipenv \
    && pipenv install --deploy --system --dev

COPY . ./

CMD ["python3", "app_run.py"]
