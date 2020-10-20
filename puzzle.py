

def DebugPrint(state):
	for i in state:
		row = ''
		for j in i:
			row += j + '\t'
		row = row[:-1]
		print(row)


def LoadFromFile(filepath):
	puzzle = []
	with open(filepath, 'r') as f:
		count = -1
		for line in f:
			if count == -1:
				n = int(line)
				print (n)
				for i in range(n):
					puzzle.append([])
				count += 1
			else:
				if count >= n:
					return None
				while line != '\n' and len(line)!= 0:
					if '\t' in line:
						puzzle[count].append(line[0:line.index('\t')])
					else: 
						if '\n' in line:
							puzzle[count].append(line[:line.index('\n')])
							line = line[line.index('\n') +1:]
						else:
							puzzle[count].append(line)
							line = ''
					if line != '\n' and '\t' in line: 
						line = line[line.index('\t') +1:]
				count +=1
	for i in puzzle:
		print(len(i))
		if len(i) != n:
			return None
	return puzzle
	#for i in range(len(puzzle)):
	#	puzzle[i] = puzzle[i][::2]
	#print(puzzle)

def findX(state):
	n = len(state)
	for i in range(n):
		for j in range(n):
			if state[i][j] == '*':
				return [i, j]


def findPair(state, x, y, x2, y2):
	tempState = [row[:] for row in state]
	temp = tempState[x2][y2]
	tempState[x2][y2] = '*'
	tempState[x][y] = temp

	return [temp,tempState]

def ComputeNeighbors(state):
	pairs = []
	n = len(state)

	coords = findX(state)
	x = coords[0]
	y = coords[1]

	if x == n-1:
		if y == 0:
			pairs.append(findPair(state, x, y, x-1, y))
			pairs.append(findPair(state, x, y, x, y+1))
		elif y == x:
			pairs.append(findPair(state, x, y, x-1, y))
			pairs.append(findPair(state, x, y, x, y-1))
		else:
			paris.append(findPair(state, x, y, x-1, y))
			pairs.append(findPair(state, x, y, x, y + 1))
			pairs.append(findPair(state, x, y, x, y-1))
	elif x == 0:
		if y == x:
			pairs.append(findPair(state, x, y, x+1, y))

			pairs.append(findPair(state, x, y, x, y+1))
		elif y == n -1:
			pairs.append(findPair(state, x, y, x+1, y))
			pairs.append(findPair(state, x, y, x, y-1))
		else:
			paris.append(findPair(state, x, y, x+1, y))
			pairs.append(findPair(state, x, y, x, y + 1))
			pairs.append(findPair(state, x, y, x, y-1))
	else:
		if y == 0:
			pairs.append(findPair(state, x, y, x-1, y))
			pairs.append(findPair(state, x, y, x, y+1))
			pairs.append(findPair(state, x, y, x+1, y))
		elif y == n-1:
			pairs.append(findPair(state, x, y, x-1, y))
			pairs.append(findPair(state, x, y, x+1, y))
			pairs.append(findPair(state, x, y, x, y-1))
		else:
			pairs.append(findPair(state, x, y, x-1, y))
			pairs.append(findPair(state, x, y, x, y+1))
			pairs.append(findPair(state, x, y, x+1, y))
			pairs.append(findPair(state, x, y, x, y-1))
	return pairs

def isGoal(state):
	goal = []
	count= 1
	n = len(state)
	for i in range(n):
		goal.append([])
		for j in range(n):
			if count == n*n:
				goal[i].append('*')
			else:
				goal[i].append(str(count))
				count += 1
	return (goal == state)

def BFS(state):
	frontier = [state]
	discovered = set(state)
	parents = {state: none}
	while len(frontier) != 0:
		current_state = frontier.pop(0)
		discovered.add(current_state)
		if IsGoal(current_state):
			print('finished')
			for i in parents:
				DebugPrint(i)
		for neigbor in ComputeNeighbors(current_state):
			if neigbor[1] not in discovered:
				frontier.append(neigbor[1])
				discovered.add(neigbor[1])
				parents[neigbor[1]] = current_state



p = LoadFromFile('testText')
print(p)
DebugPrint(p)
n2 = ComputeNeighbors(p)
print(n2)
DebugPrint(n2[0][1])
BFS(p)


