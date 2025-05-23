FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=main.py

CMD [ "flask", "run", "--host=0.0.0.0", "--port=4400" ]