from google.oauth2 import id_token
from google.auth.credentials import Credentials
from google.auth.transport.requests import Request

req: Request = Request()
creds: Credentials = id_token.fetch_id_token_credentials(audience="", request=req)
