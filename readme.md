# Student Management System using Tkinter, Mysql

# # How to operate?

1. create python environment

```bash
python -m venv env
```
<!-- env is name of environment. Can be changed according to the preferences -->4

2. active python environment

```bash
source ./env/Scripts/active
```
>for bash

```bash
Scripts\active
```
>for powershell hind: find active and run 

3. Install all the requirements

```bash
pip install -r requirements.txt
```

4. Run the Schema in the MySQL server

5. Update database credentials in config.ini
> if config.ini is not present in the dir then : create config.ini and update credentials according the snippet
```bash
[database_details]
user=username
password=password
host=host (eg. localhost)
database=database_name
```

6. run test/test.py file to veirfy the connection to the database server

7. run test/create_super_admin.py to create at least one superadmin

8. Then finally run app.py