def restoreString(s, indices):
    abc = [None] * len(s)
    for i in range(len(indices)):
        abc[indices[i]] = s[i]
    return ''.join(map(str, abc))

if __name__ == "__main__":
    s = "codeleet"
    indices = [4,5,6,7,0,1,2,3]
    print(restoreString(s, indices))