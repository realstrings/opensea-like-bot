
import base64


def like(asset_id,auth,public,session,proxy):
    thiss="AssetType:"+asset_id
    data={"id":"useAssetFavoriteMutation","query":"mutation useAssetFavoriteMutation(\n  $asset: AssetRelayID!\n  $isFavorite: Boolean!\n) {\n  assets {\n    updateFavorite(asset: $asset, isFavorite: $isFavorite)\n  }\n}\n","variables":{"asset":base64.b64encode(thiss.encode("ascii")).decode('ascii'),"isFavorite":True}}
    hedaders={
    'X-BUILD-ID':'hkYm1IElKRJQ4nEeB4JtC',
    'x-datadog-origin':'rum',
    'Authorization':'JWT '+auth,
    'x-datadog-sampling-priority':'1',
    'Content-Type':'application/json',
    'Accept':'*/*',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36',
    'x-signed-query':'d3f55288dd86ea745448362b88dacd4316547c5c4259bfd33caff7e3b3c1b333',
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
    response=session.post('https://api.opensea.io/graphql/',json=data,headers=hedaders,proxies=proxy)
    if '"updateFavorite":true' in response.text:
        return True
    else:
        print(response.text)
        return False
