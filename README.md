# Pick-My-Parts
**2025SP.CSC.289.0001 Capstone Project Group 8**
___
### Requisites (required installation)
- Python
[https://www.python.org/downloads/](https://www.python.org/downloads/)

- mariadb
[https://mariadb.org/](https://mariadb.org/)

- db browser software like dbeaver (optional)
[https://dbeaver.io/download/](https://dbeaver.io/download/)

___
### Setup and run project
- **Creating database and database user for the project**
1. Open a command prompt and run following command. Replace \<root\> with the user you created when installing mariadb (if changed). Enter the password you assigned for the user when prompted.
```cmd
mysql -u root -p
```

2. Create a database to use in our app
```cmd
create database pick_my_parts;
```

3. Create a user in the database server. Replace \<password\> as necessary
```cmd
CREATE USER 'pick_my_parts_db_user'@'localhost' IDENTIFIED BY 'password';
```

4. Grant all privileges on the database to the user
```cmd
GRANT ALL PRIVILEGES ON pick_my_parts.* TO 'pick_my_parts_db_user'@'localhost';
```

5. Apply changes
```cmd
FLUSH PRIVILEGES;
```

- **Setup a virtual env (venv)**
```bash
python -m venv venv
```

- **Activate the venv**
```ps1
.\venv\Scripts\Activate.ps1
```

If using powershell in vscode, you might need to update execution policy
```ps1
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

- **Install dependencies from requirements.txt**
```bash
pip install -r requirements.txt
```

- **Apply DB Migrations**  
Apply Migrations from /apps/core/migrations folder. 
The migrations folder hold all changes that will be applied to Database based on django models
```bash
python manage.py migrate
```

- **Populate the Database**  
After migrations, populate the database using structured JSON files located in the `/data/` folder:
```bash
python populate_db.py
```

- **Reset the Database**  
If you need to wipe all parts data clean:
```bash
python reset_db.py
```

- **Run Django server**
```bash
python manage.py runserver
```

___
- **Running Django Unit Tests (Individual Test File)**
```commandline
python manage.py test apps.core.tests.test_computer_case --settings=config.test_settings
```
- **Running Django Unit Tests (All Tests)**
```commandline
python manage.py test core --settings=config.test_settings
```
___
**NOTE 1: Create a .env file to hold all environment variables used in config/settings.py. Do not commit and push .env file.**
```
DB_HOST=*******
DB_PORT=*******
DB_NAME=*******
DB_USER=*******
DB_PASSWORD=*******
```

**NOTE 2: After making changes to Django Models (/apps/models/.....), we need to generate migration file and migrate it. Need to commit migration files as well.**
\
To create Migration
```bash
python manage.py makemigrations
```
To apply migrations
```bash
python manage.py migrate
```
