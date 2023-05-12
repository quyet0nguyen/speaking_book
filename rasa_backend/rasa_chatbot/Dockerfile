FROM python:3.8-slim as builder
ENV http_proxy=http://10.60.133.139:3128; https_proxy=http://10.60.133.139:3128

COPY swg_ca.crt /usr/local/share/ca-certificates/swg_ca.crt
RUN chmod 644 /usr/local/share/ca-certificates/swg_ca.crt && update-ca-certificates
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt


WORKDIR /app
COPY . /app

CMD [ "python", "run.py"]


# FROM python:3.8-slim as builder

# RUN apt update && \
#     apt install --no-install-recommends -y build-essential gcc curl
# RUN python -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"
# COPY requirements.txt /requirements.txt

# RUN pip install -r /requirements.txt --default-timeout=100000

# WORKDIR /app
# COPY . /app

# CMD [ "python", "run.py"]