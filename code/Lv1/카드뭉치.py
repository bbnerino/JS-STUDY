from collections import deque
cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]


def solution(cards1, cards2, goal):
    
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    for word in goal:
      if cards1 and word == cards1[0]:
         cards1.popleft()
         continue
      elif cards2 and word ==  cards2[0]:
         cards2.popleft()
         continue
      else:
         return "No"    
    return "Yes"

    

print(solution(cards1,cards2,goal))

