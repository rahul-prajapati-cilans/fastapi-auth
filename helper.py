import secrets

# Generates a URL-safe base64-encoded string
secret_key = secrets.token_urlsafe(32)
print(secret_key)
