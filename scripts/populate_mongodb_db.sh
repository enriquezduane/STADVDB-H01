docker exec -i stadvdb-h01-mongodb-1 sh -c 'mongoimport -c supplies -d main --drop' < ./data/supplies.json
