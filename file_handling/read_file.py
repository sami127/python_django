
# f = open("test.txt")  # Read the file
# r = open('/home/sami/Desktop/test.txt')

# mode = 'r','w', 'r+b'
# encode = 'utf-8'

# f = None
# try:
#     f = open("/home/sami/Desktop/my-learning/sami127/python_django/file_handling/test.txt", mode='w')
#     f.write("This is my first file full path \n")
#     f.write("This is my second line 343534\n")
# except:
#     print("we got exception")
# finally:
#     print("I am inside finally")
#     f.close()

# with open('with.txt',mode='w',encoding='utf-8') as f:
#     f.write("my with file \n")
#     f.write("this is second file \n\n")
#     f.write("third line \n")    


f = open('test.txt','r')
m = f.read()
print(m)