

def DebugPrint(state):
	for i in state:
		row = ''
		for j in i:
			row += j + '\t'
		row = row[:-1]


def LoadFromFile(filepath):
	puzzle = []
	with open(filepath, 'r') as f:
		count = -1
		for line in f:
			if count == -1:
				n = int(line)
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
			pairs.append(findPair(state, x, y, x-1, y))
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
			pairs.append(findPair(state, x, y, x+1, y))
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
def findGoal(state):
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
	return goal

def isGoal(state):
	return (findGoal(state) == state)

def makeTupleState(state):
	tupleState = []
	for i in state:
		tupleState.append(tuple(i))
	return tuple(tupleState)

def BFS(state):
	frontier = [state]
	discovered = set(makeTupleState(state))
	parents = {makeTupleState(state): None}
	while len(frontier) != 0:
		current_state = frontier.pop(0)
		discovered.add(makeTupleState(current_state))
		if isGoal(current_state):
			cs = current_state
			answer = []
			while parents[makeTupleState(cs)] != None:
				answer.append(cs)
				cs = parents[makeTupleState(cs)]
			answer.append(cs)
			return answer
		for neighbor in ComputeNeighbors(current_state):
			if makeTupleState(neighbor[1]) not in discovered:
				frontier.append(neighbor[1])
				discovered.add(makeTupleState(neighbor[1]))
				parents[makeTupleState(neighbor[1])] = current_state

def DFS(state):
	frontier = [state]
	discovered = set(makeTupleState(state))
	parents = {makeTupleState(state): None}
	while len(frontier) !=  0:
		current_state = frontier.pop()
		discovered.add(makeTupleState(current_state))
		if isGoal(current_state):
			cs = current_state
			answer = []
			while parents[makeTupleState(cs)] != None:
				answer.append(cs)
				cs = parents[makeTupleState(cs)]
			answer.append(cs)
			return answer[1:]	 
		for neighbor in ComputeNeighbors(current_state):
			if makeTupleState(neighbor[1]) not in discovered:
				discovered.add(makeTupleState(neighbor[1]))
				frontier.append(neighbor[1])
				parents[makeTupleState(neighbor[1])] = current_state



def BDS(state):
	goalState = findGoal(state)
	frontier = [state]
	rFrontier = [goalState]
	discovered = set(makeTupleState(state))
	rDiscovered = set(makeTupleState(goalState))
	rParents = {makeTupleState(goalState): None}
	parents = {makeTupleState(state): None}
	while len(frontier) != 0 and len(rFrontier) != 0:
		current_state = frontier.pop(0)
		discovered.add(makeTupleState(current_state))
		for i in discovered:
			if i in rDiscovered:
				cs = current_state
				answer = []
				while parents[makeTupleState(cs)] != None:
					answer.append(cs)
					cs = parents[makeTupleState(cs)]
				answer.append(cs)
				rcs = rCurrent_state
				rAnswer = []
				while rParents[makeTupleState(rcs)]:
					rAnswer.append(rcs)
					rcs = rParents[makeTupleState(rcs)]
				rAnswer.append(rcs)
				answer.reverse()
				return answer + rAnswer
		rCurrent_state = rFrontier.pop(0)
		rDiscovered.add(makeTupleState(rCurrent_state))
		for i in discovered:
			if i in rDiscovered:
				return i
		for neighbor in ComputeNeighbors(current_state):
			if makeTupleState(neighbor[1]) not in discovered:
				discovered.add(makeTupleState(neighbor[1]))
				frontier.append(neighbor[1])
				parents[makeTupleState(neighbor[1])] = current_state
		for neighbor in ComputeNeighbors(rCurrent_state):
			if makeTupleState(neighbor[1]) not in rDiscovered:
				rDiscovered.add(makeTupleState(neighbor[1]))
				rFrontier.append(neighbor[1])
				rParents[makeTupleState(neighbor[1])] = rCurrent_state

