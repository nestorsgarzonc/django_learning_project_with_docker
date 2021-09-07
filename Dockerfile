FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
# RUN apk add zlib-dev jpeg-dev gcc musl-dev
RUN python -m pip install Pillow
RUN pip install -r requirements.txt
COPY . /code/