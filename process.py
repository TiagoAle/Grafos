
import graphviz as gv

dot = gv.Graph(format='png')

dot.node('A')
dot.node('B')
dot.node('C')
dot.node('D')
dot.node('E')

dot.edge('A', 'B')
dot.edge('A', 'C')
dot.edge('A', 'E')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('C', 'E')
dot.edge('D', 'E')

print(dot.source)

filename = dot.render(filename='img/g1')
print(filename)
