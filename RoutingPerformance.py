#!/usr/bin/python3
# COMP9331 Assignment2 RoutingPerformance
# z5092923 Wang Jintao
# z5104857 Shi Xiaoyun

# network type values: CIRCUIT or PACKET
NETWORK_SCHEME = "CIRCUIT"
# routing scheme values: Shortest Hop Path (SHP), Shortest Delay Path (SDP) and Least Loaded Path (LLP)
ROUTING_SCHEME = "SHP"
# a file contains the network topology specification
TOPOLOGY_FILE = "topology.txt"
# a file contains the virtual connection requests in the network
WORKLOAD_FILE = "workload.txt"
# a positive integer value which show the number of packets per second which will be sent in each virtual connection.
PACKET_RATE = 2

# Graph
class Graph:
	# create a new graph
	# O(V^2)
	def __init__(self,V = 26):
		self.edges = [[0 for x in range(V)] for y in range(V)]
		self.nV = V
		self.nE = 0
	
	# vertices v and w , delay d, link capacities c, status s
	# O(1)
	def insertEdge(self,v,w,d,c,s = True):
		v = ord(v) - 65
		w = ord(w) - 65
		d = int(d)
		c = int(c)
		if self.edges[v][w] == 0:
			self.edges[v][w] = [d,c,s];
			self.edges[w][v] = [d,c,s];
			self.nE += 1;
	
	# return whether exist edge between two vertices
	# O(1)
	def adjacent(self,v,w):
		v = ord(v) - 65
		w = ord(w) - 65
		return (self.edges[v][w] != 0)
	
	# print edges in graph
	# O(nV^2)
	def showGraph(self):
		if self.nE == 0:
			print("nE = 0, No graph\n")
		else:
			print("nV: {}; nE: {}".format(self.nV,self.nE))
			for i in range(self.nV):
				for j in range(i+1,self.nV):
					if self.edges[i][j] != 0:
						print("{},{},{}".format(chr(i+65),chr(j+65),self.edges[i][j]))

def SHP():
	pass

def SDP():
	pass
	
def LLP():
	pass

def doRequest():
	print("do request")
	
def main():
	
	# open and read TOPOLOGY_FILE
	with open(TOPOLOGY_FILE) as f:
		routers = [line.strip().split(" ") for line in f]

	# open and reand WORKLOAD_FILE
	with open(WORKLOAD_FILE) as f:
		requests = [line.strip().split(" ") for line in f]
		
	graph = Graph()
	for router in routers:
		graph.insertEdge(router[0], router[1], router[2], router[3])

	for request in requests:
		doRequest()
	

if __name__ == "__main__":
	main()