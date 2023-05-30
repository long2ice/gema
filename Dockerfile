FROM node as frontend-builder
ARG GIT_TOKEN
RUN git clone https://$GIT_TOKEN@github.com/long2ice/gema-web.git /gema-web
WORKDIR /gema-web
ENV REACT_APP_API_URL /api
RUN npm install && npm run build

FROM python:3.11 as builder
RUN mkdir -p /gema
WORKDIR /gema
COPY pyproject.toml poetry.lock /gema/
ENV POETRY_VIRTUALENVS_CREATE false
RUN pip3 install poetry && poetry install

FROM python:3.11-slim
WORKDIR /gema
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=frontend-builder /gema-web/build /gema/static
COPY . /gema
CMD ["uvicorn" ,"gema.app:app", "--host", "0.0.0.0"]
