FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    clang \
    python3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir atheris

ADD . /src
WORKDIR /src
RUN python3 -m pip install .

CMD ["/src/mayhem/fuzz_python.py"]
