/*https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3*/

function solution(s) {
    var answer = Array.from(s.toLowerCase());
    var pattern_eng = /[a-zA-Z]/;
    var prev = answer[0]

    //첫 글자가 알파벳인지 체크
    if(pattern_eng.test(answer[0]))
        //알파벳인 경우 대문자로 바꿔줌
        answer[0] = answer[0].toUpperCase()

    for(var i=1;i<answer.length;i++){
        if(prev === ' ' && pattern_eng.test(answer[i]))
            //이전 문자가 빈칸이고 알파벳인 경우 대문자로 바꿔줌
            answer[i] = answer[i].toUpperCase()
        prev = answer[i]
    }

    return answer.join('');
}

console.log(solution("3people unFollowed me"))
console.log(solution("for the last week"))
console.log(solution("aaaaa  aaa"))
