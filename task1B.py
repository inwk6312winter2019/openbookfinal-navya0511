file1= open('Book1.txt','r')
file2= open('Book2.txt','r')
file3= open('Book3.txt','r')

def common_words():
    hist1=dict()
    hist2=dict()
    hist3=dict()
    hist_common=dict()
    result=[] 
    for line in file1:
        line=line.lower()
        line=line.strip()
        line=line.split()
        for word in line:
            if word not in hist1:
                hist1[word]=1
            else:
                hist1[word]+=1

    for line in file2:
        line=line.lower()
        line=line.strip()
        line=line.split()
        for word in line:
            if word not in hist2:
                hist2[word]=1
            else:
                hist2[word]+=1

    for line in file3:
        line=line.lower()
        line=line.strip()
        line=line.split()
        for word in line:
            if word not in hist3:
                hist3[word]=1
            else:
                hist3[word]+=1

    for word in hist1:
        if word in hist2 and word in hist3:

            hist_common[word]=hist_common.get(word, 0) + 1

    lst = [(value,key)for key,value in hist_common.items()]
    lst.sort(reverse=True)
    only_20 = lst[:20]
    common_20 = dict(only_20)

    return common_20



            hist_common[word] += 1

    print(hist_common)
 
common_words()
