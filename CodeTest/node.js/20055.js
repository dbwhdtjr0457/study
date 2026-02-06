const fs = require("fs");

let input = fs.readFileSync('./input.txt').toString().trim().split('\n');

const [N, K] = input[0].split(' ').map(Number);
const beltData = input[1].split(' ').map(Number);

let level = 0;

let robotPos = [];

let zeroCount = 0;

while (zeroCount < K) {
    // 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.

    level += 1;

    let temp = beltData.pop();
    beltData.unshift(temp);

    robotPos = robotPos.map(pos => pos + 1);

    if (robotPos[robotPos.length - 1] == N - 1) robotPos.pop();

    // 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 
    // 만약 이동할 수 없다면 가만히 있는다.
    //      1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.

    let lastPosIdx = robotPos.length - 1;

    for (let posIdx = lastPosIdx; posIdx >= 0; posIdx--) {
        let pos = robotPos[posIdx];
        
        if (beltData[pos + 1] > 0 && (posIdx == lastPosIdx || robotPos[posIdx + 1] != pos + 1)) {
            robotPos[posIdx] = pos + 1;
            beltData[pos + 1] -= 1;
            if (beltData[pos + 1] == 0) zeroCount += 1;
        }
    }

    if (robotPos[robotPos.length - 1] == N - 1) robotPos.pop();
    
    // 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.

    if (beltData[0] != 0) {
        beltData[0] -= 1;
        robotPos.unshift(0);

        if (beltData[0] == 0) zeroCount += 1;
    }

    // 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

    if (zeroCount >= K) break;
}

console.log(level);