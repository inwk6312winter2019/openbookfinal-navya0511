f1= open(r"access.log",'r')
ge=open(r"get.log",'w')
po=open(r"post.log",'w')
pu=open(r"put.log",'w')
de=open(r"delete.log",'w')
for line in f1:
 if "GET" in line:
    ge.write(line)
 elif "POST" in line:
    po.write(line)
 elif "PUT" in line:
    pu.write(line)
 elif "DELETE" in line:
    de.write(line)
