def solution(answers):
    man_dict = {
        1: {
            'type': [1, 2, 3, 4, 5],
            'score': 0,
        },
        2: {
            'type': [2, 1, 2, 3, 2, 4, 2, 5],
            'score': 0,
        },
        3: {
            'type': [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
            'score': 0,
        },
    }

    for i in range(0, len(answers)):
        for j in range(0, 3):
            if answers[i] == man_dict[j].type[i % len(man_dict[1].type)]:
                man_dict[j].score += 1

    winner_list = []
    
    if man_dict[1].score >= man_dict[2].score and man_dict[1].score >= man_dict[3].score:
        winner_list.append(1)
    elif man_dict[2].score >= man_dict[1].score and man_dict[2].score >= man_dict[3].score:
        winner_list.append(2)
    elif man_dict[3].score >= man_dict[2].score and man_dict[3].score >= man_dict[1].score:
        winner_list.append(3)

    return winner_list