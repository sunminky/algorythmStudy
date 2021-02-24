/*https://level.goorm.io/exam/43219/%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%92%A4%EC%A7%91%EA%B8%B0/quiz/1*/

// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on("line", function(line) {
    arr = Array.from(line).reverse()
    console.log(arr.join(''));  //배열을 문자열로 바꾸기
    rl.close();
}).on("close", function() {
    process.exit();
});
