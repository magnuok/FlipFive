from collections import deque

flip = {'.': '*', '*': '.'} # toggle set


def toggle(*args): # Create new grid. input cell to toggle: apply toggle on elements in list
    return ''.join(map(lambda x: flip.get(x[1]) if x[0] in args[1] else x[1], enumerate(args[0])))


flip_choices = {
    0: lambda x: toggle(x, [0, 1, 3]),
    1: lambda x: toggle(x, [0, 1, 2, 4]),
    2: lambda x: toggle(x, [1, 2, 5]),
    3: lambda x: toggle(x, [0, 3, 4, 6]),
    4: lambda x: toggle(x, [1, 3, 4, 5, 7]),
    5: lambda x: toggle(x, [2, 4, 5, 8]),
    6: lambda x: toggle(x, [3, 6, 7]),
    7: lambda x: toggle(x, [4, 6, 7, 8]),
    8: lambda x: toggle(x, [5, 7, 8])
}

# Create memoization set
mem = {}

q = deque() # Create queue
q.append(('.........', 0)) # append start_grid with initial depth = 0


#BFS-loop with memoization;

for _ in range(int(input())): # Create goal grid
    _goal = ''
    for _ in range(3):
        _goal += input()
    if _goal in mem: #Check if goal is allready in memoization set
        print(mem.get(_goal)) # prints number of moves if it's in memoization set
    else:
        while q: #for each
            grid, click = q.popleft() # Pops first grid in queue
            if grid in mem:
                # IMPORTANT: Check if grid is in queue.
                #If grid is in queue => Don't have to investigate more
                continue
            mem[grid] = click
            for i in range(9):
                q.append((flip_choices.get(i)(grid), click + 1)) #Create new child grid. Use parent grid. Toggle cell i
            if grid == _goal: #Check if grid equals goal grid
                print(mem.get(_goal)) # Prints moves
                break # finish case
