#develop stage
FROM nieronghua/apline-python-3.8 as develop-stage
RUN apk add build-base python3-dev postgresql-dev
WORKDIR app
RUN pip install pipenv greenlet
RUN pipenv run python -m pip install --upgrade pip
COPY . .

# production stage
FROM develop-stage as production-stage
RUN pipenv install
EXPOSE 5432
CMD pipenv run uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000}
