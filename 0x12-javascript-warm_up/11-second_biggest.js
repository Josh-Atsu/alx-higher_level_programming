#!/usr/bin/node
const len = process.argv.length;
if (len === 2 || len === 3) {
  console.log(0);
} else {
  const myList = [];
  for (let i = 0; i < (len - 2); i++) {
    myList[i] = Number(process.argv[i + 2]);
  }
  myList.sort((a, b) => b - a);
  console.log(myList[1]);
}
