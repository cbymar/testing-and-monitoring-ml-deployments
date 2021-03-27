FROM python:3.7-alpine
WORKDIR /code

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# gcc speeds up MarkupSafe and SQLAlchemy
RUN apk add --no-cache gcc musl-dev linux-headers

# copy reqs to container separately apparently is better use of layer caching
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /code

CMD ["flask","run"]
