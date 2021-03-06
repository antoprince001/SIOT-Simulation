from BlockchainInterface import createDomain
import time

domainLocator = "iotnet"
lat = "13.082680"
long = "80.270721"
networkId = 42
category = "private"
exists = 1

with open("./output/DomainReceipt.txt","w") as f:
    st = time.time()
    f.write("\n----------------------------\n")
    receipt = createDomain(domainLocator , lat, long, networkId, category, exists)
    f.write(str(receipt))
    print(receipt)
    et = time.time()
    print("Time taken in seconds : "+str(et-st)) 

    # time when failed : 0.0059986114501953125



'''
AttributeDict(
    {'blockHash': HexBytes('0xcafe94697d5c2acb58e63b3ff32f8b63bb594f94fb2d324a2d5ca0616052ea9e'), 
    'blockNumber': 32255717, 
    'contractAddress': None, 
    'cumulativeGasUsed': 189193, 
    'effectiveGasPrice': 2000000007, 
    'from': '0x9aa49368F973F32a1d8E9C8D9F58fd203C625BEe', 
    'gasUsed': 189193, 'logs': [], 
    'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'), 
    'status': 1, 
    'to': '0x5D2baaE89554903d061590A101252b488FBDD16B', 
    'transactionHash': HexBytes('0x009abccc69f61483fc1a22aef1f0552038691aaf59bd73d3dadb256004d14fc5'), 
    'transactionIndex': 0, 
    'type': '0x2'}
)
Time taken in seconds : 12.259176015853882
'''


domainLocator = "iotnet2"
lat = "13.082680"
long = "80.270721"
networkId = 42
category = "private"
exists = 1

with open("./output/DomainReceipt.txt","a") as f:
    st = time.time()
    f.write("\n----------------------------\n")
    receipt = createDomain(domainLocator , lat, long, networkId, category, exists)
    f.write(str(receipt))
    print(receipt)
    et = time.time()
    print("Time taken in seconds : "+str(et-st)) 




'''
AttributeDict({
    'blockHash': HexBytes('0x6bd8f5e1fc85b65eda068c87d922b86a7389c1f13fce375d67ce4b0e5136d060'), 
    'blockNumber': 32258503, 
    'contractAddress': None, 
    'cumulativeGasUsed': 189193, 
    'effectiveGasPrice': 2500000007, 
    'from': '0x9aa49368F973F32a1d8E9C8D9F58fd203C625BEe', 
    'gasUsed': 189193, 
    'logs': [], 
    'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'), 
    'status': 1, 
    'to': '0x5D2baaE89554903d061590A101252b488FBDD16B', 
    'transactionHash': HexBytes('0x954e6dbeab9eab7094e4355d534b66fe808673b84c33a25f2f7edb0c9aaf537b'), 
    'transactionIndex': 0, 
    'type': '0x2'})
Time taken in seconds : 16.363840341567993
'''