import random
from datetime import datetime, timedelta

methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD']
paths = [
    '/index.html', '/login', '/logout', '/dashboard', '/api/data', '/api/users',
    '/products', '/cart', '/checkout', '/styles.css', '/script.js', '/favicon.ico'
]
status_codes = [200, 201, 204, 301, 302, 400, 401, 403, 404, 500, 502, 503]
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)',
    'Mozilla/5.0 (Linux; Android 11)',
    'curl/7.68.0',
    'Wget/1.20.3 (linux-gnu)',
    'Googlebot/2.1 (+http://www.google.com/bot.html)'
]
referrers = ['-', 'https://example.com/', 'https://example.com/login', 'https://google.com', 'https://facebook.com']
ip_blocks = ['192.168.1.', '10.0.0.', '172.16.0.', '203.0.113.', '198.51.100.', '192.0.2.']

base_time = datetime(2025, 8, 21, 10, 0, 0)

def generate_log_line():
    ip = random.choice(ip_blocks) + str(random.randint(1, 254))
    dt = base_time + timedelta(seconds=random.randint(0, 3600))
    timestamp = dt.strftime('%d/%b/%Y:%H:%M:%S +0000')
    method = random.choice(methods)
    path = random.choice(paths)
    protocol = 'HTTP/1.1'
    status = random.choice(status_codes)
    size = random.randint(100, 5000)
    referrer = random.choice(referrers)
    user_agent = random.choice(user_agents)
    
    return f'{ip} - - [{timestamp}] "{method} {path} {protocol}" {status} {size} "{referrer}" "{user_agent}"'

with open('access.log', 'w') as f:
    for _ in range(1000):
        f.write(generate_log_line() + '\n')

print("✅ access.log with 1000 lines has been created.")

