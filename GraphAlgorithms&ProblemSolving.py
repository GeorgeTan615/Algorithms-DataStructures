"Student Name: George Tan Juan Sheng"
"Student ID: 30884128"

import math
def best_trades(prices:list, starting_liquid:int, max_trades:int, townspeople:list) -> int:
    """
    The function takes in prices, an array which is of length n, where prices[i] is the value of 1L of the liquid with 
    ID i, starting_liquid is the ID of the liquid you arrive with and this liquid is 1L, max_trades is the maximum number of trades
    you can conduct before you need to move on, townspeople is a list of non-empty lists and each interior list corresponds to the 
    trades offered by a particular person. The function then returns the maximum value that you can obtain after performing at most
    max_trades trades.

    Pre-cond: For each liquid, there will be at least one townsperson who is willing to trade for that liquid. Starting_liquid is the liquid
              which you will arrive with and its of 1L.
    Post-cond: Maximum value that can be obtained after performing at most max_trades trades.

    Time-complexity: Best and worst is O(TM), where T is the total number of trades available and M is the max_trades.
    Explanation: O(M*T + N) where N is the number of liquids
               : O(M(loop through max_trades)*T(loop through all trades available) + N(loop through all liquids to obtain and get maximum profit))
               : O(MT + N) , however N is bounded by T as every liquid there will be people willing to trade for it
               : O(TM)

    Auxiliary-space complexity:O(N), where N is the len(prices)/number of liquids 
    Explanation: We will be creating two extra lists, litres1 and litres2 which will be of size len(prices). Litres is used to store
                 optimal litres of that liquid.

    Space-complexity: O(T+N), where T is the number of trades available and N is the number of liquid.
                    : Input + Auxiliary
                    : O(T) + O(N)
                    : O(T+N)
    """
    litres1 = [0] * len(prices)
    litres2 = [0] * len(prices)
    litres1[starting_liquid]=1          #initialise starting_liquid to 1 litre
    litres2[starting_liquid]=1          #initialise starting_liquid to 1 litre

    for j in range(max_trades):
        for trades in townspeople:
            for trade in trades:
                u,v,w = trade 
                if litres1[u]*w > litres2[v]:
                    litres2[v] = litres1[u]*w
        litres1,litres2 = litres2,litres1
    
    maximum_profit = -1

    for l in range(len(litres1)):
        if litres1[l]*prices[l] > maximum_profit:
            maximum_profit = litres1[l]*prices[l]
    return round(maximum_profit)

class MinHeap:
    """
    This is a MinHeap class and implements MinHeap methods and also some additional methods like
    swap_indx which updates the position of the vertexces in the indx list. The MinHeap class also stores
    objects of Vertex type in the heap.
    """
    def __init__(self, vertex_arr:list) -> None:
        """
        This is the __init__ function for the MinHeap class. The function takes in a list of 
        vertices which will be inserted into our MinHeap. The function creates and initialises a the_array
        and indx list, the_array is used to store the vertices in our heap, while indx is use to 
        map those vertices and show which position it is stored in the_array.

        Time-complexity: Best and worst is O(n), where n is the size of vertex_arr
        Explanation: O(n + n + n)
                   : O(n (create list for the_array) + n(create list for indx) + n(assign intial values to the_array and indx))
                   : O(3n)
                   : O(n)

        Auxiliary-time complexity: O(n), where n is the size of vertex_arr
        Explanation: Two additional list of size O(n) will be created.

        Space-complexity: O(n), where n is the size of vertex_arr
        Explanation: Input + Auxiliary
                   : O(n) + O(n)
                   : O(2n)
                   : O(n)
        """
        self.length = len(vertex_arr)
        self.the_array = [None]*(len(vertex_arr) + 1)
        self.indx = [None] * len(vertex_arr)

        for i in range(1,len(self.the_array)):
            self.the_array[i] = vertex_arr[i-1]            #initialise array
            self.indx[i-1] = i                             #initialise index

    def __len__(self) -> int:
        """
        This function returns the number of vertices we have in our heap when we call len() on our 
        heap.

        Time-complexity: Best and worst is O(1).
        Explanation: Function runs at constant time.

        Auxiliary-time complexity: O(1).
        Explanation: Fucntion is an in place algorithm.

        Space-complexity: O(1).
        Explanation: Input + Auxiliary
                   : O(1)

        """
        return self.length

    def is_full(self) -> bool:
        """
        This function returns a boolean whether our MinHeap is full(all the empty spaces are filled)

        Time-complexity: Best and worst is O(1).
        Explanation: Function runs at constant time.

        Auxiliary-time complexity: O(1)
        Explanation: In place algorithm.

        Space-complexity: O(1)
        Explanation: Input + Auxiliary
                   : O(1)
        """
        return self.length + 1 == len(self.the_array)

    def rise(self, k: int) -> None:
        """
        The function rise vertex at index k to its correct position. Along rising, the positions
        in the heap and the indx list are updated.

        Pre-cond: 1<= k <= self.length
        Post-cond: The vertex at index k is risen to the correct position, positions in heap and indx list
                   are also updated.

        Time-complexity: Worst is O(log N), where N is the size of the_array.
        Explanation: The depth of the MinHeap is log N, hence at worst case 
                    where it needs to rise until position 1 in heap, it will take at most log N
                    iterations. 

        Auxiliary-time complexity: O(1).
        Explanation: This is an in-place algorithm.

        Space-complexity: O(1)
        Explanation: Input + Auxiliary
                   : O(1)

        """
        while k > 1 and self.the_array[k].cost < self.the_array[k // 2].cost:
            pos1 = self.the_array[k].id
            pos2 = self.the_array[k//2].id
            self.swap(k, k // 2)                #update position in heap
            self.swap_indx(pos1,pos2)           #update position in indx mapping list
            k = k // 2

    def smallest_child(self, k: int) -> int:
        """
        The function returns the index of the largest child of k.
                
        Pre-cond:2*k <= self.length (at least one child)
        Post-cond: Position of the largest child of k is returned.

        Time-complexity: Best and worst is O(1).
        Explanation: Function runs at constant time.

        Auxiliary-time complexity: O(1)
        Explanation: This is an in place algoritm.

        Space-complexity: O(1)
        Explanation: Input + Auxiliary
                   : O(1)

        """
        if 2 * k == self.length or self.the_array[2 * k].cost < self.the_array[2 * k + 1].cost:
            return 2*k
        else:
            return 2*k+1

    def sink(self, k: int) -> None:
        """ 
        This function make the vertex at index k sink to the correct position.

        Time-complexity: Worst is O(log N), where N is the size of the Heap, which is size of self.the_array
        Explanation: The depth of the MinHeap is log N, hence at worst case 
                    where it needs to sink until the last position in heap, it will take at most log N
                    iterations. 

        Auxiliary-time complexity: O(1)
        Explanation: The function runs at constant time.

        Space-complexity: O(1)
        Explanation: Input + Auxiliary
                   : O(1)

        """
        while 2*k <= self.length:
            child = self.smallest_child(k)
            if self.the_array[k].cost <= self.the_array[child].cost:
                break
            pos1 = self.the_array[k].id
            pos2 = self.the_array[child].id
            self.swap(child, k)                 #update position in heap
            self.swap_indx(pos1,pos2)           #update position in indx mapping list
            k = child

    def swap(self,index1:int,index2:int) -> None:
        """
        The function swap the two vertices at index index1 and index2 of the_array.

        Time-complexity: Best and worst is O（1）
        Explanation: The function runs at constant time.

        Auxiliary-time complexity: O(1).
        Explanation This is an in place algorithm.

        Space-complexity: O(1)
        Explanation: Input + Auxiliary
                   : O(1)
        """
        self.the_array[index1],self.the_array[index2] = self.the_array[index2],self.the_array[index1]

    def swap_indx(self,index1:int, index2:int) -> None:
        """
        The function swaps the position data at index1 and index2 of indx list and updates the position
        of the corresponding vertices in the MinHeap(the_array)

        Time-complexity: Best and worst is O(1)
        Explanation: The function runs at constant time

        Auxiliary-time complexity: O(1)
        Explanation: This is an in place algorithm

        Space-complexity: O(1)
        Explanation: Input + Auxiliary
                   : O(1)
        """
        self.indx[index1],self.indx[index2] = self.indx[index2],self.indx[index1]

    def serve(self) -> None:
        """
        The function returns a vertex which is at position 1 in the_array. The function also swaps
        the position of vertex at index 1 and self.length and then decreases the heap size by 1.
        
        Time-complexity: Worst is O(log N), where N is the size of self.the_array.
        Explanation: self.sink runs at O(log N) for worst case.

        Auxiliary-time complexity: O(1)
        Explanation: This is an in place algorithm.

        Space-complexity: O(1)
        Explanation: Input + Auxiliary
                   : O(1)
        """
        popped = self.the_array[1]
        pos1 = self.the_array[1].id
        pos2 = self.the_array[self.length].id
        self.swap(1,self.length)                        #update position in heap
        self.swap_indx(pos1,pos2)                       #update position in indx mapping list
        self.length -= 1
        self.sink(1)
        return popped

class Graph:
    """
    This the class for constructing an undirected weighted graph.
    """
    def __init__(self,n:int) -> None:
        """
        This is the __init__ function for Graph class which adds n number of vertices into a list
        called self.vertices.

        Time-complexity: Best and worst is O(n), where n is the input n
        Explanation: O(n(create self.vertices) + n(fill in self.vertices with Vertices) )
                   : O(2n)
                   : O(n)

        Auxiliary-time complexity: O(n), where n is the input n
        Explanation: Function creates a list of size n.

        Space-complexity: O(n)
        Explanation: Input + Auxiliary
                   : O(1 + n)
                   : O(n)
        """
        self.vertices = [None]*n
        for i in range(n):
            self.vertices[i] = Vertex(i)
    
    def add_edges(self, argv_edges:list) -> None:
        """
        This function adds all the edges in argv_edges list to the respective vertices. The
        function adds the edges in both direction, hence constructing an undirected weighted graph. 
        
        Pre-cond: The tuples in argv_edges are in the form (u,v,w)

        Time-complexity: Best and worst is O(n), where n is the size of argv_edges.
        Explanation: The function loops through the whole list and add each of the edges.

        Auxiliary-time complexity: O(1)
        Explanation: This function is an in place algorithm.

        Space-complexity: O(n), where n is the size of argv_edges.
        Explanation: Input + Auxiliary
                   : O(1 + n)
                   : O(n)
        """
        for edge in argv_edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            current_edge = Edge(u,v,w)
            current_vertex = self.vertices[u]
            current_vertex.add_edge(current_edge)

            current_edge = Edge(v,u,w)
            current_vertex = self.vertices[v]
            current_vertex.add_edge(current_edge)   #for undirected weighted
    
    def dijkstra(self,source:int,end:int,delivery_path:tuple) -> tuple:
        """
        This function takes a source,end, a delivery path and returns a tuple in the form 
        (cost,path,delivery_path_used), where cost is the smallest cost from source 
        to end, path is the path taken from source to reach end with the smallest cost, delivery_path_used
        is a boolean, whether through the path, if the delivery path has been used.
        
        Pre-cond: Source and end is an integer in the range [0...n-1] where n is the number of vertices in the graph.

        Time-complexity: Worst is O(E log V), where E is the number of edges in the graph and V is the number of vertices in graph.
                         Best is (log V), where V is the number of vertices in graph.
        Explanation: Worst case is when the end vertex is the last vertex to be served and finalised. 
                     Best case is when the end vertex is served and finalised directly after the source vertex.

                     Worst case:
                     O(V(create MinHeap) + log V (rise source) + E log V (serve from minHeap and relax edges until end vertex is reached) 
                     + V(get path from source to end))
                     :O(2V + log V + E log V)
                     :O(E log V)

        Auxiliary-time complexity: O(n), where n is the number of vertices in graph.
        Explanation: Creating a MinHeap and backtracking path requires O(n) auxiliary-space complexity:

        Space-complexity:O(n), where n is the number of vertices in graph.
        Explanation: Input + Auxiliary
                   : O(1 + n)
                   : O(n)

        """
        delivery_path_used = False
        self.vertices[source].cost = 0
        discovered = MinHeap(self.vertices)             #create MinHeap and add all vertices into MinHeap
        discovered.rise(discovered.indx[source])        #rise the source vertex
        while (len(discovered)) > 0 :
            u = discovered.serve() 

            if u.id == end:                             #reached our end, terminate early
                path,delivery_path_used = self.get_path(source,end,delivery_path)   #backtrack to get path    
                return (u.cost,path,delivery_path_used)

            u.visited = True
            for edge in u.edges:                        #edge relaxation
                v = self.vertices[edge.v]
                if v.discovered == False:
                    v.discovered = True
                    v.cost = u.cost + edge.w
                    v.previous = u
                    position = discovered.indx[v.id]    #calculate positon of vertex v in heap
                    discovered.rise(position)
                elif v.visited == False:
                    if v.cost > u.cost + edge.w:
                        v.cost = u.cost + edge.w
                        v.previous = u
                        position = discovered.indx[v.id] #calculate positon of vertex v in heap
                        discovered.rise(position)    
                          
        path,delivery_path_used = self.get_path(source,end,delivery_path)   #backtrack to get path
        return (self.vertices[end].cost, path, delivery_path_used)
    
    def get_path(self,source:int,end:int,delivery_path:tuple) -> tuple:
        """
        The function returns a tuple in the form (path,delivery_path_used), where path is the 
        path taken from source to reach end with the smallest cost, delivery_path_used
        is a boolean, whether through the path, if the delivery path has been used.

        Pre-cond: Source and end is an integer in the range [0...n-1] where n is the number of vertices in the graph.

        Time-complexity: Best and worst is O(n), where n is the number of vertices in the graph.
        Explanation: The function loops from end vertex until it gets source vertex, and there is a maximum of
                     n vertices, hence O(n).

        Auxiliary-time complexity: O(n), where n is the number of vertices in the graph.
        Explanation: The function creates a list which will be maximum of size O(n).

        Space-complexity: O(n), where n is the number of vertices in the graph.
        Explanation: Input + Auxiliary
                   : O(1 + n)
                   : O(n) 

        """
        delivery_path_used = False
        path = [end]
        previous = self.vertices[end]
        while path[-1] != source:
            previous = previous.previous
            path.append(previous.id)
            if path[-2] == delivery_path[1] and path[-1] == delivery_path[0]:       #check if delivery path is used
                delivery_path_used = True
        return (path,delivery_path_used)

class Vertex:
    """
    This class is the class for a Vertex.
    """
    def __init__(self,id:int) -> None:
        """
        This function initialises the attributes for the Vertex object.

        Time-complexity: Best and worst is O(1)
        Explanation: The function runs at constant time.

        Auxiliary-time complexity: O(1)
        Explanation: This is an in place algorithm.

        Space-complexity: O(1)
        Explanation: Input + Auxiliary
                   : O(1)
        """
        self.id = id
        self.edges = []
        self.discovered = False
        self.visited = False
        self.cost = math.inf 
        self.previous = None

    def add_edge(self, edge) -> None:
        """
        This function takes an edge which is a tuple of (u,v,w) and adds it into the vertex's
        edge list.
        
        Pre-cond: Edge must be in the form (u,v,w)

        Time-complexity: Best and worst is O(1)
        Explanation: The functions runs at constant time.

        Auxiliary-time complexity: O(1)
        Explanation: This is an in place algorithm.

        Space-complexity: O(1)
        Explanation: Input + Auxiliary
                   : O(1)
        """
        self.edges.append(edge)
    
class Edge:
    """
    This is the class for Edge.

    """
    def __init__(self, u:int, v:int, w:int) -> None:
        """
        This function takes u,v,w and assigns it to Edge object's u,v,w attribute.

        Time-complexity: Best and worst is O(1)
        Explanation: The function runs at constant time.

        Auxiliary-time complexity: O(1)
        Explanation: This is an in place algorithm.

        Space-complexity: O(1)
        Explanation: Input + Auxiliary
                   : O(1)

        """
        self.u = u
        self.v = v
        self.w = w

def opt_delivery(n:int,roads:list,start:int,end:int,delivery:tuple) -> tuple:
    """
    This function takes n, which is the number of cities, numbered from [0...n-1], roads, which is 
    a list of tuples in the form (u,v,w) ad each tuple represents an road between cities u and v and w is
    the cost of travelling along the road. Start and end are each an integer in the range[0...n-1].
    Start is the city you start and end is city you need to reach. Delivery is a tuple containing 3 values,
    first value is city where we can pick up the item, second value is city where we can deliver the item,
    third value is the amount of money we can make if we deliver the item from the pickup city to the delivery city.
    The function returns a tuple containing 2 elements, the first element is the most optimal cost of travelling 
    from start city to end city including the profit we made from delivery(if we make the delivery). Second element
    is a list of integers, which represents the cities we need to travel to in order to achieve the cheapest cost, starting 
    from start city and ending with end city.

    Pre-cond: Tuples in road must be in the form of (u,v,w). W is non-negative.

    Time-complexity: Best and worst is O(R log N), where R is the total number of roads and N is the total number of cities.
    Explanation: O(N(create graph) + R(add all edges) + R log N(run dijkstra from start to end) + N(reset vertices) 
                 + R log N(run dijkstra from start city to pickup city) + N(reset vertices)  + R log N(run dijkstra from pickup city to delivery city) 
                 + N(reset vertices)  + R log N(run dijkstra from delivery city to end city) + N(obtain final path))
                 :O(5N + R + 4 R log N)
                 :O(R log N)

    Auxiliary-time complexity: O(N), where N is the total number of cities.
    Explanation: Creating graph and computing the path both takes O(N) auxiliary space complexity.

    Space-complexity: O(R+N), where R is the number of total roads in input roads list and N is the number of cities.
    Explanation: Input + Auxiliary
               : O(R) + O(N)
               : O(R+N)
    """
    my_graph = Graph(n)
    my_graph.add_edges(roads)                           #create graph and add edges for all vertices
    pickup_city,delivery_city,profit = delivery
    delivery_path = (delivery[0],delivery[1])


    start_end = my_graph.dijkstra(start,end,delivery_path)                          #run dijkstra from start city to end city, reset vertices afterwards
    reset(my_graph)
    start_pickup = my_graph.dijkstra(start,pickup_city,delivery_path)               #run dijkstra from start city to pickup city, reset vertices afterwards
    reset(my_graph)
    pickup_delivery = my_graph.dijkstra(pickup_city,delivery_city,delivery_path)    #run dijkstra from pickup city to delivery city, reset vertices afterwards
    reset(my_graph)
    delivery_end = my_graph.dijkstra(delivery_city,end,delivery_path)               #run dijkstra from delivery city to end city

    delivery_profit = start_pickup[0] + pickup_delivery[0] + delivery_end[0] - profit   #as delivery path will be used, subtract profit from total cost

    if start_end[2]:
        start_end[0] -= profit          #check if delivery path used in start city to end city path

    if start_end[0] <= delivery_profit:
        return (start_end[0], [start_end[1][i] for i in range(len(start_end[1])-1,-1,-1)])          #reconstruct path as our path is stored backwards

    else:
        path = []
        for i in range(len(start_pickup[1])-1,-1,-1):
            path.append(start_pickup[1][i])

        for j in range(len(pickup_delivery[1])-2,-1,-1):        #reconstruct path as our path is stored backwards
            path.append(pickup_delivery[1][j])
        
        for l in range(len(delivery_end[1])-2,-1,-1):
            path.append(delivery_end[1][l])
        return (delivery_profit,path)

def reset(graph:Graph) -> None:
    """
    This function is used to reset all the initial attributes of vertices in the graph back to default value.

    Time-complexity: Best and worst is O(N), where N is the number of vertices in graph.
    Explanation: The function loops through all the vertices in graph and reset each vertices' attributes.

    Auxiliary-time complexity: O(1)
    Explanation: This is an in place algorithm.

    Space-complexity: O(1)
    Explanation: Input + Auxiliary
               : O(1)

    """
    for vertex in graph.vertices:
        vertex.discovered = False
        vertex.visited = False
        vertex.cost = math.inf 
        vertex.previous = None
        vertex.next = None








