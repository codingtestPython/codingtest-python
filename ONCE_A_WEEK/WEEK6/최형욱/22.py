def solution(record):
    answer = []
    uid = {}

    for line in record:
        cmd = line.split(" ")

        if cmd[0] != "Leave":
            uid[cmd[1]] = cmd[2]

    for line in record:
        cmd = line.split(" ")

        if cmd[0] == "Enter":
            answer.append(f"{uid[cmd[1]]}님이 들어왔습니다.")
        elif cmd[0] == "Change":
            pass
        else:
            answer.append(f"{uid[cmd[1]]}님이 나갔습니다.")
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))