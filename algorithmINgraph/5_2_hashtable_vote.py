votedic = {}
def checkvote(name):
    if votedic.get(name):
        print('kick him out!')

    else:
        votedic[name] = True
        print('let hin vote!')


checkvote('mike1')
checkvote('mike2')
checkvote('mike1')
checkvote('mike2')

#to avoid collision, hash table needs two notes:  the first is to lower the index(it needs to be smaller than 1,
# and when the index is bigger than 0.7, the range of table should become bigger
# ) in table
# and the second is to design a beautiful function
#the function can make data in table seperate in average