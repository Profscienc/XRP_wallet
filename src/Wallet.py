from xrpl.wallet import generate_faucet_wallet
from xrpl.clients import JsonRpcClient
client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")

test_wallet = generate_faucet_wallet(client)
print(test_wallet)
