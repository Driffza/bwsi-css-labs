import numpy as np
import hashlib

def my_hash(data):
    if not isinstance(data, str):
        d2 = data.tobytes()
    else:
        d2 = data.encode('utf-8')
       
    return hashlib.md5(d2).hexdigest()

def round_and_report(data, num_decimals):
    d2 = np.rint(data * 10**num_decimals).astype(np.int32)
    return my_hash(d2)

arr = np.array([np.pi, np.pi*3, 9.93493])

print(((arr)))
