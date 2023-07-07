import * as readline from "readline";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function bottle(num: number) {
  let count = 0;
  while (num + 1 > 3) {
    const a = Math.floor(num / 3);
    const b = num % 3;
    num = a + b;
    count += a;
    // 最后剩两个瓶子
    if (num == 2) {
      count += 1;
      break;
    }
  }
  return count;
}

rl.on("line", function (line) {
  const num = parseInt(line) || 0;
  if (num == 0) {
    rl.close();
  } else {
    const count = bottle(num);
    console.log(count);
  }
});
