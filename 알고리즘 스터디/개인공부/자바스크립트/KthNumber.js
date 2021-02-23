/*https://programmers.co.kr/learn/courses/30/lessons/42748?language=javascript*/

function solution(array, commands) {
    var answer = new Array();

    for(var i=0;i < commands.length;i++) {
        //배열 자르기
        var n_arr = array.slice(commands[i][0] - 1, commands[i][1]);    //잘린 배열의 복사본 반환
        //정렬 후 k번째 원소 반환
        answer.push(n_arr.sort((a, b)=>{
            if (a > b)  return 1;
            else if(a === b) return 0;
            else return -1;
        })[commands[i][2]-1])
    }

    return answer;
}

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) //[5, 6, 3]