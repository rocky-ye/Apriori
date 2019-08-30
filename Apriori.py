import sys, time

#  Implementation of Apriori Algorithm in python

# this function takes in data and minSupport and returns a frequent set with support
def apriori(data, support):
    finalSet = {}
    # find 1 and 2 frequent set and add to final set
    singleSet = getSingleFS(data,support)
    frequentSet = getTwoFS(data,support)
    finalSet.update(singleSet)
    finalSet.update(frequentSet)
    # find 3+ frequent set and add to the final set
    for i in range(len(singleSet)):
        candidateSet = getCandidateSet(frequentSet)
        frequentSet = getFrequentSet(candidateSet, data, support)
        finalSet.update(frequentSet)
        if len(frequentSet) == 0:
            break
    return finalSet

# this function takes in data and minSupport and returns the 1 frequent set
def getSingleFS(data, support):
    singleCs = {} # generate 1 candidate set
    for i in data:
        for j in i:
            if j in singleCs:
                singleCs[j] += 1
            else:
                singleCs[j] = 1
    # return 1 frequent set
    return {a:b for a,b in singleCs.items() if b >= support}

# this function takes in data and minSupport and returns the 2 frequent set
def getTwoFS(data, support):
    cs = {}
    for i in data:
        for j in range(len(i)):
            for k in range(j+1, len(i)):
                # create every possible 2 combinations
                s = '%s %s' % (i[j], i[k])
                if s in cs:
                    cs[s] += 1
                else:
                    cs[s] = 1
    return {k:v for k, v in cs.items() if v >= support}

# this function takes in the n-1 frequent set and returns the n candidate set
def getCandidateSet(fs):
    fs = list(fs.keys())
    cs = set()
    numOfLines = len(fs)
    for i in range(numOfLines):
        for j in range(i+1, numOfLines):
            # select two integer lists
            l1 = fs[i].split()
            l2 = fs[j].split()
            # add the string representation to the k candidate set if joinbable
            if joinPrune(l1,l2,fs):
                l1 = list(map(str, sorted(list(map(int, l1)))))  # sort l1
                cs.add(' '.join(l1))
    return cs

# this function takes in two lists and data returns true if two lists are able to join after pruning
def joinPrune(l1,l2,fs):
    n = len(l1)
    # return false if two lists are not joinable
    for k in range(n - 1):
        if l1[k] != l2[k]:
            return False
    # prune the list
    l1.append(l2[-1])
    l1 = list(map(str, sorted(list(map(int, l1))))) # sort l1
    for i in range(n-1):
        subL = l1[:i] + l1[i+1:]
        if ' '.join(subL) not in fs:
            return False
    return True

# this function takes in the n candidate set and data and returns the n frequent set
def getFrequentSet(cs, data, support):
    fs = {}
    for itemSet in cs:
        freq = 0
        for transaction in data:
            # print(transaction)
            if set(itemSet.split()).issubset(set(transaction)):
                freq += 1
        if freq >= support:
            fs[itemSet] = freq
    return fs


# unpacking command line input
inputFileN = sys.argv[1]
support = int(sys.argv[2])
outputFileN = sys.argv[3]

inputFile = open(inputFileN)
content = inputFile.readlines()
# create a list of lists of integers of transactions
data = [line.split() for line in content]

startTime = time.time()
print('running...')
finalSet = apriori(data,support)

# print well-formated output in a file
outputFile = open(outputFileN, 'w')
(', '.join(content))
finalList = []
for k,v in finalSet.items():
    l = [x for x in map(int, k.split())]
    l.append(0)
    l.append(v)
    finalList.append(l)
finalList.sort()
for itemSet in finalList:
    del itemSet[-2]
    s = ' '.join(map(str, itemSet[:len(itemSet) - 1])) + ' (' + str(itemSet[-1]) + ')' + '\n'
    outputFile.write(s)
outputFile.close()
totalTime = round(time.time() - startTime, 2)
print('Done: Total Time: ', totalTime, ' seconds')

