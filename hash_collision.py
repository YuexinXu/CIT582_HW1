import hashlib
import os
import uuid


def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    while True: 
          x = uuid.uuid4().bytes
          y = uuid.uuid4().bytes

          if x == y:
               continue
          hash_x = hashlib.sha256(x).digest()
          hash_y = hashlib.sha256(y).digest()
          if num_matches(hash_x, hash_y) >= k:
               break    
    
    return( x, y )


def num_matches(hash_x, hash_y):
    match = 0
    for i in range(len(hash_x) - 1, -1, -1):
        xor = (hash_x[i] ^ hash_y[i])
        if xor == 0:
            match += 8
        else:
            if xor % 2 == 0:
                xor = xor / 2
                match += 1
            break
    return match
