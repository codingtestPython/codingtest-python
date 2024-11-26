// 절대 자바스크립트로는 코테 보지 말아야 하는 이유

function solution(genres, plays) {
    let l = genres.length;
        map = new Map();
        arr = Array.from([...new Set(genres)]);
    for (let i = 0; i < l; i++) {
        let g = arr[arr.indexOf(genres[i])];
        map.set(g, (map.get(g) || 0) + plays[i]);
    }
    arr = [...map.entries()].sort((a, b) => b[1] - a[1]);
    let genres_map = new Map;
    for (let i = 0; i < l; i++) {
        let g = genres[i];
        genres_map.set(g, (genres_map.get(g) || 0) + 1);
    }
    let genres_obj = [];
    for (let i = 0; i < l; i++) {
        genres_obj[i] = {genres: genres[i], index: i, plays: plays[i], genresCount: genres_map.get(genres[i])};
    }
    genres_obj.sort((a, b) => b.plays - a.plays);
    for (let i = 0; i < arr.length; i++) {
        genres_obj.sort((a, b) => {
            if (a.genres === arr[i][0] && b.genres !== arr[i][0]) {
                return -1;
            } else if (a.genres !== arr[i][0] && b.genres === arr[i][0]) {
                return 1;
            } else {
                return 0;
            }
        })
    }
    genres_obj.reverse();
    genres_obj.push({genres: 'genre', index: 0, plays: 0});
    genres_obj.push({genres: 'genre', index: 0, plays: 0});

    let result = [];
    arr = [];
    let j = 0;
    for (let i = 0; i < l; i++) {
        if (genres_obj[i].genresCount == 1) {
            result.push(genres_obj[i].index);
        } else if (genres_obj[i].genres !== genres_obj[i + 2].genres) {
            j++;
            result.push(genres_obj[i].index);
        } else {
            result.push(-1);
        }
        if (j >= 2) {
            j = 0;
            let r = result[i - 1];
            result[i - 1] = result[i];
            result[i] = r;
        }
    }
    result = result.filter((v) => v >= 0);
    return result;
}