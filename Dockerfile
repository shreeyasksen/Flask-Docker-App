FROM python:3.9-slim

WORKDIR /app

ENV PORT=4000

COPY "requirements.txt" .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .

CMD ["python", "app.py"]
