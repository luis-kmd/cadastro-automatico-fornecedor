import requests
# API PARA CONSULTAS E LANÇAMENTOS NO BANCO DE DADOS
def api(metodo, query):
    url = 'ADRESS_API'
    auth = ('USER', 'PASSWORD')
    headers = {'Content-Type': 'application/json'}
    payload = {'query': query}

    if metodo == 'GET':
        url = f"{url}/consultateste"
        response = requests.get(url, headers=headers, auth=auth, json=payload)
    elif metodo == 'POST':
        url = f"{url}/executarteste"
        response = requests.post(url, headers=headers, auth=auth, json=payload)
    else:
        return None
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

