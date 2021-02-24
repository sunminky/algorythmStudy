/*https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3*/

function solution(s) {
    var trans = s.toLowerCase().split(' ');
    var answer = [];
    var pattern_head = new RegExp("[a-zA-Z]+")

    for(var i=0;i<trans.length;i++){
        var match = trans[i].match(pattern_head)

        if (match === null)
            answer.push(trans[i])
        else {
            answer.push(trans[i][0].toUpperCase() + trans[i].slice(1,))
        }
    }

    return answer.join(" ");
}

console.log(solution("3people unFollowed me"))
console.log(solution("for the last week"))
console.log(solution("aaaaa  aaa"))
