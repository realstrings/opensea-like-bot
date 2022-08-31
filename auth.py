import requests
import json
def auth(message,public,signed,session,proxy):
    datas={"id":"authLoginMutation","query":"mutation authLoginMutation(\n  $address: AddressScalar!\n  $identity: IdentityInputType!\n  $message: String!\n  $signature: String!\n  $chain: ChainScalar\n) {\n  auth {\n    login(address: $address, identity: $identity, message: $message, signature: $signature, chain: $chain) {\n      token\n    }\n  }\n}\n","variables":{"address":public,"identity":{"address":public},"message":message,"signature":signed,"chain":"ETHEREUM"}}
    headers={
    'X-BUILD-ID':'wcYZqaKPOhuEVP8aUNBpW',
    'x-datadog-origin':'rum',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36',
    'x-datadog-sampling-priority':'1',
    'Content-Type':'application/json',
    'Accept':'*/*',
    'x-signed-query':'c59037126bd280c25d87029e968b165b74c6722a1ee4c8457d35a88dba54472b',
    'X-VIEWER-ADDRESS':public,
    'x-datadog-sampled':'1',
    'X-API-KEY':'2f6f419a083c46de9d83ce3dbe7db601',
    'Sec-GPC':'1',
    'Origin':'https://opensea.io',
    'Sec-Fetch-Site':'same-site',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Dest':'empty',
    'Referer':'https://opensea.io/',
    'Accept-Language':'en-GB,en-US;q=0.9,en;q=0.8'
    }
    response=session.post('https://api.opensea.io/graphql/',json=datas,headers=headers,proxies=proxy)
    jesko=json.loads(response.text)
    return jesko['data']['auth']['login']['token']