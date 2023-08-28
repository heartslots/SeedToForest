import hashlib
from datetime import datetime

type1 = [['#','@','@'],['@','@','@'],['@','@','@']]
type2 = [['@','#','@'],['@','@','@'],['@','@','@']]
type3 = [['@','@','#'],['@','@','@'],['@','@','@']]
type4 = [['@','@','@'],['#','@','@'],['@','@','@']]
type5 = [['@','@','@'],['@','#','@'],['@','@','@']]
type6 = [['@','@','@'],['@','@','#'],['@','@','@']]
type7 = [['@','@','@'],['@','@','@'],['#','@','@']]
type8 = [['@','@','@'],['@','@','@'],['@','#','@']]
type9 = [['@','@','@'],['@','@','@'],['@','@','#']]
type0 = [['@','@','@'],['@','@','@'],['@','@','@']]

tileset = [type1, type2, type3, type4, type5, type6, type7, type8, type9, type0]

#seed = '20'
seed = str(datetime.now().microsecond) + str(datetime.now())

def hash(seed):
    data = seed.encode()
    hash_object = hashlib.sha1()
    hash_object.update(data)
    hex_dig = hash_object.hexdigest()

    return str(int(hex_dig, base=16))

def mapGeneration(rannum):
    n = 5
    treemap = []
    for i in range(25):
        treemap.append(tileset[int(rannum[i+1])])
    
    result = [treemap[i * n:(i + 1) * n] for i in range((len(treemap) + n - 1) // n )] 

    return result

def sweep(lists):
    treemap = []
    div = 15

    for i in range(5):
        for j in range(3):
            for m in range(5):
                for n in range(3):
                    treemap.append(lists[i][m][j][n])
    result = [treemap[i * div:(i + 1) * div] for i in range((len(treemap) + div - 1) // div )]

    return result


print(sweep(mapGeneration(hash(seed))))
print(sweep(mapGeneration(hash(seed))))