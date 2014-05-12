<b>type this command in terminal for install this application:</b>
git clone https://github.com/maximzxc/maximzxc_notes

cd maximzxc_notes

apt-get install virtualenv

apt-get install_install pip

virtualenv --distribute env

virtualenv .env

source .env/bin/activate

sudo apt-get build-dep python-imaging

sudo ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/

sudo ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/

sudo ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/

pip install -r requirements.txt

python manage.py migrate

python manage.py syncdb --noinput

python manage.py migrate --fake

python manage.py loaddata fixtures notes_views_testdata.json

python manage.py loaddata fixtures books_views_testdata.json

python manage.py runserver

<b>open browser and go to see notes that already exists:</b>

http://localhost:8000/notes/list/

<b>for addind new notes or deleting exists open browser and go to:</b>

http://localhost:8000/admin/

<b>for testing application type:</b>

python manage.py test Notes
