from web3 import Web3
import json

contractAddress = Web3.toChecksumAddress('0x5d2baae89554903d061590a101252b488fbdd16b')
private_key = 'a1dd85b68f449a7acbed0f91d9cc586b7b943a9d057ddf6f5327f13204f69e64'

#infura_url = "https://kovan.infura.io/v3/16497e91567d468facb98a99c27db479"
infura_url = "wss://kovan.infura.io/ws/v3/16497e91567d468facb98a99c27db479"
web3 = Web3(Web3.WebsocketProvider(infura_url))

abi=json.loads('[{"inputs":[{"internalType":"uint256","name":"deviceType","type":"uint256"},{"internalType":"string","name":"_deviceMapper","type":"string"},{"internalType":"string","name":"_lat","type":"string"},{"internalType":"string","name":"_long","type":"string"},{"internalType":"string","name":"publicKey","type":"string"},{"internalType":"string","name":"privateKey","type":"string"},{"internalType":"string","name":"_domainLocator","type":"string"}],"name":"addDevice","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"deviceId","type":"uint256"}],"name":"dnsLookup","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"domainServer","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"domains","outputs":[{"internalType":"string","name":"domainLocator","type":"string"},{"internalType":"string","name":"lat","type":"string"},{"internalType":"string","name":"long","type":"string"},{"internalType":"uint256","name":"networkId","type":"uint256"},{"internalType":"string","name":"category","type":"string"},{"internalType":"bool","name":"exists","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"deviceId","type":"uint256"}],"name":"getKeyPair","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"deviceId","type":"uint256"}],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"nameServer","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_domainLocator","type":"string"},{"internalType":"string","name":"_lat","type":"string"},{"internalType":"string","name":"_long","type":"string"},{"internalType":"uint256","name":"_networkId","type":"uint256"},{"internalType":"string","name":"_category","type":"string"}],"name":"registerDomain","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"}]')

#web3 = Web3(Web3.HTTPProvider(infura_url))
web3.eth.defaultAccount = Web3.toChecksumAddress("0x9aa49368f973f32a1d8e9c8d9f58fd203c625bee")



contract = web3.eth.contract(
     address = contractAddress,
     abi = abi,
 )


# Following are the functions to interact with Kovan testnet blockchain

def createDomain(domainLocator , lat, long, networkId, category, exists):
    """Adds the iot domain to the blockchain"""
    try:
        transaction = contract.functions.registerDomain(domainLocator , lat, long, networkId, category).buildTransaction()
        transaction.update({ 'gas' : 2000000 })
        transaction.update({ 'nonce' : web3.eth.getTransactionCount('0x9aa49368F973F32a1d8E9C8D9F58fd203C625BEe') })
        signed_tx = web3.eth.account.signTransaction(transaction, private_key)
        txn_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        receipt = web3.eth.waitForTransactionReceipt(txn_hash)
        return receipt
    except Exception as e: 
         print(e)
         return 'Iot domain could not be added'


# Note : Source should be integer or else it will throw error
def createDevice(deviceType , deviceMapper, lat, long, publicKey, privateKey, domainLocator):
    """Adds the iot device to the blockchain"""
    try:
        transaction = contract.functions.addDevice(deviceType , deviceMapper, lat, long, publicKey, privateKey, domainLocator).buildTransaction()
        transaction.update({ 'gas' : 2000000 })
        transaction.update({ 'nonce' : web3.eth.getTransactionCount('0x9aa49368F973F32a1d8E9C8D9F58fd203C625BEe') })
        signed_tx = web3.eth.account.signTransaction(transaction, private_key)
        txn_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        receipt = web3.eth.waitForTransactionReceipt(txn_hash)
        return receipt
    except :
         return 'Iot device could not be added'

def queryDomains(id):
    """Retrieves the domain details from the blockchain"""
    try:
        domain = contract.functions.domains(id).call()
        return domain
    except Exception as e:
        print(e)
        return 'Error finding the data'

def queryDNS(id):
    """Retrieves the DNS details from the blockchain"""
    try:
        domain = contract.functions.dnsLookup(id).call()
        return domain
    except Exception as e:
        print(e)
        return 'Error finding the data'

def queryKeyPair(id):
    """Retrieves the DNS details from the blockchain"""
    try:
        keyPair = contract.functions.getKeyPair(id).call()
        return keyPair
    except Exception as e:
        print(e)
        return 'Error finding the data'