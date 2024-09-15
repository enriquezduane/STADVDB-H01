docker-compose up -d

python3 -m venv .venv

source .venv/bin/activate

pip3 install sqlalchemy pandas mysql-connector-python

python3 init.py

# etl
# python3 main.py

