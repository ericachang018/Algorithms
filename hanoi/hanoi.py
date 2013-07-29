
import control

if __name__ == "__main__":
    control.run_hanoi()

# Recursive solution 
# def towersOfHanoi(n, start, holder, end):
#     print "hanoi( ", n, start, holder, end, " called"
#     if n > 0:
#         # move tower of size n - 1 to holder:
#         towersOfHanoi(n - 1, start, end, holder)
#         # move disk from start peg to end peg
#         if start[0]:
#             disk = start[0].pop()
#             print "moving " + str(disk) + " from " + start[1] + " to " + end[1]
#             end[0].append(disk)
#         # move tower of size n-1 from holder to end
#         towersOfHanoi(n - 1, holder, start, end)
        
# start = ([3,2,1], "start")
# end = ([], "end")
# holder = ([], "holder")
# towersOfHanoi(len(start[0]),start,holder,end)


# print start, holder, end


# # Iterative 
# """
# Class that models one Hanoi move (a node in recursion binary tree)
# """
# class HanoiMove:
#     #number of moves to make
#     num = None
 
#     def __init__(self):
#         #True if this move/node has unvisited left child nodes 0
#         self.leftMoves = True
 
#     def __init__(self,source,destination,pivot,num,leftMoves):
#         self.source = source
#         self.destination = destination
#         self.pivot = pivot
#         self.num = num
#         self.leftMoves = leftMoves



#   #string representation
#     def __str__(self):
#         return "Move from stack " + self.source + " to stack " + self.destination
 
#     def setnum(self,val):
#         self.num = val
#         if val == 1:
#             self.leftMoves = False
 
#     def getNum(self):
#         return self.num
 
#     num = property(getNum,setNum)
 
 
# def visitHanoiNode(hanoinode):
#     print hanoinode

# def solveHanoi(int num, visitorfunc):
#     stack = deque()
 
#     stack.append(HanoiMove('A','B','C',num))
 
#     while(len(stack)>0):
#         #collections.deque doens't have "peek" method
#         root = stack[len(stack)-1]
 
#         if root.num == 1:
#             visitorfunc(root)
#             stack.pop()
#         else if root.leftMoves == True:
#             num = root.num
#             source = root.source
#             destination = root.destination
#             pivot = root.pivot
#             stack.pop()
 
#             stack.append(HanoiMove(source,destination,pivot,num,0))
#             while num>1:
#                 temp = stack[len(stack)-1]
#                 num -=1
#                 source = temp.source
#                 destination = temp.destination
#                 pivot = temp.pivot()
#                 stack.append(HanoiMove(source,pivot,destination,num,0))
 
#         else:
#             visitorfunc(root)
#             stack.pop()
#             source = root.source
#             pivot = root.pivot
#             destination = root.destination
             
#             num = root.num-1
#             stack.append(HanoiMove(pivot,destination,source,num,1)    

