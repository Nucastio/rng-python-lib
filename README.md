# RNG API Library

## Installation

To install the required dependency:

```sh
pip install py-rng-lib
```

## Usage

### Importing the Library

```python
from rng_lib import RNG
```

### Initialization

To initialize the RNG library, you need to provide the following parameters:

- `network`: The network to use (0 for testnet, 1 for mainnet).
- `blockfrostApiKey`: Your Blockfrost API key.
- `walletSeed`: The seed phrase for your wallet.
- `oracleCBOR`: Oracle Contract CBOR-encoded hexadecimal string.
- `rngCBOR`: RNG Contract CBOR-encoded hexadecimal string.
- `ogmiosUrl`: The URL of the Ogmios server.
- `rngAPIURL`: The URL of the RNG API.
- `rngfid` (optional): The identifier for the RNG.
- `rngOutputLen` (optional): The length of the random number (default is 4).

Example:

```python
rng = RNG(
    network=0,
    blockfrostApiKey='your-blockfrost-api-key',
    walletSeed='your-wallet-seed',
    oracleCBOR='oracle-cbor',
    rngCBOR='rng-cbor',
    ogmiosUrl='https://ogmios-url',
    rngAPIURL='https://rng-api-url'
)
```

### Methods

#### `init()`

Initiates an RNG DID.

- **Returns**:
  - `txHash`: Transaction hash of initiated RNG ID.
  - `datum`: Datum Hash.
  - `rngfid`: RNG ID.
  - `rnlen`: Random Number Length.

Example:

```python
init_result = rng.init()
print(init_result)
```

#### `mint(oracleDIDName: str)`

Mints an Oracle DID to the wallet.

- **Parameters**:

  - `oracleDIDName`: Name of the Oracle DID (UTF-8 encoded).

- **Returns**:
  - `txHash`: Transaction hash of Mint.
  - `oracleDIDUnit`: Unit ID of Oracle DID.

Example:

```python
mint_result = rng.mint('my-oracle-did')
print(mint_result)
```

#### `register(oracleDIDUnit: str, initRNGTx: str)`

Registers an Oracle DID to the contract.

- **Parameters**:

  - `initRNGTx`: Transaction hash of initiated RNG ID.
  - `oracleDIDUnit`: Unit ID of Oracle DID.

- **Returns**:
  - `txHash`: Transaction hash of registered Oracle DID.
  - `oracleDIDUnit`: Unit ID of Oracle DID.
  - `rngOutput`: Random number from the Oracle.

Example:

```python
register_result = rng.register('oracle-did-unit', 'init-rng-tx-hash')
print(register_result)
```

#### `update(oracleDIDUnit: str, initRNGTx: str, currUpdatedOracleDIDTx: str)`

Updates an Oracle DID.

- **Parameters**:

  - `initRNGTx`: Transaction hash of initiated RNG ID.
  - `oracleDIDUnit`: Unit ID of Oracle DID.
  - `currUpdatedOracleDIDTx`: Latest Oracle DID transaction hash for UTXO reference in the contract.

- **Returns**:
  - `txHash`: Transaction hash of updated Oracle DID.
  - `oracleDIDUnit`: Unit ID of Oracle DID.
  - `rngOutput`: Random number from the Oracle.

Example:

```python
update_result = rng.update('oracle-did-unit', 'init-rng-tx-hash', 'current-updated-oracle-did-tx')
print(update_result)
```

#### `query(currUpdatedOracleDIDTx: str)`

Queries the RNG data of Oracle DID.

- **Parameters**:

  - `currUpdatedOracleDIDTx`: Latest Oracle DID transaction hash for UTXO reference in the contract.

- **Returns**:
  - `rngOutput`: Random number from the Oracle.

Example:

```python
query_result = rng.query('current-updated-oracle-did-tx')
print(query_result)
```

#### `getRandomID()`

Generates a random ID for RNG ID.

- **Returns**: RNG ID.

Example:

```python
random_id = rng.getRandomID()
print(random_id)
```

### CLI App

For integrating this library, you can refer to this [repository](https://github.com/Nucastio/rng-py-cli).
