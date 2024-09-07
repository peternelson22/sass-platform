import stripe
from decouple import config

# from . import date_utils

DJANGO_DEBUG=config("DJANGO_DEBUG", default=False, cast=bool)
STRIPE_SECRET_KEY=config("STRIPE_SECRET_KEY", default="", cast=str)
STRIPE_TEST_OVERRIDE = config("STRIPE_TEST_OVERRIDE", default=False, cast=bool)

if "sk_test" in STRIPE_SECRET_KEY and not DJANGO_DEBUG and not STRIPE_TEST_OVERRIDE:
    raise ValueError("Invalid stripe key for prod")

stripe.api_key = STRIPE_SECRET_KEY

def create_customer(name="", email="", metadata={}, raw=False):
    response = stripe.Customer.create(
        name=name,
        email=email,
        metadata=metadata,
    )
    if raw:
        return response
    stripe_id = response.id 
    return stripe_id