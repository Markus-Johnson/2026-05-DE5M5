FROM python:3.12-slim
WORKDIR /app
COPY hello.py .
COPY . .
RUN pip install pandas
ENTRYPOINT ["python", "hello.py"]