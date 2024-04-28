from rng_lib import RNG

# Define parameters
network = 0
blockfrostApiKey = "YOUR_BLOCKFROST_API_KEY"
walletSeed = "YOUR_WALLET_SEED"
CBORhex = "YOUR_CBOR_HEX"
rngfid = "YOUR_RNGFID"
rnlen = 10
ogmiosUrl = "YOUR_OGMIOS_URL"
RNG_API_URL="http://localhost:7000"

# Initialize RNG object with parameters
rng = RNG(network, blockfrostApiKey, walletSeed, CBORhex, rngfid, rnlen, ogmiosUrl, RNG_API_URL=RNG_API_URL)

# Initiating RNG
try:
    print("Initiating RNG...")
    response = rng.initiate()
    print("Initiate response: ", response)
except Exception as e:
    print("Error during initialization:", e)

# Minting Oracle DID
try:
    assetName = "YOUR_ASSET_NAME"
    print(f"Minting Oracle DID for asset '{assetName}'...")
    response = rng.mintOracleDid(assetName)
    print("Minting response:", response)
except Exception as e:
    print("Error during minting:", e)

# Registering Oracle DID
try:
    initiator = "INITIATOR_ADDRESS"
    seedtxid = "SEED_TRANSACTION_ID"
    oracleDid = "ORACLE_DID"
    print("Registering Oracle DID...")
    response = rng.didRegister(initiator, seedtxid, oracleDid)
    print("Registration response:", response)
except Exception as e:
    print("Error during registration:", e)

# Updating Oracle
try:
    lastUpdatedTx = "LAST_UPDATED_TRANSACTION_ID"
    oracleDid = "ORACLE_DID"
    seedtxid = "SEED_TRANSACTION_ID"
    print("Updating Oracle...")
    response = rng.updateOracle(initiator, lastUpdatedTx, oracleDid, seedtxid)
    print("Update response:", response)
except Exception as e:
    print("Error during update:", e)
