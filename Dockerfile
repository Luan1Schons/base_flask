# Usa uma imagem base leve com Python 3
FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

#CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "/app/run.py:app"]
CMD ["gunicorn", "--log-level", "debug", "-w", "2", "-b", "0.0.0.0:5000", "run:app"]
