f = open('index (2).html', 'r')

doc = f.readlines()

f.close()

for line in doc:
    if 'pwd' in line:
        password = line.split('"')
        if (len(password) > 1):
            print(password[1])
