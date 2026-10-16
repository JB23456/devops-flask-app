FROM python:latest

WORKDIR /web-app

COPY hello.py /web-app
COPY requirements.txt /web-app

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app", "hello", "run", "--host=0.0.0.0"]