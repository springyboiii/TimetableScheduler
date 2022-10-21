import csv
input=open("test-input-1.csv")
file=csv.reader(input)
rows = []
for row in file:
    rows.append(row)
rooms=rows.pop(-1)
subjects_timeslots={}
subjects_optional={}

for row in rows:
    row=[element.strip() for element in row]
    subjects_timeslots[row[0]]=row[2:]
    subjects_optional[row[0]]=True if row[1]=="o" else False
# print(subjects_optional)

def getCompulsorySubs(subjects_timeslots,dict=subjects_optional):
    compulsorySubs_timeslots={}
    for key in dict:
         if dict[key]==False:
             compulsorySubs_timeslots[key]=subjects_timeslots[key]

    
    return compulsorySubs_timeslots
compulsorySubs_timeslots=  getCompulsorySubs(subjects_timeslots)
print(compulsorySubs_timeslots)
def removeCompulsorySubsTimeslotsIntersection(compulsorySubs_timeslots):
    intersection={}
    for sub1 in compulsorySubs_timeslots:
        timeslots1=compulsorySubs_timeslots[sub1]
        for sub2 in compulsorySubs_timeslots:
            if sub1==sub2:
                continue
            timeslots2=compulsorySubs_timeslots[sub2]
            for timeslot in timeslots1:
                if timeslot in timeslots2 or timeslot in intersection:
                    # print(timeslot)
                    if timeslot not in intersection:
                        intersection[timeslot]=[sub1,sub2]
                    # timeslots1.remove(timeslot)
                    # compulsorySubs_timeslots[sub1]=timeslots1
                    # if timeslot in timeslots2:
                    #     timeslots2.remove(timeslot)
    # return compulsorySubs_timeslots
    return intersection
# removeCompulsorySubsTimeslotsIntersection(compulsorySubs_timeslots)
# print(list(compulsorySubs_timeslots.values()))
intersection=removeCompulsorySubsTimeslotsIntersection(compulsorySubs_timeslots)
# print(intersection)
# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')