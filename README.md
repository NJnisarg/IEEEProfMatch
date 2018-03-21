# Professor Matching Project
The Backend Repository of IEEE Envision(NITK) project Professor Matching

## Installation Instructions
1. Clone the repository into the desired location

2. Create a virtual environment to run the application using : 

```
virtualenv -p python3 ProfMatchEnv
source ProfMatchEnv/bin/activate
```

3. Change directory into the location containing the requirement.txt and manage.py

4. Run the following commands(while the virtualenv is running) to install the project dependencies :

```
pip install -r requirements.txt
```

5. Make the database migrations :

```
python manage.py migrate
```

6. Test the application on localhost by running the server
```
python manage.py runserver
```

This starts up the server on ``` localhost:8000/ ```
   
## Database configurations

By default this application when cloned will use the embedded sqlite3 database. But other databases can be configured as well.

The followwing segment guides how to use Mysql database instead of sqlite3. Mysql is the intended production database server.

### Configuring MySQL with the project(Linux)

1. Install mysql and setup
```
sudo apt-get update
sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
sudo mysql_secure_installation
```

2. Install the django mysql depedencies(First activate the virtual environment)
```
pip install mysqlclient
```
     
3. Change the configuration in the {installation_dir}/ProfMatch/settings.py

``` 
Go to the DATABASES section of the file and commet out the sqlite3 settings and uncomment the mysql settings
Give appropriate values to the USER and PASSWORD fields, supply the ones you used to setup the mysql installation
Leave the NAME field as it is. This field is the name of the Database to use.
```

4. Create the database of the same name as in the NAME field above. Assuming you left the field as it is with the name 'ProfMatch' type the following in the terminal :
```
sudo service mysql start
mysql -h 127.0.0.1 -u <username> -p
```

\<username\> is the username you provided during the mysql setup. If left as default it will be 'root'. The above command will prompt for a password as well.
Provide the password used during the mysql setup
    
* To create the database (named ProfMatch):
``` 
CREATE DATABASE ProfMatch;
SHOW DATABASES;
```
    
Using SHOW DATABASES Command your created database will appear in the list of databases

5. To use this database, again migrate 
``` 
python manage.py migrate 
```

6. Run the server 
``` 
python manage.py runserver
```

## Technical details

* For more information like Database schemas, the modules present, the services implemented and the API endpoints, please refer the wiki section.

## Usage Instructions

* This repository is the backend system of Professor Matching project under IEEE Envision programme.
* To get the system up and running on your local machine, carry out the installation instructions listed above and configure the database.
* You can use the default inbuilt SQLite database for testing. For using MySQL database, carry out the above database configurations
* At the end of the process, the backend server will be running on ``` localhost:8000/ ```
* To test the services and apis, check out the wiki section for technical implementation details about the database schemas and API endpoints.
* We recommend using API testing tools like "postman" for testing the endpoints.

#### More about Postman

* For more information about how to install and use postman follow this link : https://www.getpostman.com/docs/v6/postman/launching_postman/installation_and_updates
