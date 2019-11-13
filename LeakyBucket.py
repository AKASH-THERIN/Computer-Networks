import time
import random
bucketSize =512
def bktInput(size,rate):
    if size>bucketSize:
        print("\n Bucket Overflow")
    else:
        time.sleep(1)
        while size>rate:
            print("\n {} bytes sent".format(rate))
            size -=rate
            time.sleep(1)
        if size >0:
            print("\n Last {} bytes sent".format(size))
        print("\n Bucket output successful")

outputRate = int(input("Enter the ouput rate : "))
for i in range(5):
    print(random.randint(0,1000))
    time.sleep(random.randint(0,1000))
    packetSize = random.randint(0,1000)
    print("\n Packet Number : {}  \n Packet Size : {} ".format((i+1),packetSize))
    bktInput(packetSize,outputRate)
    
    
    
"""
OUTPUT :
Enter the ouput rate : 43

 Packet Number : 1 
 Packet Size : 26 
 Last 26 bytes sent

 Bucket output successful
 
 

 Packet Number : 2 
 Packet Size : 150 
 43 bytes sent
 43 bytes sent
 43 bytes sent
 Last 21 bytes sent

 Bucket output successful



 Packet Number : 3 
 Packet Size : 703 
 Bucket Overflow


 
 Packet Number : 4 
 Packet Size : 740 
 Bucket Overflow



 Packet Number : 5 
 Packet Size : 650 
 Bucket Overflow
 
 
"""

