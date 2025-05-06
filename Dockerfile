FROM python:3.9-slim
WORKDIR /app
COPY numbers.py /app/numbers.py
ENTRYPOINT [ "python", "numbers.py" ]
