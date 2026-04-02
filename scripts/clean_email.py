# Email cleaning logic used in n8n Code node

def clean_email(body):
    # Remove extra whitespace
    clean_body = body.strip()[:1500]
    return clean_body