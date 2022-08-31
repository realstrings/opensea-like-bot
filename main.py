from audioop import add
import utils
import tosign
import requests
import json
import auth
import utils
import like
from web3.auto import w3
from eth_account.messages import encode_defunct
import random
import threading
import getid

count = 0

with open("config.json") as c:
    jsonn=json.loads(c.read())
    proxy=jsonn["proxy"]
    proxy={'http':'http://'+proxy,'https':'http://'+proxy}
    nft=jsonn["nft"]
    threads=jsonn["threads"]

# we need to get id of the nft from given url, id is purely for opensea identification
id = str(getid.get_id(nft))
print(id)




def thread():
    global count
    while True:
        try:
            print(count)
            session=requests.session()
            # getting random num, converting it to int, this will be our seed
            privatekey=str(random.randint(111111111,99999999999999999))
            # getting bytes of private key from seed, this will be needed 4 signing
            realkey=utils.get_bytes(privatekey)
            # getting public key (address) from seed, needed in opensea backend
            address=utils.get_ethereum_address_from_private_key(privatekey)
            # getting message with nonce from opensea
            message=tosign.get_message(address,session,proxy)
            # Encode a message for signing, using an old, unrecommended approach.
            msg = encode_defunct(text=message)
            # signing that message with private key bytes
            signed_message = w3.eth.account.sign_message(msg, private_key=realkey)
            # signed message
            signature=signed_message.signature.hex()
            # logging in, proving its $address with our signed message and then getting JWT token on opensea
            jwt=auth.auth(message,address,signature,session,proxy)
            # liking the stuff we want
            result = like.like(id,jwt,address,session,proxy)
            if result:
                count = count + 1
        except Exception:
            return thread()

for x in range(50):
    threading.Thread(target=thread).start()

