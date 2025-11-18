FROM python:3.11-slim

WORKDIR /app
COPY exporter.py .
COPY config.yaml .

RUN pip install flask requests pyyaml

ENV PYTHONUNBUFFERED=1

CMD ["python", "exporter.py"]
