from py2neo import *

graph = Graph(password="mypassword")

#example code
# results = graph.run("match (p:People) return p limit 50")
# for node in results.data():
#     print(node['p'].get('firstName'))

# More example code:
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

# Update:

# Delete:

createEmployee("1", "Howard", "howard", "0")