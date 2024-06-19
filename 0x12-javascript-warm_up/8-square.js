#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (num) {
  let i = 0; let j = 0;
  for (i = 0; i < num; i++) {
    for (j = 0; j < num; j++) {
      console.log('X');
    }
  }
} else {
  console.log('Missing size');
}
