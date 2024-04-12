# gunicorn_config.py
import vendorproject.settings as settings

bind = settings.BIND
workers = settings.WORKERS
