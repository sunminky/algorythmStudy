/*https://programmers.co.kr/learn/courses/30/lessons/12921*/

function solution(n) {
    var arr = new Array();
    let answer = 0

    for(var i=0;i<n;i++)
        arr.push(0)

    //에라토스테너스의 체
    for(var i=2;i<=n;i++){
        if(arr[i-1] == 0){
            for(var j=2;i*j<=n;j++)
                arr[i*j-1] = 1;
        }
    }

    for(var i=2;i<=n;i++)
        if(arr[i-1] == 0)
            answer++

    return answer;
}

solution(10)    //4
solution(5) //3
