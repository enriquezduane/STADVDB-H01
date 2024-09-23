# Software utilized for the project
- **Docker**: https://docs.docker.com/desktop/install/windows-install/
- **DBeaver**: https://dbeaver.io/
- **IDE**: Any will do.

# Python Dependencies
Python is the programming language used in the creation of the export scripts in the repository. 
- SQLAlchemy
- Pandas
- mysql-connector-python
- PyMongo
- PyMySQL

# Data Warehouse setup for Windows
1. Install Docker and DBeaver
2. Once they are installed, run this code in the terminal. It should set the foundation for the local database:
  ```Terminal
	  docker-compose up -d --build
  ```
3. Using DBeaver, create two new database connections (Crtl + Shift + N) and fill them with these database credentials. Both should be connected before running any script:
   ```
    Local Database:
    hostname: localhost
    port: 3306
    username: root
    password: rootpassword
    
    Cloud Database
    hostname: db.relational-data.org
    port: 3306
    username: guest
    password: relational
   ```
4. Install Python dependencies.
   ```
    pip3 install mysql-connector-python
    pip3 install pandas
    pip3 install sqlalchemy
    pip3 install pymongo
    pip3 install pymysql
   ```
5. Run all Python scripts.
   ```
   python export/export_sql.py
   python export/export_csv.py
   python export/export_json.py
   python export/connect_to_fact.py
   ```
   
# Data Warehouse setup for Unix-based systems
1. Install Docker and DBeaver
2. Using DBeaver, create two new database connections (Crtl + Shift + N) and fill them with these database credentials. Both should be connected before running any script:
   ```
    Local Database:
    hostname: localhost
    port: 3306
    username: root
    password: rootpassword
    
    Cloud Database
    hostname: db.relational-data.org
    port: 3306
    username: guest
    password: relational
   ```
3. Run the shell script 'run.sh'.
   ```
   ./run.sh
   ```


