file1= open('Book1.txt','r')
file1=file1.readlines()

def unique_words(file):
  result=[]
  for line in file:
    line=line.strip()
    line=line.split()
    for word in line:
      if word not in result:
        result.append(word)
  print(result)

unique_words(file1)
