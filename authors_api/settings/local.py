from .base import * # noqa
from .base import env



SECRET_KEY = env("DJANGO_SECRET_KEY", default = "Qn_jPjlguugAmX-eifchMO2-cfemzToJhk97j13UG7KxepDUqmc",)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

