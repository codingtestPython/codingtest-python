def solution(record):
    answer = []
    uid_dict = {}

    for r in record:
        split_r = r.split()
        if split_r[0] == "Enter" or split_r[0] == "Change":
            uid_dict[split_r[1]] = split_r[2]

    for r in record:
        split_r = r.split()
        if split_r[0] == "Enter":
            answer.append(f"{uid_dict[split_r[1]]}님이 들어왔습니다.")
        elif split_r[0] == "Leave":
            answer.append(f"{uid_dict[split_r[1]]}님이 나갔습니다.")

    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

# 결국 문제를 풀기 위해 최종적으로 필요한 데이터가 무엇인지에서부터 역으로 생각해 보는 과정이 크게 도움이 되었다.
# uid라는 해시값을 기준으로 닉네임을 변경한다고 생각하면 되려나