import requests
import uuid
from typing import Optional, Any, TypedDict, Union, TypeVar, Generic


class RequestsInstance(requests.Session):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.headers.update({
            'Content-Type': 'application/json'
        })

    def request(self, method, url, *args, **kwargs):
        url = self.base_url + url
        return super().request(method, url, *args, **kwargs)


T = TypeVar('T')


class BaseResponse(Generic[T], TypedDict):
    data: T
    success: bool
    error: Any


class InitData(TypedDict):
    txHash: str
    datum: str
    rngfid: str
    rnlen: int


class MintData(TypedDict):
    txHash: str
    oracleDIDUnit: str


class RegisterData(TypedDict):
    txHash: str
    oracleDIDUnit: str
    rngOutput: str


class UpdateData(TypedDict):
    txHash: str
    oracleDIDUnit: str
    rngOutput: str


class QueryData(TypedDict):
    rngOutput: str


class RNG:
    def __init__(self,
                 network: 0 | 1,
                 blockfrostApiKey: str,
                 walletSeed: str,
                 oracleCBOR: str,
                 rngCBOR: str,
                 ogmiosUrl: str,
                 rngAPIURL: str,
                 rngfid: Optional[str] = None,
                 rngOutputLen: int = 4,
                 ):
        self.network = network
        self.blockfrostApiKey = blockfrostApiKey
        self.walletSeed = walletSeed
        self.oracleCBOR = oracleCBOR
        self.rngCBOR = rngCBOR
        self.rngfid = rngfid if rngfid is not None else self.getRandomID()
        self.rngOutputLen = rngOutputLen
        self.ogmiosURL = ogmiosUrl

        self.instance = RequestsInstance(rngAPIURL)


    def __str__(self):
        return "{\n" + ",\n".join([f'  "{key}": {getattr(self, key)!r}' for key in vars(self)]) + "\n}"

    def init(self) -> BaseResponse[InitData]:
        """
            Initiate RNG DID function.

            Returns:
            txHash: Transaction hash of initiated RNG ID
            datum: Datum Hash
            rngfid: RNG ID
            rnlen: Random Number Length
        """
        try:
            data = {
                "network": self.network,
                "blockfrostApiKey": self.blockfrostApiKey,
                "walletSeed": self.walletSeed,
                "CBORhex": self.rngCBOR,
                "rngfid": self.rngfid,
                "rnlen": self.rngOutputLen,
            }
            response = self.instance.post("/api/rng/generate", json=data)

            resData = response.json()

            return BaseResponse[InitData](resData)
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")

    def mint(self, oracleDIDName: str) -> BaseResponse[MintData]:
        """
            Mint Oracle DID function.

            Parameters:
            oracleDIDName: Name of the Oracle DID (UTF-8 encoded)

            Returns:
            txHash: Transaction hash of Mint
            oracleDIDUnit: Unit ID of Oracle DID
        """
        try:
            data = {
                "network": self.network,
                "blockfrostApiKey": self.blockfrostApiKey,
                "walletSeed": self.walletSeed,
                "oracleDIDName": oracleDIDName,
            }
            response = self.instance.post("/api/oracle/mint", json=data)

            resData = response.json()

            return BaseResponse[MintData](resData)
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")

    def register(self, oracleDIDUnit: str, initRNGTx: str) -> BaseResponse[RegisterData]:
        """
            Register Oracle DID function.

            Parameters:
            initRNGTx: Transaction hash of initiated RNG ID
            oracleDIDName: Name of the Oracle DID (UTF-8 encoded)

            Returns:
            txHash: Transaction hash of regitered Oracle DID
            oracleDIDUnit: Unit ID of Oracle DID
            rngOutput: Random number from the Oracle
        """
        try:
            data = {
                "network": self.network,
                "blockfrostApiKey": self.blockfrostApiKey,
                "walletSeed": self.walletSeed,
                "CBORhex": self.oracleCBOR,
                "ogmiosUrl": self.ogmiosURL,
                "rngfid": self.rngfid,
                "rnlen": self.rngOutputLen,
                "initRNGTx": initRNGTx,
                "oracleDIDUnit": oracleDIDUnit,
            }
            response = self.instance.post("/api/oracle/register", json=data)

            resData = response.json()

            return BaseResponse[RegisterData](resData)
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")

    def update(self, oracleDIDUnit: str, initRNGTx: str, currUpdatedOracleDIDTx: str) -> BaseResponse[UpdateData]:
        """
            Update Oracle DID function.

            Parameters:
            initRNGTx: Transaction hash of initiated RNG ID
            oracleDIDName: Name of the Oracle DID (UTF-8 encoded)
            currUpdatedOracleDIDTx: Latest Oracle DID transaction hash for UTXO reference in the contract

            Returns:
            txHash: Transaction hash of regitered Oracle DID
            oracleDIDUnit: Unit ID of Oracle DID
            rngOutput: Random number from the Oracle
        """
        try:
            data = {
                "network": self.network,
                "blockfrostApiKey": self.blockfrostApiKey,
                "walletSeed": self.walletSeed,
                "CBORhex": self.oracleCBOR,
                "ogmiosUrl": self.ogmiosURL,
                "rngfid": self.rngfid,
                "rnlen": self.rngOutputLen,
                "initRNGTx": initRNGTx,
                "oracleDIDUnit": oracleDIDUnit,
                "currUpdatedOracleDIDTx": currUpdatedOracleDIDTx,
            }

            response = self.instance.post("/api/oracle/update", json=data)

            resData = response.json()

            return BaseResponse[UpdateData](resData)
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")

    def query(self, currUpdatedOracleDIDTx: str) -> BaseResponse[QueryData]:
        """
            Update Oracle DID function.

            Parameters:
            currUpdatedOracleDIDTx: Latest Oracle DID transaction hash for UTXO reference in the contract

            Returns:
            rngOutput: Random number from the Oracle
        """
        try:
            data = {
                "network": self.network,
                "blockfrostApiKey": self.blockfrostApiKey,
                "currUpdatedOracleDIDTx": currUpdatedOracleDIDTx,
            }

            response = self.instance.post("/api/oracle/query", json=data)

            resData = response.json()

            return BaseResponse[QueryData](resData)
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")

    def getRandomID(self) -> str:
        id = str(uuid.uuid4()).replace('-', '')[:24]
        return f'rngfid_{id}'
