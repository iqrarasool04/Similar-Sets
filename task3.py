from random import shuffle

a = "flying fish flew by the space station"
b = "he will not allow you to bring your sticks of dynamite and pet armadillo along"
c = "he figured a few sticks of dynamite youre easier than a fishing pole to catch an armadillo"

k = 2
def shingle(text: str, k: int):
    shingle_set = []
    for i in range (len(text) - k+1):
        shingle_set.append(text[i:i+k])
    return set(shingle_set)

def create_hash_func(size: int):
    hash_ex = list(range(1, size+1))
    shuffle(hash_ex)
    return hash_ex

def build_minhash_func(vocab_size: int, nbits: int):
    hashes = []
    for _ in range(nbits):
        hashes.append(create_hash_func(vocab_size))
    return hashes

def create_hash(vector: list):
    signature = []
    for func in minhash_func:
        for i in range(1, len(vocab)+1):
            idx = func.index(i)
            signature_val = vector[idx]
            if signature_val == 1:
                signature.append(idx)
                break
    return signature

def jaccard(a: set, b:set):
    return len(a.intersection(b)) / len(a.union(b))

a = shingle(a, k)
b = shingle(b, k)
c = shingle(c, k)
vocab = list(a.union(b).union(c))
a_1hot = [1 if x in a else 0 for x in vocab]
b_1hot = [1 if x in b else 0 for x in vocab]
c_1hot = [1 if x in c else 0 for x in vocab]

minhash_func = build_minhash_func(len(vocab),20)

a_sig = create_hash(a_1hot)
b_sig = create_hash(b_1hot)
c_sig = create_hash(c_1hot)

print('Signature of a: ',a_sig)
print('Signature of b: ',b_sig)
print('Signature of c: ',c_sig)

print(jaccard(a,b), jaccard(set(a_sig), set(b_sig)))
print(jaccard(a,c), jaccard(set(a_sig), set(c_sig)))
print(jaccard(b,c), jaccard(set(b_sig), set(c_sig)))
