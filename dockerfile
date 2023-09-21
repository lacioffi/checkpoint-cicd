FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install flask
RUN pip install pandas

CMD ["python3", "app.py"]
