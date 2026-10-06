import json
import urllib.error
import urllib.request

url = 'http://127.0.0.1:8001/generate'
data = json.dumps({
    'document_type': 'Rental Agreement',
    'user_details': 'Landlord: Ravi Kumar. Tenant: Arun Kumar. Property: Chennai.'
}).encode()
req = urllib.request.Request(url, data=data, method='POST', headers={'Content-Type': 'application/json'})

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        body = resp.read().decode()
        result = {'status': resp.status, 'body': body}
except urllib.error.HTTPError as e:
    result = {'status': e.code, 'body': e.read().decode()}

with open(r'D:\LegalEase\api_check.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2)
