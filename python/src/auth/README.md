python3 -m venv venv
<br>
source ./venv/bin/activate

env | grep VIRTUAL

Run the script for DB
<br>
'mysql -uroot'

Troubleshooting (for homebrew Mac Users)
<br>
If you're not able to execute 'mysql -uroot', then run 'brew services start mysql'. By default, MySQL is installed without a root password through homebrew. To secure this, run: 'mysql_secure_installation'