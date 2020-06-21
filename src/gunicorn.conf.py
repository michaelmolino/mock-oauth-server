import os

bind = '0.0.0.0:4444'
forwarded_allow_ips = '*'
secure_scheme_headers = {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
workers = 1
keep_alive = 5
certfile = os.environ.get("CERT_FILE") or '/ssl/public.crt'
keyfile = os.environ.get("KEY_FILE") or '/ssl/private.key'
