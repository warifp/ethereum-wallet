from eth_account import Account
import secrets
import json

class Wallet:
    def create(self):
        __secrets = secrets.token_hex(32)
        __private_key = "0x" + __secrets
        __account = Account.from_key(__private_key)

        d = {
            "private_key": __private_key,
            "address": __account.address
        }

        return d

# init
wallet = Wallet()
print(json.dumps(wallet.create(), indent=4))