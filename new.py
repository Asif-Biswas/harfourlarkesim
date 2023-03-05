import requests
import base64
import pandas as pd

client_id = 'cf9b7270-18a3-450b-9175-c31345bd32fc'
client_secret = 'b701185c1152e6bf7479bdabeb'
redirect_url = 'https://apps.net-results.com/app/Oauth/manualAuth'
scope = 'Contact'
b64_id_secret = base64.b64encode(bytes(client_id + ':' + client_secret, 'utf-8')).decode('utf-8')

controller = 'Contact'
limit = 1000
offset = 1

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YWZvbGFrZS5iYWl5ZXd1QGluZm9kYXRpbmMuY29tOm9oQjRvaXk='
}

while True:
    try:
        payload = {'id': 'example-api-random-unique-id',
        'method': 'getMultiple',
        'jsonrpc': '2.0',
        'params': {'offset': offset,
        'limit': limit,
        'order_by': 'contact_id',
        'order_dir': 'ASC',
        'options': ''}}

        response = requests.post(f'https://apps.net-results.com/api/v2/rpc/server.php?Controller={controller}',
                                headers=headers, json=payload)

        df = pd.DataFrame(response.json()['result']['results'])
        df.to_csv('net_results_contact2.csv', mode='a', header=False, index=False)
        
        print(f'Total scraped: {len(df) * offset}')
        offset += 1
    
    except:
        break
