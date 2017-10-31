# fout = open("output.txt", "w")
# line1 = "How many roads must a man walk down\n"
# fout.write(line1)
# line2 = "Before you call him a man?\n"
# fout.write(line2)
# fout.close() 

# pattern = 'man'
# replace = 'woman'
# source = 'output.txt'
# dest = 'new_' + source

import os
cwd = os.getcwd()
#cwd stands for "currently working directory"
#print Cwd

# print(os.path.abspath("output.txt"))
# print(os.path.exists("output.txt"))

# print(os.listdir(cwd))


def walk(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
# walk(cwd)

def walk2(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))

# walk2(cwd)



# try:    
#     fin = open('bad_file')
# except:
#     print('Something went wrong.')

# print("now we are here")


import pickle
t1 = [1,2,3]
s = pickle.dumps(t1)
t2 = pickle.loads(s)
print(t2)

print(t2 == t1)
