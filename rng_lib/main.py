import requests

class RNG:
    def __init__(self, network: int, blockfrostApiKey: str, walletSeed: str, CBORhex: str, rngfid: str, rnlen: int, ogmiosUrl: str, RNG_API_URL: str = ""):
        self.network = network
        self.blockfrostApiKey = blockfrostApiKey
        self.walletSeed = walletSeed
        self.CBORhex = CBORhex
        self.rngfid = rngfid
        self.rnlen = rnlen
        self.ogmiosUrl = ogmiosUrl
        self.RNG_API_URL = RNG_API_URL
    
    def __str__(self):
        return "{\n" + ",\n".join([f'  "{key}": {getattr(self, key)!r}' for key in vars(self)]) + "\n}"
    
    def initiate(self):
        try:
            url = f"{self.RNG_API_URL}/api/initiate"
            headers = {
                "Content-Type": "application/json",
            }
            data = {
                "network": self.network,
                "blockfrostApiKey": self.blockfrostApiKey,
                "walletSeed": self.walletSeed,
                "CBORhex": self.CBORhex,
                "rngfid": self.rngfid,
                "rnlen": self.rnlen,
            }

            response = requests.post(url, headers=headers, json=data)

            if not response.ok:
                errorResJson = response.json()
                print(errorResJson)
                raise Exception("Failed to initiate RNG")

            responseData = response.json()
            return responseData
        except:
            raise Exception("Error initiating RNG")
        
    def mintOracleDid(self, assetName: str):
        try:
            url = f"{self.RNG_API_URL}/api/mint-oracle"
            headers = {
                "Content-Type": "application/json",
            }
            data = {
                "network": self.network,
                "blockfrostApiKey": self.blockfrostApiKey,
                "walletSeed": self.walletSeed,
                "assetName": assetName,
            }

            response = requests.post(url, headers=headers, json=data)

            if not response.ok:
                errorResJson = response.json()
                print(errorResJson)
                raise Exception("Failed to mint oracle DID")

            responseData = response.json()
            return responseData
        except Exception as error:
            raise Exception("Error minting oracle DID")

    def didRegister(self,initiator: str,seedtxid: str,oracleDid: str):
        try:
            url=f"{self.RNG_API_URL}/api/did-register"
            headers= {
                'Content-Type': 'application/json'
            }
            data = {
                "network": self.network,
                "blockfrostApiKey": self.blockfrostApiKey,
                "ogmiosUrl": self.ogmiosUrl,
                "walletSeed": self.walletSeed,
                "CBORhex": self.CBORhex,
                "initiator": initiator,
                "rngfid": self.rngfid,
                "seedtxid": seedtxid,
                "rnlen": self.rnlen,
                "oracleDid": oracleDid,
            }
            response = requests.post(url,headers=headers,json=data)
            if not response.ok:
                raise Exception("Failed to register")
            responseData=response.json()
            return responseData
        except Exception as err:
            raise Exception("Error registering oracle DID")

    def updateOracle(self, initiator: str,lastUpdatedTx: str, oracleDid: str, seedtxid: str):
        try:
            url = f"{self.RNG_API_URL}/api/update-oracle"
            headers = {
                'Content-Type': 'application/json',
            }
            data = {
                "network": self.network,
                "blockfrostApiKey": self.blockfrostApiKey,
                "ogmiosUrl": self.ogmiosUrl,
                "walletSeed": self.walletSeed,
                "CBORhex": self.CBORhex,
                "initiator": initiator,
                "rngfid": self.rngfid,
                "seedtxid": seedtxid,
                "rnlen": self.rnlen,
                "lastUpdatedTx": lastUpdatedTx,
                "oracleDid": oracleDid,
            }

            response = requests.post(url, headers=headers, json=data)

            if not response.ok:
                raise Exception("Failed to update oracle")

            responseData = response.json()
            return responseData
        except Exception as error:
            raise Exception("Error updating oracle")

