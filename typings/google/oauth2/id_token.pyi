from google.auth.credentials import Credentials
from google.auth.transport.requests import Request

def fetch_id_token_credentials(
    audience: str, request: Request | None = None
) -> Credentials: ...
