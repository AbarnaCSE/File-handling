f = open("file.txt","w")
f.write("Welcome to guvi")
f.close()
f = open("file.txt","r")
print(f.read())
f.close()
