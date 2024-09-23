Remove-Item -Recurse -Force .venv

docker-compose down -v

docker-compose up -d --build

Get-Content ./data/supplies.json | docker exec -i stadvdb-h01-mongodb-1 mongoimport -c supplies -d main --drop

python -m venv .venv

& .venv\Scripts\Activate.ps1

pip install mysql-connector-python
pip install pandas
pip install sqlalchemy
pip install pymongo
pip install pymysql

Start-Sleep -Seconds 10

python export/export_sql.py
python export/export_csv.py
python export/export_json.py
python export/connect_to_fact.py

Write-Host "ETL Process Done"
