from collections import deque

def solution(cards1, cards2, goal):
    q_cards1 = deque(cards1)
    q_cards2 = deque(cards2)
    q_goal = deque(goal)
    while q_goal:
        # 큐가 비면 인덱스에 접근이 불가능하다
        if q_cards1 and q_cards1[0] == q_goal[0]:
            q_cards1.popleft()
        elif q_cards2 and q_cards2[0] == q_goal[0]:
            q_cards2.popleft()
        else:
            return 'No'
        q_goal.popleft()
    return 'Yes'