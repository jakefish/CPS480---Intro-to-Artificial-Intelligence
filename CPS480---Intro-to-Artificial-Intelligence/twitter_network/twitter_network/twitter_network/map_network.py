import networkx as net
import matplotlib.pyplot as plt

from collections import defaultdict
import math

twitter_network = [ line.strip().split('\t') for line in file('twitter_network.csv') ]

o = net.DiGraph()
hfollowers = defaultdict(lambda: 0)
for (twitter_user, followed_by, followers) in twitter_network:
    o.add_edge(twitter_user, followed_by, followers=int(followers))
    hfollowers[twitter_user] = int(followers)

ROOT = 'PlayStation'

# centre around the ROOT node and set radius of graph
g = net.DiGraph(net.ego_graph(o, ROOT, radius=4))

def trim_degrees_ted(g, degree=1, ted_degree=1):
    g2 = g.copy()
    d = net.degree(g2)
    for n in g2.nodes():
        if n == ROOT: continue # don't prune the ROOT node
        if d[n] <= degree and not n.lower().startswith('play'):
            g2.remove_node(n)
        elif n.lower().startswith('play') and d[n] <= ted_degree:
            g2.remove_node(n)
    return g2

def trim_edges_ted(g, weight=1, ted_weight=10):
    g2 = net.DiGraph()
    for f, to, edata in g.edges_iter(data=True):
        if f == ROOT or to == ROOT: # keep edges that link to the ROOT node
            g2.add_edge(f, to, edata)
        elif f.lower().startswith('play') or to.lower().startswith('play'):
            if edata['followers'] >= ted_weight:
                g2.add_edge(f, to, edata)
        elif edata['followers'] >= weight:
            g2.add_edge(f, to, edata)
    return g2

print 'g: ', len(g)
core = trim_degrees_ted(g, degree=235, ted_degree=1)
print 'core after node pruning: ', len(core)
core = trim_edges_ted(core, weight=250000, ted_weight=35000)
print 'core after edge pruning: ', len(core)

nodeset_types = { 'Play': lambda s: s.lower().startswith('play'), 'Not Play': lambda s: not s.lower().startswith('play') }

nodesets = defaultdict(list)

for nodeset_typename, nodeset_test in nodeset_types.iteritems():
    nodesets[nodeset_typename] = [ n for n in core.nodes_iter() if nodeset_test(n) ]

pos = net.spring_layout(core) # compute layout

colours = ['red','green']
colourmap = {}

plt.figure(figsize=(18,18))
plt.axis('off')

# draw nodes
i = 0
alphas = {'Play': 0.6, 'Not Play': 0.4}
for k in nodesets.keys():
    print "DRAWING NODES"
    ns = [ math.log10(hfollowers[n]+1) * 80 for n in nodesets[k] ]
    print k, len(ns)
    net.draw_networkx_nodes(core, pos, nodelist=nodesets[k], node_size=ns, node_color=colours[i], alpha=alphas[k])
    colourmap[k] = colours[i]
    i += 1
print 'colourmap: ', colourmap

# draw edges
net.draw_networkx_edges(core, pos, width=0.5, alpha=0.5)

# draw labels
alphas = { 'Play': 1.0, 'Not Play': 0.5}
for k in nodesets.keys():
    for n in nodesets[k]:
        x, y = pos[n]
        plt.text(x, y+0.02, s=n, alpha=alphas[k], horizontalalignment='center', fontsize=9)
