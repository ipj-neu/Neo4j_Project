from py2neo import *

graph = Graph(password="mypassword")

#example code
# results = graph.run("match (p:People) return p limit 50")
# for node in results.data():
#     print(node['p'].get('firstName'))

#1
# node50 = graph.nodes.match(id = "50").first()
# print(node50)
# boss50 = graph.match(nodes=[node50], r_type="BOSS_OF").count()
# print(boss50)

#2
# node666 = graph.nodes.match(id = "666").first()
# print(node666)
# boss666 = graph.match(nodes=[node666], r_type="BOSS_OF").count()
# print(boss666)

