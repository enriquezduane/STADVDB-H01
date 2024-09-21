rm -rf .venv 

docker-compose down -v

docker-compose up -d --build

docker exec -i stadvdb-h01-mongodb-1 sh -c 'mongoimport -c supplies -d main --drop' < ./data/supplies.json

python3 -m venv .venv

source .venv/bin/activate

pip3 install mysql-connector-python
pip3 install pandas
pip3 install sqlalchemy
pip3 install pymongo
pip3 install pymysql

sleep 10

python3 export/export_sql.py
python3 export/export_csv.py
python3 export/export_json.py
python3 export/connect_to_fact.py

echo "ETL Process Done"
