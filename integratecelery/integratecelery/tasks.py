from celery import shared_task
from .plaidclient import get_plaid_client



@shared_task
def get_access_token(public_token):
    client = get_plaid_client()
    response = client.Item.public_token.exchange(public_token)
    return response

    