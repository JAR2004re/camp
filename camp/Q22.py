import heapq

goal_st=[
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

def man_dist(state):
    dist=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=0:
                goal_row,goal_col=divmod(goal_st[i][j]-1,3)
                dist+=abs(i-goal_row)+abs(j-goal_col)
    return dist


def astsearch(initial_st):
    visited=set()
    heap=[(man_dist(initial_st),initial_st,0,"")]
    
    while heap:
        _,curr_st,cost,path=heapq.heappop(heap)
        if curr_st==goal_st:
            return path,cost
        zero_row,zero_col=[(i,j) for i in range (3) for j in range (3) if curr_st[i][j]==0][0]
        possible_moves=[(zero_row-1,zero_col),(zero_row+1,zero_col),(zero_row,zero_col-1),(zero_row,zero_col+1)]
        for move_row,move_col in possible_moves:
            if 0<=move_row<3 and 0<=move_col<3:
                new_st=[row[:] for row in curr_st]
                new_st[zero_row][zero_col],new_st[move_row][move_col]=new_st[move_row][move_col],new_st[zero_row][zero_col]
                if tuple(map(tuple,new_st))not in visited:
                    visited.add(tuple(map(tuple,new_st)))
                    new_cost=cost+1
                    new_path=path+str((move_row,move_col))
                    heapq.heappush(heap,(new_cost+man_dist(new_st),new_st,new_cost,new_path))
                    
    return "No sol" , float ("inf")

initial_st=[
    [1,0,3],
    [4,2,5],
    [7,8,6]
]
path,cost=astsearch(initial_st)
print("in st:")
for row in initial_st:
    print(row)
print("goal st:")
for row in goal_st:
    print(row)
    
print(f"path is :{path}")
print(f"no of moves is:{cost}")