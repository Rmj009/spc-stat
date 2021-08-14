FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
ENV PG_URL='postgresql://postgres:edge9527@host.docker.internal:5432/dev_tenant'
ENV PORT=5000
ENV HOST=0.0.0.0
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
