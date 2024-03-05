import re
from random import shuffle

a = "The quick brown fox jumps over the lazy dog"
b = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
c = "The five boxing wizards jump quickly"
d = "How vexingly quick daft zebras jump!"
e = "Bright vixens jump; dozy fowl quack"

#preprocessing
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

#shingling
k = 3
def shingle(text: str, k: int):
    shingle_set = []
    for i in range (len(text) - k+1):
        shingle_set.append(text[i:i+k])
    return set(shingle_set)

a = preprocess_text(a)
b = preprocess_text(b)
c = preprocess_text(c)
d = preprocess_text(d)
e = preprocess_text(e)

print('Preprocessing text a: ',a)
print('Preprocessing text b: ',b)
print('Preprocessing text c: ',c)
print('Preprocessing text d: ',d)
print('Preprocessing text e: ',e)

a = shingle(a, k)
b = shingle(b, k)
c = shingle(c, k)
d = shingle(d, k)
e = shingle(e, k)

print('Shingles of a: ',a)
print('Shingles of b: ',b)
print('Shingles of c: ',c)
print('Shingles of d: ',d)
print('Shingles of e: ',e)

#vector representation
vocab = list(a.union(b).union(c).union(d).union(e))
a_1hot = [1 if x in a else 0 for x in vocab]
b_1hot = [1 if x in b else 0 for x in vocab]
c_1hot = [1 if x in c else 0 for x in vocab]
d_1hot = [1 if x in d else 0 for x in vocab]
e_1hot = [1 if x in e else 0 for x in vocab]

#minhashing
def create_hash_func(size: int):
    hash_ex = list(range(1, size+1))
    shuffle(hash_ex)
    return hash_ex

def build_minhash_func(vocab_size: int, nbits: int):
    hashes = []
    for _ in range(nbits):
        hashes.append(create_hash_func(vocab_size))
    return hashes

minhash_func = build_minhash_func(len(vocab),20)

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

#LSH
def split_vector(signature,b):
    assert len(signature) % b == 0
    r = int(len(signature) / b)
    subvecs = []
    for i in range(0, len(signature), r):
        subvecs.append(signature[i: i+r])
    return subvecs

def probability(s, r, b):
    return 1-(1 - s**r)**b

#jaccard similarity
def jaccard(a: set, b:set):
    return len(a.intersection(b)) / len(a.union(b))

a_sig = create_hash(a_1hot)
b_sig = create_hash(b_1hot)
c_sig = create_hash(c_1hot)
d_sig = create_hash(d_1hot)
e_sig = create_hash(e_1hot)

print('Signature of a: ',a_sig)
print('Signature of b: ',b_sig)
print('Signature of c: ',c_sig)
print('Signature of d: ',d_sig)
print('Signature of e: ',e_sig)

band_a = split_vector(a_sig, 10)
band_b = split_vector(b_sig,10)
band_c = split_vector(c_sig, 10)
band_d = split_vector(d_sig, 10)
band_e = split_vector(e_sig, 10)

for a_rows, b_rows in zip(band_a, band_b):
    if a_rows == b_rows:
        print(f"Candidate pair: {a_rows} == {b_rows}")
        break
for a_rows, c_rows in zip(band_a, band_c):
    if a_rows == c_rows:
        print(f"Candidate pair: {a_rows} == {c_rows}")
        break
for a_rows, d_rows in zip(band_a, band_d):
    if a_rows == d_rows:
        print(f"Candidate pair: {a_rows} == {d_rows}")
        break
for a_rows, e_rows in zip(band_a, band_e):
    if a_rows == e_rows:
        print(f"Candidate pair: {a_rows} == {e_rows}")
        break
for b_rows, c_rows in zip(band_b, band_c):
    if b_rows == c_rows:
        print(f"Candidate pair: {b_rows} == {c_rows}")
        break
for b_rows, d_rows in zip(band_b, band_d):
    if b_rows == d_rows:
        print(f"Candidate pair: {b_rows} == {d_rows}")
        break
for b_rows, e_rows in zip(band_b, band_e):
    if b_rows == e_rows:
        print(f"Candidate pair: {b_rows} == {e_rows}")
        break
for c_rows, d_rows in zip(band_c, band_d):
    if c_rows == d_rows:
        print(f"Candidate pair: {c_rows} == {d_rows}")
        break
for c_rows, e_rows in zip(band_c, band_e):
    if c_rows == e_rows:
        print(f"Candidate pair: {c_rows} == {e_rows}")
        break
for d_rows, e_rows in zip(band_d, band_e):
    if d_rows == e_rows:
        print(f"Candidate pair: {d_rows} == {e_rows}")
        break

print('Signature Similarity:')
print(jaccard(a,b), jaccard(set(a_sig), set(b_sig)))
print(jaccard(a,c), jaccard(set(a_sig), set(c_sig)))
print(jaccard(a,d), jaccard(set(a_sig), set(d_sig)))
print(jaccard(a,e), jaccard(set(a_sig), set(e_sig)))
print(jaccard(b,c), jaccard(set(b_sig), set(c_sig)))
print(jaccard(b,d), jaccard(set(b_sig), set(d_sig)))
print(jaccard(b,e), jaccard(set(b_sig), set(e_sig)))
print(jaccard(c,d), jaccard(set(c_sig), set(d_sig)))
print(jaccard(c,e), jaccard(set(c_sig), set(e_sig)))
print(jaccard(d,e), jaccard(set(d_sig), set(e_sig)))

