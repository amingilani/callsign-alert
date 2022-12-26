import encrypted_secrets

DEBUG = False
SECRET_KEY = encrypted_secrets.get_secret('secret_key')


ALLOWED_HOSTS = [
    "callsign-alert.fly.dev",  # fly.io development domain
]
