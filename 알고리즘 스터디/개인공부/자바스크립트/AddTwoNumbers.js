/*https://programmers.co.kr/learn/courses/30/lessons/68644?language=javascript*/

function solution(numbers) {
    var answer = [];

    for(var i=0;i<numbers.length;i++){
        for(var j=i+1;j<numbers.length;j++){
            answer.push(Number(numbers[i] + numbers[j]))
        }
    }

    return Array.from(new Set(answer)).sort((a, b) => {
        if(a > b) return 1;
        if(a === b) return 0;
        if(a < b) return -1;
    });
}

solution([2,1,3,4,1])
