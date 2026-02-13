const fs = require('fs');

let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

let data = input.slice(1).map(Number);



data.forEach(num => {
    let numArr = Array.from({length: num}, (_, i) => i + 1);

    function backTracking(idx, operArr, resultArr) {
        if (idx == num) {
            let arrSum = resultArr.reduce((acc,val) => acc + val, 0);
            if (arrSum == 0) {
                let result = ''

                for (let i = 0; i < numArr.length; i++) {
                    result += numArr[i];
                    if (operArr[i]) result += operArr[i]
                }

                console.log(result);
            }
            return;
        }

        operArr.push(' ');
        backTracking(idx + 1, operArr, [...resultArr.slice(0, resultArr.length - 1), Number(resultArr[resultArr.length - 1] + String(numArr[idx]))]);
        operArr.pop();

        operArr.push('+');
        resultArr.push(numArr[idx]);
        backTracking(idx + 1, operArr, resultArr);
        operArr.pop();
        resultArr.pop();

        operArr.push('-')
        resultArr.push(numArr[idx] * -1);
        backTracking(idx + 1, operArr, resultArr);
        operArr.pop();
        resultArr.pop();
    }

    backTracking(1, [], [1]);

    console.log();
})