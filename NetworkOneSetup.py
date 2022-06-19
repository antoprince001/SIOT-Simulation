import json
from BlockchainInterface import createDevice
from utils.KeyPairGenerator import generatekeyPair
import time

# Device 1 - Type : Apartment
deviceType = 0
deviceMapper =  "private"
lat = "13.082680"
long = "80.270721"
keyPair = generatekeyPair()
publicKey =  keyPair["public"]
privateKey = keyPair["private"]
domainLocator = "iotnet"

with open("./output/NetworkOne.txt","w") as f:
    st = time.time()
    f.write("\n----------------------------\n")
    receipt = createDevice(deviceType , deviceMapper, lat, long, publicKey, privateKey, domainLocator)
    f.write(str(receipt))
    print(receipt)
    et = time.time()
    print("Time taken in seconds for device 1 : "+str(et-st))
    f.write("Time taken in seconds for device 1 : "+str(et-st))


# Device 2 - Type : Vehicle
deviceType = 1
deviceMapper = "private"
lat = "13.082680"
long = "80.270721"
keyPair = generatekeyPair()
publicKey =  keyPair["public"]
privateKey = keyPair["private"]
domainLocator = "iotnet"


with open("./output/NetworkOne.txt","w") as f:
    st = time.time()
    f.write("\n----------------------------\n")
    receipt = createDevice(deviceType , deviceMapper, lat, long, publicKey, privateKey, domainLocator)
    f.write(str(receipt))
    print(receipt)
    et = time.time()
    print("Time taken in seconds for device 2 : "+str(et-st))
    f.write("Time taken in seconds for device 2 : "+str(et-st))


# Device 3 - Type : Mall
deviceType = 2 
deviceMapper =  "private"
lat = "13.082680"
long = "80.270721"
keyPair = generatekeyPair()
publicKey =  keyPair["public"]
privateKey = keyPair["private"]
domainLocator = "iotnet"


with open("./output/NetworkOne.txt","w") as f:
    st = time.time()
    f.write("\n----------------------------\n")
    receipt = createDevice(deviceType , deviceMapper, lat, long, publicKey, privateKey, domainLocator)
    f.write(str(receipt))
    print(receipt)
    et = time.time()
    print("Time taken in seconds for device 3 : "+str(et-st))
    f.write("Time taken in seconds for device 3 : "+str(et-st))

