docker-compose up -d && \
pip install -r requirements.txt && \
source .env && \
python app/main.py