from winreg import QueryInfoKey
from py2neo import *

graph = Graph(password="mypassword")

#example code
# results = graph.run("match (p:People) return p limit 50")
# for node in results.data():
#     print(node['p'].get('firstName'))

# More example code:
# Create:
def createEmployee(id, firstName, lastName, hireYear):
    # Uses 'Node' to create a...node
    query = Node("People", id = id, firstName = firstName, lastName = lastName, hireYear = hireYear)
    graph.create(query)

# Read:
def findEmployee(id):
    return graph.nodes.match("People", id=id).first()

# Update: (Work in progress)
def updateEmployee(identity, id, firstName, lastName, hireYear):
    query = Node("People", identity = identity, id = id, firstName = firstName, lastName = lastName, hireYear = hireYear)
    graph.merge(query)

# Delete:

# createEmployee("1", "Howard", "howard", "0")
# (Work in progress)
# updateEmployee("10001", "1", "Boward", "boward", "3")