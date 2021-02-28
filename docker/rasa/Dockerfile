# FROM rasa/rasa:2.2.0
FROM rasa/rasa:2.3.0-spacy-en

# Use subdirectory as working directory
WORKDIR /app

USER root

RUN apt update -y && apt install -y openssh-server

# Workaround
# TODO: Need to fix copy from docker/ras
# ADD docker/rasa/entrypoint_1.sh ./
# RUN chmod +x entrypoint_1.sh

ADD entrypoint_rasa.sh ./
RUN chmod +x entrypoint_rasa.sh

COPY endpoints.yml ./
COPY credentials.yml ./

# install custom channels
COPY setup.py /app
RUN /opt/venv/bin/python -m pip install --upgrade pip
RUN python -m pip install .

# RUN pip install -U spacy==2.2.4 \
#     && python -m spacy download en_core_web_md \
#     && python -m spacy link en_core_web_md en
# RUN python -m spacy download en_core_web_md
# RUN python -m spacy link en_core_web_md en
# RUN pip install spacy==2.2.4
# https://github.com/explosion/spacy-models/releases/download/en_core_web_md-2.0.0/en_core_web_md-2.0.0.tar.gz

# Don't use root user to run code
# USER 1001

# TODO: Need to fix copy from docker/rasa with ./entrypoint.sh
ENTRYPOINT ["./entrypoint_rasa.sh"]