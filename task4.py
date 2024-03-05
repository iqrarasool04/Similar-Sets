import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from random import shuffle

# a = "hello, my name is Iqra"
# b = "i am a 3rd year BSCS student"
# c = "i like this subject"
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

def split_vector(signature,b):
    assert len(signature) % b == 0
    r = int(len(signature) / b)
    subvecs = []
    for i in range(0, len(signature), r):
        subvecs.append(signature[i: i+r])
    return subvecs

def probability(s, r, b):
    return 1-(1 - s**r)**b
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

band_a = split_vector(a_sig, 10)
band_b = split_vector(b_sig,10)
band_c = split_vector(c_sig, 10)
print(band_a)
print(band_b)
print(band_c)

for b_rows, c_rows in zip(band_b, band_c):
    if b_rows == c_rows:
        print(f"Candidate pair: {b_rows} == {c_rows}")
        break

for a_rows, b_rows in zip(band_a, band_b):
    if a_rows == b_rows:
        print(f"Candidate pair: {a_rows} == {b_rows}")
        break

for a_rows, c_rows in zip(band_a, band_c):
    if a_rows == c_rows:
        print(f"Candidate pair: {a_rows} == {c_rows}")
        break

results = pd.DataFrame({
    's': [],
    'P': [],
    'r,b': []
})

for s in np.arange(0.01,1,0.01):
    total = 100
    for b in [100,50,25,20,10,5,4,2,1]:
        r=int(total/b)
        p=probability(s,r,b)
        # results = results.append({
        #     's': s,
        #     'P': P,
        #     'r,b': f"{r},{b}"
        # }, ignore_index=True)
        results.loc[len(results)] = [s, p, f"{r},{b}"]

sns.lineplot(data=results, x='s', y='P', hue='r,b')
plt.show()