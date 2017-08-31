def generateDictionary(arq):
    lines = arq.split('\n')
    dictionary = {}
    for i in lines :
        if (len(i) != 0) :
            if (i[0] != ';'):
                arr =  i.split(' ')
                dictionary[(arr[0],arr[1])] = [arr[4],arr[2],arr[3]]
    return dictionary
