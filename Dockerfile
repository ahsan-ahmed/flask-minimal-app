FROM python:latest

ADD ./requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -q -r /tmp/requirements.txt
ENV PORT 12
EXPOSE 12
WORKDIR /usr/src
ADD . /usr/src


CMD ["python","app.py"]