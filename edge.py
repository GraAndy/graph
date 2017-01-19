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

conn = sqlite3.connect("me.db")

G = nx.read_adjlist("20deep")

c = conn.cursor()


for n in nx.nodes(G):
    c.execute("INSERT INTO nodes VALUES (?)", [n])


nodes = list()
nodes.extend(nx.nodes(G))
k = 0
for node in nodes:
    friends = getFriends(node)
    for friend in friends:
        if nodes.__contains__(friend):
            c.execute("INSERT INTO edges VALUES (?, ?)", (node, friend))
    k = k + 1
    if 0 == k % 100:
        print(k)

conn.commit()
conn.close()

