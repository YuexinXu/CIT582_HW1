import hashlib
import uuid

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    while True:
    	nonce = uuid.uuid4().bytes
    	hash_nonce = hashlib.sha256(nonce).digest()

    	cur = len(target_string) - 1
    	if cur < 0:
    		return nonce
    	flag = True
    	for j in range(len(hash_nonce) - 1, -1, -1):
    		byte = hash_nonce[j]
    		if not flag:
    			break
    		for i in range(8):
    			if (byte & (1 << i)) == 0:
    				cur_bit = '0'
    			else:
    				cur_bit = '1'
    			if cur_bit == target_string[cur]:
    				cur -= 1
    			else:
    				flag = False
    				break
    			if cur < 0:
    				return (nonce)
