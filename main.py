f = open("file.txt","a")
f.write("xyz")
f.close()

f = open("file.txt","r")
print(f.read())