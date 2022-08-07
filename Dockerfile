FROM python:3.9 as builder
RUN mkdir -p /gema
WORKDIR /gema
COPY pyproject.toml poetry.lock /gema/
ENV POETRY_VIRTUALENVS_CREATE false
RUN pip3 install poetry && poetry install

FROM python:3.9-slim
WORKDIR /gema
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY . /gema
