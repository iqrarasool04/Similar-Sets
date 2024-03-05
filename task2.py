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

vocab = list(a.union(b).union(c))
print('Shingle vocabulary: ',vocab)

a_1hot = [1 if x in a else 0 for x in vocab]
b_1hot = [1 if x in b else 0 for x in vocab]
c_1hot = [1 if x in c else 0 for x in vocab]
print(a_1hot)