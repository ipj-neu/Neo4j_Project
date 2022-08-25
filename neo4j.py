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
def createEmployee(id, firstName, lastName, hireYear):
    try:
        # Uses 'Node' to create a...node
        query = Node("People", id = id, firstName = firstName, lastName = lastName, hireYear = hireYear)
        results = graph.create(query)
        print("createEmployee Results -> " + results)
    except:
        print("Something went wrong! -> createEmployee")

# Read:
def findEmployee(id):
    return graph.nodes.match("People", id=id).first()

# Update:

# Delete:

# createEmployee("1", "Howard", "howard", "0")
# createDatabase()