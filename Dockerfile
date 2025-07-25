FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y gcc gfortran libfftw3-dev libopenblas-dev liblapack-dev git && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python3", "MEN_Falsification_Engine.py"]