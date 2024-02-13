FROM python:3.12-alpine
WORKDIR .
COPY . .
RUN python3 -m pip install --upgrade pip -r requirements.txt
EXPOSE 5000
CMD gunicorn -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000 main:app
