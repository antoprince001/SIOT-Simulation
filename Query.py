from BlockchainInterface import queryDNS, queryDomains
import time

st =time.time()
print(queryDomains(id=0))
et = time.time()
print("Time taken to query domain 1: "+str(et-st))
'''
['iotnet', '13.082680', '80.270721', 42, 'private', True]
Time taken to query domain 1: 2.1722378730773926
Storage : 0.058 Kilobytes
'''

st =time.time()
print(queryDomains(id=1))
et = time.time()
print("Time taken to query domain 2: "+str(et-st))
'''
['iotnet2', '13.082680', '80.270721', 42, 'private', True]
Time taken to query domain 2: 1.7475907802581787
Storage : 0.061 Kilobytes
'''


# DNS individual entry Storage size : 0.034 Kilobytes
# Devices from Network 1
st =time.time()
print(queryDNS(id=0))
et = time.time()
print("Time taken to query DNS: "+str(et-st))
'''
['13.082680', '80.270721', 42]
Time taken to query DNS: 1.6760962009429932
'''

st =time.time()
print(queryDNS(id=1))
et = time.time()
print("Time taken to query DNS: "+str(et-st))
'''
['13.082680', '80.270721', 42]
Time taken to query DNS: 1.6470143795013428
'''

st =time.time()
print(queryDNS(id=2))
et = time.time()
print("Time taken to query DNS: "+str(et-st))
'''
['13.082680', '80.270721', 42]
Time taken to query DNS: 1.647613525390625
'''

# Devices from Network 2
st =time.time()
print(queryDNS(id=3))
et = time.time()
print("Time taken to query DNS: "+str(et-st))
'''
['13.082680', '80.270721', 42]
Time taken to query DNS: 1.758908987045288
'''

st =time.time()
print(queryDNS(id=4))
et = time.time()
print("Time taken to query DNS: "+str(et-st))
'''
['13.082680', '80.270721', 42]
Time taken to query DNS: 1.9878973960876465
'''

st =time.time()
print(queryDNS(id=5))
et = time.time()
print("Time taken to query DNS: "+str(et-st))
'''
['13.082680', '80.270721', 42]
Time taken to query DNS: 2.06646990776062
'''

