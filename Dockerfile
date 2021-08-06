FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
ENV PG_URL='postgresql://paul:15TCjQ7VhREM2@34.80.53.176:5432/dev_tenant'
ENV PORT=5000
ENV PATH="/ServingSPC"
EXPOSE 5000
CMD ["python3","-m","flask run"]
