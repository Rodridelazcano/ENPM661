import numpy as np
import os

class Node: #each generated Node will be a class defined by its value, index of the node generated and its parent node
    def __init__(self, node_state, node_index, parent_node):
        self.node_state = node_state
        self.node_index = node_index
        self.parent_node = parent_node

def Insert_Input(): #gets the value of each element of the puzzle from the terminal
    print("WELCOME to 8 Puzzle Solver by Rodrigo Perez-Vicente \nEnter element value of matrix 3x3 from range 0-8, do not repeat values:")
    Input= np.zeros((3,3))
    for i in range(3):
        for j in range(3):            
            Input[i,j] = int(input("\t Enter element ("+ str(i+1) + ","+str(j+1)  + "):"))
    return Input

def CheckInput(Node): #checks if the input has the right values between 0-8 and no repeated values
    Input=np.reshape(Node,9)
    for i in range(9):
        repeat_count=0
        if Input[i]<0:
            print("There is an element lower than 0, please re-enter values:")
            return False
        elif Input[i]>8:
            print("There is an element higher than 8, please re-enter values:")
            return False
        for j in range(9):
            if Input[i]==Input[j]:
                repeat_count+=1
            if repeat_count>1:
                return False
    return True
            
def CheckSolution(Node): #checks if there is a final solution for the puzzle https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
    NodeList = np.reshape(Node, 9)
    inv_count = 0
    for i in range(9):
        if not NodeList[i] == 0:
            check_value = NodeList[i]
            for j in range(i + 1, 9):
                if check_value > NodeList[j] and NodeList[j] != 0:
                    inv_count+=1
                else:
                    continue
    if inv_count% 2 == 0:
        print("Solvable, wait until solved")

        return True
    else:
        print("Not solvable, re-enter values:")

        return False

def BlankTileLocation(Node): #looks for the blank tile and returns its possition
	
	for i in range(3):#two for loops to search row-columns
		for j in range(3):
			if Node[i,j]==0:
				return i,j  

#####MOVEMENT FUNCTIONS####

def ActionMoveLeft(Node):
	
	i,j=BlankTileLocation(Node)
	NewNode=np.copy(Node)
	if j==0:
		return False
	else:
		NewNode[i,j-1]=0
		NewNode[i,j]=Node[i,j-1]		
		
		return NewNode
def ActionMoveRight(Node):
	
	i,j=BlankTileLocation(Node)
	NewNode=np.copy(Node)
	if j==2:
		return False
	else:
		NewNode[i,j+1]=0
		NewNode[i,j]=Node[i,j+1]		
		
		return NewNode
def ActionMoveUp(Node):
	
	i,j=BlankTileLocation(Node)
	NewNode=np.copy(Node)
	if i==0:
		return False
	else:
		NewNode[i-1,j]=0
		NewNode[i,j]=Node[i-1,j]		
		
		return NewNode
def ActionMoveDown(Node):
	
	i,j=BlankTileLocation(Node)
	NewNode=np.copy(Node)
	if i==2:
		return False
	else:
		NewNode[i+1,j]=0
		NewNode[i,j]=Node[i+1,j]		
		return NewNode
def MOVE(move, Node):  #This function reads the type of movement to be made and the node to be moved and calls the corresponding function moving action and returns that functions resulting new ndoe
	if move == 'left':
        	return ActionMoveLeft(Node)
	if move == 'right':
        	return ActionMoveRight(Node)    
	if move == 'up':
        	return ActionMoveUp(Node)
	if move == 'down':
        	return ActionMoveDown(Node)
	else:
        	return False

def AddNode(Node): #returns the values that will form the lists Nodes_Info and Nodes
    return Node.node_state.tolist(), Node

def generate_path(FinalNode):#reads the shortest path from the beginning Node to the final Node
    path=[]
    path.append(FinalNode.node_state.tolist())
    NodeParent=FinalNode
    while NodeParent.parent_node is not None:
        NodeParent=NodeParent.parent_node
        path.append(NodeParent.node_state.tolist())#saves in path list the node_state of the parent node from the current node
    path.reverse()#reverses path list from beginning node to goal noad

    return path

#####WRITING FUNCTIONS TO CREATE NODES.txt,NodesInfo.txt and nodePath#####
def WriteNodes(Nodes):  
    if os.path.exists("Nodes.txt"):
        os.remove("Nodes.txt")

    f = open("Nodes.txt", "w")
    for value in Nodes:
        for i in range(3):
            for j in range(3):
                f.write(str(value[j][i]) + " ") #writes the values of the nodes column wise       
        f.write("\n")
    f.close()
def WriteNodesInfo(Nodes_Info):  
    if os.path.exists("NodesInfo.txt"):
        os.remove("NodesInfo.txt")

    f = open("NodesInfo.txt", "w")
    for Node in Nodes_Info:
        if Node.parent_node is not None:
            f.write(str(Node.node_index) + " " + str(Node.parent_node.node_index) + "\n")
    f.close()
def WritePath(FinalPath):
    if os.path.exists("nodePath.txt"):
        os.remove("nodePath.txt")

    f = open("nodePath.txt", "w")
    for value in FinalPath:
        for i in range(3):
            for j in range(3):
                f.write(str(value[j][i]) + " ")        
        f.write("\n")
    f.close()

#####ALGORITHM TO SOLVE PUZZLE#####
def Solve(InitialNode):
    GoalNode = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    Node_Queue = [InitialNode] #stores new nodes in a queue to be iterated
    Nodes = [] #stores node_state as list of elements
    Nodes_Info = [] #stores nodes as class
    Nodes.append(Node_Queue[0].node_state.tolist())  
    Node_Index = 0
    print(Node_Queue[0].node_state)
    actions = ["left", "right", "up", "down"]
    while Node_Queue: #in while Node_Queue has values in it
        Actual_Node = Node_Queue.pop(0) #takes Node from queue to be iterated
        
        if Actual_Node.node_state.tolist() == GoalNode.tolist():
                
                return Actual_Node, Nodes_Info, Nodes
                    
        for move in actions: #tries all movement types for a node
            
            temp_Node=MOVE(move,Actual_Node.node_state)
            
            if temp_Node is not False:
                
                Node_Index+=1
                New_Node=Node(temp_Node, Node_Index, Actual_Node)
                
                if New_Node.node_state.tolist() not in Nodes: #verifies if the new node is not in the past nodes list 
                    Node_Queue.append(New_Node)
                    Nodelist,Node_Infolist=AddNode(New_Node)
                    Nodes.append(Nodelist)
                    Nodes_Info.append(Node_Infolist)
                    if New_Node.node_state.tolist() == GoalNode.tolist():
                        
                        return New_Node, Nodes, Nodes_Info
    return None, None, None

Checksol=False
Checkin=False
while Checksol==False or Checkin==False: #if there is no solution to the puzzle oor values enter wrong insert input again
    # A=np.array([[1,2,3],[4,7,0],[5,6,8]])
    A=Insert_Input()
    Checksol=CheckSolution(A)
    Checkin=CheckInput(A)
InitialNode=Node(A,0,None)
GoalNode,Nodes,Nodes_Info=Solve(InitialNode)
print("SOLVED!!!!!!")
WriteNodes(Nodes)
WriteNodesInfo(Nodes_Info)
WritePath(generate_path(GoalNode))    
