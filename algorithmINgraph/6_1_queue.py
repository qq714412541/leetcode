graph = {}
graph['you'] = ['aa','bb','cc']
graph['bb'] = ['aj','pegy']
graph['aa'] = ['pegy','you']
graph['aj'] = []
graph['pegy'] = ['m']
graph['thom'] = []
graph['jonny'] = []
graph['cc'] = ['jonny']

from collections import deque
#import queue
searchqueue = deque()
searchqueue += graph['you']




def person_is_seller(person):
    return person[-1] == 'm'


def lookfor_seller(searchqueue):
    searched = []
    while searchqueue:
        person = searchqueue.popleft()
        if person not in searched:
            if person_is_seller(person):

              print(person + 'is a seller')
              print(searched)
              return True

            else:
                searchqueue += graph[person]
                searched.append(person)
    return False


print(lookfor_seller(searchqueue))
#this code:  if person not in searched:  if it is not added, the array called searched may have same element in it. Because the hashtable can have
#same reflection to get the same result in somesearch. And it may cause high time complexty?(Does this procedure of
# check element cause high complextity?)
