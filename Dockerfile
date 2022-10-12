FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install --quiet --no-cache-dir --upgrade pip && \
    pip3 install --quiet --no-cache-dir -r requirements.txt
COPY . /code/