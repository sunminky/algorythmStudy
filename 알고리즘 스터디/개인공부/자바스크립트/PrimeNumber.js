/*https://programmers.co.kr/learn/courses/30/lessons/42839?language=javascript*/

function solution(numbers) {
    var answer = 0;
    var arrr = []

    function isPrime(num) {
        if(num.length == 0 || Number(num) <= 1)
            return 0;
        else{
            var n = Number(num)

            for(var i=2;i<n;i++){
                if(n % i == 0){
                    return 0;
                }
            }
            return 1;
        }
    }

    function combi(str, c){
        arrr.push(Number(c));

        if(str.length == 0) {
            return;
        }
        else{
            for(var i=0;i<str.length;i++){
                combi(str.slice(0, i) + str.slice(i+1, str.length), c + str[i])
            }
        }
    }

    combi(numbers, "")
    var sarr = new Set(arrr)

    for (let item of sarr) {
        answer += isPrime(item);
    }

    console.log(answer)
    return answer;
}

solution("17")  //3
//solution("011") //2
