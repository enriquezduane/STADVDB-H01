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
3. Change directory to where the file is located in your computer then run the Powershell script 'windows-setup.ps1'.
   ```
    .\windows-setup.ps1
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


