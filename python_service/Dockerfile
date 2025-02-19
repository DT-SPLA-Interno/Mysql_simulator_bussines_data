# Dockerfile para Python Service (python_service/Dockerfile)
FROM python:3.9

WORKDIR /app

COPY main.py .
RUN pip install mysql-connector-python

CMD ["python", "main.py"]
