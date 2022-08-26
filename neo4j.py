from xml.dom.minidom import TypeInfo
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

# Update:
def updateEmployee(id, firstName, lastName, hiredYear):
    graph.run("match (p:People {id:\"%s\"}) set p.firstName = \"%s\" set p.lastName = \"%s\" set p.hiredYear = \"%s\" RETURN (p)"
    %(id, firstName, lastName, hiredYear))
    print("Person of ID: " + str(id) + " updated!")

# Delete:
def deleteEmployee(id):
    graph.run('MATCH(p:People {id:"' + str(id) + '"})delete p')
    print("node " + str(id) + " deleted ")

# Joins / Match
def findWhoReportsToEmployee(id):
    relationshipMatcher = RelationshipMatcher(graph)
    result = relationshipMatcher.match(nodes=[findEmployee(str(id))], r_type="BOSS_OF").all()
    print(result)

# Indexing
def indexByFirstName():
    graph.run('CREATE INDEX FOR (p:People) ON (p.firstName)')
    print("successfully indexed")

def showIndexTables():
    tables = graph.run('CALL db.indexes')
    print(tables)

def aggregateWithAverage():
    result = graph.run('MATCH (p:People) RETURN avg(toInteger(p.hiredYear))')
    print(result)

# Create relationship between two nodes
def createRelationship(empID1, relationship,empID2):
    emp1 = graph.nodes.match("People", id=empID1).first()
    emp2 = graph.nodes.match("People", id=empID2).first()
    emp1_BOSS_OF_emp2 = Relationship(emp1, relationship, emp2)
    graph.create(emp1_BOSS_OF_emp2)

# CALL db.indexes

# createEmployee("10002", "Zoward", "Woward", "1998")

# deleteEmployee(10001)

# findWhoReportsToEmployee(666)

# indexByFirstName()

# showIndexTables()

# createDatabase()

# aggregateWithAverage()

# createRelationship("10002", "BOSS_OF", "10001")
