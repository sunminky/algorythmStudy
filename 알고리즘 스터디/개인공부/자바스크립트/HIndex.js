/*https://programmers.co.kr/learn/courses/30/lessons/42747?language=javascript*/

function solution(citations) {
    var answer = 0;

    citations.sort((a, b) => {
        if(a > b) return -1;
        if(a === b) return 0;
        if(a < b) return 1;
    })

    for(var i=0;i <citations.length;i++){
        if(citations[i] <= i) {
            answer = i
            return answer
        }
    }

    return citations.length;
}

console.log(solution([10,11,12,13]))    //4

/*def solution(citations):
answer = 0
citations.sort()
citations.reverse()
#인용된 횟수보다 논문이 더 많은 경우
for i in range(len(citations)):
#인용된 횟수(i+1) 비교
if(citations[i] <= i):    #h번 이상 인용된 논문수가 h개 이상
answer = i
return answer
return len(citations)*/
