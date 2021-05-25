import hashlib
import uuid

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    while True:
    	nonce = uuid.uuid4().bytes
    	hash_nonce = hashlib.sha256(nonce).digest()

    	cur = 0
    	if cur >= len(target_string):
    		return nonce
    	flag = True
    	for byte in hash_nonce:
    		if not flag:
    			break
    		for i in range(7, -1, -1):
    			if (byte & (1 << i)) == 0:
    				cur_bit = '0'
    			else:
    				cur_bit = '1'
    			if cur_bit == target_string[cur]:
    				cur += 1
    			else:
    				flag = False
    				break
    			if cur == len(target_string):
    				return nonce
