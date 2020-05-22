import itertools
# Initialise array based on the failure function:
def init_arr(w):
    m = len(w)
    i = 0
    j = 1

    # No proper prefix for string of length 1:
    global arr
    arr[0] = 0

    while j < m:
        if w[i] == w[j]:
            i += 1
            arr[j] = i
            j += 1

        # The first character didn't match:
        elif i == 0:
            arr[j] = 0
            j += 1

        # Mismatch after at least one matching character:
        else:
            i = arr[i - 1]


def kmp_search(w, s):
    # Initialise array:
    init_arr(w)

    # Initialising variables:
    i = 0
    j = 0
    m = len(w)
    n = len(s)

    # Start search:
    while i < m and j < n:
        # Last character matches -> Substring found:
        if w[i] == s[j] and i == m - 1:
            return True

        # Character matches:
        elif w[i] == s[j]:
            i += 1
            j += 1

        # Character didn't match -> Backtrack:
        else:
            i = arr[i - 1]
            if i == 0:
                j += 1

    # Substring not found:
    return False

def kmp_search(file1,file2):
    i=0
    for line in file1 & file2:
        if line:
            print(line)
            i=1
    if(i==1): return True
    elif(i == 0): return False
def listToString(s):

	str1 = ""
	for ele in s:
		str1 += ele
	return str1

def kmp_compare(f1,f2):
    print()
    print("----- KMP Analysis of "+f1+" & "+f2+" -----")
    print()
    print("Common Lines Identified:")

    file1 = set(line.strip() for line in open(f1))
    file2 = set(line.strip() for line in open(f2))
    if(not (kmp_search(file1,file2))): print("None Found")

    line1=[line.rstrip('\n') for line in open(f1)]
    linelist2 = [line.rstrip('\n') for line in open(f2)]
    line1=listToString(line1)

    for a in line1:
        if (a==''): line1.remove(a)

    linelist2 = [line.rstrip('\n') for line in open(f1)]

    # create array:
    arr = [None] * len(line1)



    # create array:
    arr = [None] * len(line1)
    print()
    print()
    print()
