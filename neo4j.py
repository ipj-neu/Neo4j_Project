from py2neo import *

graph = Graph(password="mypassword")

def createDatabase():
    graph.run("load csv with headers from 'file:///people.csv' as row create (:People {id: row.id, firstName: row.firstName, lastName: row.lastName, hiredYear: row.hiredYear})")
    print("createDatabase -> Nodes created")
    createRelationships()
    print("createDatabase -> Done")

def createRelationships():
    graph.run("load csv with headers from 'file:///friendships.csv' as row match (p:People), (f:People) where p.id = row.pid and f.id = row.friendid create (p)-[r:FRIEND_OF]->(f)")
    print("createRelasionships -> Freindships created")
    graph.run("load csv with headers from 'file:///reportsTo.csv' as row match (p:People), (b:People) where p.id = row.pid and b.id = row.bossid create (b)-[r:BOSS_OF]->(p)")
    print("createRelasionships -> Bosses created")

# Create:
def createEmployee(id, firstName, lastName, hiredYear):
    # Uses 'Node' to create a...node
    query = Node("People", id = id, firstName = firstName, lastName = lastName, hiredYear = hiredYear)
    graph.create(query)

# Read:
def findEmployee(id):
    return graph.nodes.match("People", id=id).first()

# Update: (Work in progress)
def updateEmployee(id, firstName, lastName, hiredYear):
    graph.run("match (p:People {id:\"%s\"}) set p.firstName = \"%s\" set p.lastName = \"%s\" set p.hiredYear = \"%s\" RETURN (p)"
    %(id, firstName, lastName, hiredYear))
    print("Person of ID: " + str(id) + " updated!")


# Delete:
def deleteEmployee(id):
    graph.run('MATCH(p:People {id:"' + str(id) + '"})delete p')
    print("node " + str(id) + " deleted ")

# createEmployee("10002", "Howard", "Boward", "0000")
# findEmployee("10002")
# updateEmployee("10002", "Coward", "Doward", "1000")
# deleteEmployee(10001)