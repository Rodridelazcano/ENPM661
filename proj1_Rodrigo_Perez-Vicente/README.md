##Project 1. 8 Puzzle Problem
#1. Instructions
	1. Run python file SourceCode.py
	2. Enter each element of the 3x3 matrix in the terminal. "Enter element(x,x):"
	3. If any element repeats or is not in the range 0-8 or the puzzle is not solvable, the program will re-initialize.
	4. If the input is correct, wait until solved
	5. Output files: Nodes.txt ,Nodes_Info.txt and node_Path.txt
	6. Run plot_path.py to visualize shortst path to solve
#2. Libraries
	**NumPy:**adds support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. The nodes of the problem are stored as 3x3 arrays
	**OS module:** allows Python to interface with the underlying opperating system. Used to remove or create new files to store the nodes data.
