import requests
import base64
import pandas as pd

client_id = 'cf9b7270-18a3-450b-9175-c31345bd32fc'
client_secret = 'b701185c1152e6bf7479bdabeb'
redirect_url = 'https://apps.net-results.com/app/Oauth/manualAuth'
scope = 'Contact'
b64_id_secret = base64.b64encode(
    bytes(client_id + ':' + client_secret, 'utf-8')).decode('utf-8')

controller = 'Contact'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YWZvbGFrZS5iYWl5ZXd1QGluZm9kYXRpbmMuY29tOm9oQjRvaXk='
}

offset = 1
max_row_limit = 5500 # change this to the number of rows you want to scrape
total_scrapped = 0

while True:
    try:
        payload = {'id': 'example-api-random-unique-id',
                   'method': 'getMultiple',
                   'jsonrpc': '2.0',
                   'params': {'offset': offset,
                              'limit': 1000,
                              'order_by': 'contact_id',
                              'order_dir': 'ASC',
                              'options': ''}}

        response = requests.post(f'https://apps.net-results.com/api/v2/rpc/server.php?Controller={controller}',
                                 headers=headers, json=payload)

        df = pd.DataFrame(response.json()['result']['results'])

        if len(df)+total_scrapped > max_row_limit:
            df = df.head(max_row_limit-total_scrapped)
            df.to_csv('net_results_contact2.csv',
                      mode='a', header=False, index=False)
            print(f'Total scraped: {max_row_limit}')
            break

        df.to_csv('net_results_contact2.csv',
                  mode='a', header=False, index=False)

        print(f'Total scraped: {len(df) * offset}')
        offset += 1
        total_scrapped += len(df)

    except:
        break
