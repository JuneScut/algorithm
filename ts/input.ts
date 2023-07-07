import * as readline from "readline";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
rl.on("line", function (line: string) {
  const tokens = line.split(" ");
  console.log(parseInt(tokens[0]) + parseInt(tokens[1]));
});
