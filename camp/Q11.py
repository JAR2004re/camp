import heapq

class State:
    def __init__(self,j1,j2,parent=None,action="initial"):
        self.j1=j1
        self.j2=j2
        self.parent=parent
        self.action=action
        self.cost=0
        
    def __lt__(self,other):
        return self.cost<other.cost
    def __eq__(self,other):
        return self.j1==other.j1 and self.j2==other.j2
    def __hash__(self):
        return hash((self.j1,self.j2))
    

def swjp(cap1,cap2,target):
    initial_st=State(0,0)
    goal_st=State(target,0)
    open_list=[]
    closed_set=set()
    heapq.heappush(open_list,initial_st)
    
    while open_list:
        curr_st=heapq.heappop(open_list)
        if curr_st==goal_st:
            path=[]
            while curr_st.parent:
                path.append(curr_st.action)
                curr_st=curr_st.parent
            path.reverse()
            return path
        
        if curr_st in closed_set:
            continue
        closed_set.add(curr_st)
        
        #fill j1
        if curr_st.j1<cap1:
            fillj1=min(cap1-curr_st.j1,cap2-curr_st.j2)
            new_st=State(curr_st.j1+fillj1,curr_st.j2,curr_st,"fill j1")
            new_st.cost=new_st.parent.cost+1
            heapq.heappush(open_list,new_st)
            
        #fill j2
        if curr_st.j2<cap2:
            fillj2=min(cap2-curr_st.j2,cap1-curr_st.j1)
            new_st=State(curr_st.j1,curr_st.j2+fillj2,curr_st,"fill j2")
            new_st.cost=new_st.parent.cost+1
            heapq.heappush(open_list,new_st)
        
        #empty j1
        if curr_st.j1>0:
            new_st=State(0,curr_st.j2,curr_st,"empty j1")
            new_st.cost=new_st.parent.cost+1
            heapq.heappush(open_list,new_st)
            
        #empty j2
        if curr_st.j2>0:
            new_st=State(curr_st.j1,0,curr_st,"empty j2")
            new_st.cost=new_st.parent.cost+1
            heapq.heappush(open_list,new_st)
            
        #pour j1 to j2
        if curr_st.j1>0 and curr_st.j2<cap2:
            pj1toj2=min(curr_st.j1,cap2-curr_st.j2)
            new_st=State(curr_st.j1-pj1toj2,curr_st.j2+pj1toj2,curr_st,"Pour j1 to j2")
            new_st.cost=new_st.parent.cost+1
            heapq.heappush(open_list,new_st)
            
        #pour j2 to j1
        if curr_st.j1<cap1 and curr_st.j2>0:
            pj2toj1=min(cap1-curr_st.j1,curr_st.j2)
            new_st=State(curr_st.j1+pj2toj1,curr_st.j2-pj2toj1,curr_st,"Pour j2 to j1")
            new_st.cost=new_st.parent.cost+1
            heapq.heappush(open_list,new_st)
            
    return None

def main():
    cap1=4
    cap2=3
    target=2
    sol=swjp(cap1,cap2,target)
    
    if sol:
        print("sol is:")
        for step,action in enumerate(sol):
            print(f"Step {step+1} : {action}")
    else:
        print("no sol")
        
if __name__=="__main__":
    main()