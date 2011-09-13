Set up
======

    git clone git://github.com/stasm/replaydog.git
    cd replaydog
    virtualenv --no-site-packages --python=python2.7 env
    source env/bin/activate
    pip install -r requirements.txt
    ./manage.py validate
    ./manage.py syncdb
    ./manage.py runserver 0.0.0.0:8001
