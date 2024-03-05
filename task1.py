a = "flying fish flew by the space station"
b = "he will not allow you to bring your sticks of dynamite and pet armadillo along"
c = "he figured a few sticks of dynamite youre easier than a fishing pole to catch an armadillo"

k = 2
def shingle(text: str, k: int):
    shingle_set = []
    for i in range (len(text) - k+1):
        shingle_set.append(text[i:i+k])
    return set(shingle_set)

a = shingle(a, k)
b = shingle(b, k)
c = shingle(c, k)
print('Shingles of a: ',a)
print('Shingles of b: ',b)
print('Shingles of c: ',c)

union = a.union(b,c)
print('Shingle vocabulary: ',union)