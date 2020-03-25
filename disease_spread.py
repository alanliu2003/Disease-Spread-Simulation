# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:14:15 2020

@author: Alan Liu
"""
import networkx as nx
import matplotlib.pyplot as plt
import random
#number of people in society
numpeople=100
G=nx.watts_strogatz_graph(numpeople,6,1)
pos=nx.spring_layout(G)
for node in list(G):
    for neighbor in G.neighbors(node):
        G.add_weighted_edges_from([(node,neighbor,0.5)])
start_family=0
while numpeople-start_family>5:
    end_family=start_family+random.randint(0,5)
    for j in range (start_family,end_family):
        for k in range(j,end_family):
            G.add_weighted_edges_from([(j,k,10)])
    start_family=end_family+1

for i in range (start_family,numpeople):
    for k in range(i,end_family):
            G.add_weighted_edges_from([(i,k,10)])
infected=[]
infected.append(random.randint(0,numpeople))
death=0
days=0
state=""
while len(infected)>0 and len(infected)<numpeople:
    days+=1
    for people in list(G):
        if people in infected:
            if random.random()<0.01:
                infected.remove(people)
    for infected_node in infected:
        for connected in G.neighbors(infected_node):
            relation=G.get_edge_data(infected_node,connected).get('weight')
            if random.random()<0.05*relation and connected not in infected:
                infected.append(connected)
    for people in list(G):
        if people in infected:
            if random.random()<0.03:
                infected.remove(people)
                G.remove_node(people)
                death+=1
    nx.draw_networkx_nodes(G,pos,nodelist=infected,node_color='g',node_size=100)
    nx.draw_networkx_nodes(G,pos,nodelist=list(set(G.nodes)-set(infected)),node_color='r',node_size=100)
    nx.draw_networkx_edges(G,pos)
    fig=plt.gcf()
    fig.set_size_inches(13,10)
    plt.show()
    if len(infected) > 0.8*len(G.nodes):
        state="80% infected"
        break
print("death: "+str(death))
print("days: "+str(days))

