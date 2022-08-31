import requests
import json


def get_message(wallet,session,proxy):
    datas={"id":"challengeLoginMessageQuery","query":"query challengeLoginMessageQuery(\n  $address: AddressScalar!\n) {\n  auth {\n    loginMessage(address: $address)\n  }\n}\n","variables":{"address":wallet}}
    headers={'Accept':'*/*',
    'X-BUILD-ID':'wcYZqaKPOhuEVP8aUNBpW',
    'x-signed-query':'05649d324b3f3db988d5065ea33599bca390adf00e3f46952dd59ff5cc61e1e0',
    'X-VIEWER-ADDRESS':wallet,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36',
    'X-API-KEY':'2f6f419a083c46de9d83ce3dbe7db601',
    'Content-Type':'application/json',
    'Sec-GPC':'1',
    'Origin':'https://opensea.io',
    'Sec-Fetch-Site':'same-site',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Dest':'empty',
    'Referer':'https://opensea.io/',
    'Accept-Language':'en-GB,en-US;q=0.9,en;q=0.8',
    }
    response=session.post('https://api.opensea.io/graphql/',json=datas,headers=headers,proxies=proxy)
    jesko=json.loads(response.text)
    return jesko['data']['auth']['loginMessage']
