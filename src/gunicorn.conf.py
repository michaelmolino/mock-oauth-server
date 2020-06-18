bind = '0.0.0.0:4444'
forwarded_allow_ips = '*'
secure_scheme_headers = {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
workers = 1
keep_alive = 5
certfile = '/config/certs/nginx-selfsigned.crt'
keyfile = '/config/certs/nginx-selfsigned.key'
