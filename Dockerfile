
# FROM python:3.9-slim

# WORKDIR /app

# COPY . /app

# RUN pip install -r requirements.txt

# EXPOSE 5000

# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0

# CMD ["flask", "run"]

FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

RUN pip install gunicorn

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
