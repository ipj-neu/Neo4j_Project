from py2neo import *

graph = Graph(password="mypassword")

#example code
# results = graph.run("match (p:People) return p limit 50")
# for node in results.data():
#     print(node['p'].get('firstName'))

# More example code:
# Create:
def createEmployee():
    query = "CREATE (a:Employee {}), {}"
    results = graph.run(query)
    print("createEmployee Results -> " + results)

# Read:

# Update:

# Delete: