#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (num) {
  for (let i = 0; i < num; i++) {
    let str = '';
    for (let j = 0; j < num; j++) {
      str = str + 'X';
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
