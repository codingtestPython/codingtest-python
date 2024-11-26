from collections import Counter

def solution(genres, plays):
    play_list = [{'genre': genres[i], 'play': plays[i], 'index': i} for i in range(len(genres))]
    
    sorted_list = sorted(play_list, key=lambda x: (-x['play'], x['index']))

    genres_counter = Counter()
    for genre, play in zip(genres, plays):
        genres_counter[genre] += play

    sorted_genres = genres_counter.most_common()

    answer = []
    
    for genre, _ in sorted_genres:
        count = 0
        for song in sorted_list:
            if song['genre'] == genre:
                count += 1
                if count <= 2:
                    answer.append(song['index'])
                else:
                    break

    return answer

solution(["classic", "pop", "classic", "classic", "pop"], 	[500, 600, 150, 800, 2500])

# 너무 유지보수하기 어렵고, 복잡한 코드가 아닐까...
# 결론적으로 속도는 O(n log n) 수준이니, 이보다 간단하게 구현할 방법이 필요할 것 같다