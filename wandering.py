from random import randrange
import requests
import re
import json
import networkx as nx
import numpy as np
import queue
import sqlite3

def getFriends(idx):
    answer = requests.get("https://api.vk.com/method/friends.get?user_id=" + idx)
    if answer.status_code != 200:
        return []
    decoded = json.loads(answer.text)
    if "response" not in decoded:
        return []
    return [str(x) for x in decoded["response"]]

heap = queue.LifoQueue()
G = nx.Graph()
heap.put(str(39575636))
count = 20 # глубина блужданий
nodesDone = set() # пройденные вершины

vertexes = [] # вершины

while count > 0:
    node = heap.get()
    if nodesDone.__contains__(node):
        print("cycle")
        break
    friends = getFriends(node)
    if len(friends) > 0:
        k = 0
        vertexes.extend(friends)
        while (k < len(friends)):
            number = randrange(len(friends))
            n = friends.pop(number)
            if (len(getFriends(n))>0):
                heap.put(n)
                break
            k = k + 1
    if heap.empty():
        break
    count = count - 1
    nodesDone.add(node)
print(len(vertexes))

G.add_nodes_from(vertexes)

nx.write_adjlist(G, "20deep")
