FROM python:3.7.6-buster


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000

COPY src/ src/
COPY index.py index.py
COPY .env .env

CMD ["python3", "index.py"]
