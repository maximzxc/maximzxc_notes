<b>type this command in terminal for install this application:</b>

git clone https://github.com/maximzxc/maximzxc_notes/tree/create-app-that-shows-list-of-text-notes

cd create-app-that-shows-list-of-text-notes

apt-get install virtualenv

apt-get install_install pip

virtualenv --distribute env

virtualenv .env

source .env/bin/activate

pip install -r requirements.txt

python manage.py syncdb --noinput

python manage.py migrate

python manage.py loaddata fixtures notes_views_testdata.json

python manage.py runserver

<b>open browser and go to see notes that already exists:</b>

http://localhost:8000/notes/list/

<b>for addind new notes or deleting exists open browser and go to:</b>

ttp://localhost:8000/admin/

<b>for testing application type:</b>

python manage.py test Notes