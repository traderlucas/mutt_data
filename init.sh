#!/bin/bash
source .env 
docker-compose up -d && \
#source venv/bin/activate &&\
pip install -r requirements.txt && \
python app/main.py