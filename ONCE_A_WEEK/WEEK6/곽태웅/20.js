function solution(participant, completion) {
    let map = new Map();
        pl = participant.length;
        result = '';
    
    for (let i = 0; i < pl; i++) {
        let p = participant[i];
            c = completion[i];
        
        map.set(p, (map.get(p) || 0) + 1);
        map.set(c, (map.get(c) || 0) - 1);
    }
    
    map.forEach((v, k) => {
        if (v > 0) result = k;
    })
    
    return result;
}

// 자바스크립트로는 코테보는 게 아니다...
// 과거에 풀었던 기록이 남아있어서 추가