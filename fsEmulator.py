import sys
from termcolor import colored


class Folder:
    def __init__(self, parent, name):
        ''':parent is parent directory
           :name is directory name'''
        self.parent = parent
        self.name = name
        self.folder = []    #directory list 
        self.file = []      #file list


root = Folder(parent = None, name = 'home')
cur = root
path = 'root'


#Create a file
def touch(name):
    
    global cur

    if name in cur.file: #Check if the name of file already exists
        return print(colored(f'Error:file "{name}" exists', 'red'))
    cur.file.append(name)
    return ''

#Delete file
def rm(name):

    global cur

    if name in cur.file:
        cur.file.remove(name)
        return ''
    return print(colored(f'Error:"{name}" No such file', 'red'))

#Create a directory
def mkdir(name):
    
    global cur, path

    for i in cur.folder: #Check if the name of directory already exists
        if name == i.name:
            return print(colored(f'Error:directory "{name}" exists', 'red'))
    directory = Folder(parent = cur, name = name)
    cur.folder.append(directory)
    return ''


#Delete directory
def rmdir(name):

    global cur, path

    #directory = Folder(parent = cur, name = name)
    #if len(directory) > 0:
        #print('Error')
    if len(cur.folder) < 1:
        print(colored(f'Error:"{name}" No such directory', 'red'))
    for i in cur.folder:
        if name == i.name:
            if len(i.folder) > 0:
                return  print(colored(f'Error:directory "{name}" is not empty: try "rm -r"', 'red'))
            cur.folder.remove(i)
            return ''
        
    return print(colored(f'Error:"{name}" No such directory', 'red'))



#Delete directory recursively
def rm_r(name):

    global cur, path

    if len(cur.folder) < 1:
        print(colored(f'Error:"{name}" No such directory', 'red'))
    for i in cur.folder:

        if name == i.name:
            cur.folder.remove(i)
            return ''






#Change the current directory 
error = 0

def cd(name):                                        

    global cur, path, error 
    
    if name == '..':
        if cur.parent != None:
            path = path[:(len(path) - len(cur.name)) - 1]
            cur = cur.parent

    else:
        for i in cur.folder:
            if i.name == name:
                cur = i 
                path = path + '/' + name
                return path
        cur = root
        path = 'root'
        error = 1
        return print(colored('Error: No such directory', 'red'))

def cd_path(name):
    global error

    name = name.split('/')
    for i in name:
        if error:
            break
        cd(i)





#List all files and directories
def ls():
    
    global cur

    for i in cur.file:
        print(i, end = ' ')

    for i in cur.folder:
        print(colored(i.name, 'blue'), end = ' ' )
    print()



        

#Main method to run the program
if __name__ == '__main__':
    while True:
        print(path,end = ':$ ')
        command = input().split(' ')

 #Create a file 
        if command[0] == 'touch':
            if len(command) < 2 or command[1] == '':
                print(colored('"touch":missing operand', 'red'))
            for i in range(1, len(command)):
                try:
                    touch(command[i])
                except:
                    print('Command error')

#Delete file recursively
        elif command[0] == 'rm' and command[1] == '-r':
            if len(command) < 3 or command[2] == '':
                print(colored('"rm -r":missing operand', 'red'))
            try:
                rm_r(command[2])

            except:
                print("Command error")

#Delete file
        elif command[0] == 'rm':
            if len(command) < 2 or command[1] == '':
                print(colored('"rm":missing operand', 'red'))
            for i in range(1, len(command)):
                try:
                    rm(command[i])
                except:
                    print('Command error')
                           
#Create a directory
        elif command[0] == 'mkdir':
            if len(command) < 2 or command[1] == '':
                print(colored('"mkdir":missing operand', 'red'))
            for i in range(1, len(command)):
                try:
                    mkdir(command[i])
                except:
                    print('Command error') 
                    
#Delete directory
        elif command[0] =='rmdir':
            if len(command) < 2 or command[1] == '':
                print(colored('"rmdir":missing operand', 'red'))
            for i in range(1, len(command)):
                try:
                    rmdir(command[i])
                except:
                    print('Command error') 
    
#Change directory
        elif command[0] == 'cd':
            if command[1] == '':
                print(colored('"cd":missing operand', 'red'))
            else:
                try:
                    cd_path(command[1])
                except:
                    print(colored('"cd":missing operand', 'red'))
                
#Print working directory
        elif command[0] == 'pwd':
            pwd = path
            if len(pwd) > 1:
                pwd = pwd.split('/')
                pwd = '/'.join(pwd[1:])
                print(colored('/' + pwd, 'green'))
             
            else:
                print(colored(path,'green')) 
                
#List all the content
        elif command[0] == 'ls':
            ls()

#List all hidden contet                 #NOT FINISHED YET
       # elif command[0] == 'ls -a':
            #ls()
            #print('.')
            #print('..')

#Long list format                       #NOT FINISHED YET
       #elif command[0] == 'ls -l"



#Close the program
        elif command[0] == 'exit':
            sys.exit(colored('File System Closed\n"""Best Regarts"""', 'green'))
        
#Continue
        elif command[0] == '':
            continue

        else:
            print(colored('Error:No such command', 'red'))





























































