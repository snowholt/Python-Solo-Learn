file = open("filename.txt", "w")
msg = "Hi, this is a test!"
x = file.write(msg)
print(len(msg))
print(x)
file.close()
file = open("filename.txt", "r")
print(file.read())
file.close()
