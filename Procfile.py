import gunicorn

from run import app

web: gunicorn run:app