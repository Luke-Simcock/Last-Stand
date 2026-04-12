###############################################################     READ


file = open("C:/TextFolders Data/AccountUsernames.txt", 'r')
read = file.readlines()
modified = []

for line in read:
    if line not in modified:
        modified.append(line.strip())

print(modified)
file.close()


################################################################    WRITE


file = open("C:/TextFolders Data/AccountPasswords.txt", 'w')

usernames = ['franky', 'steven', 'alisha', 'barney']
passwords = ['123456', 'passwo', 'undwoi', 'Jon8w@']

for i in range(0, 4):
    entry = usernames[i] + "-" + str(passwords[i])+'\n'
    file.write(entry)

file.close()


##################################################################    APPEND


file = open("C:/TextFolders Data/AccountPasswords.txt", 'a')

username = ['Adrian']
password = ['verysecure@indeed']


entry = username[0]+ "-" + str(password[0])+'\n'
file.write(entry)

file.close()