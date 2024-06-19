#!/usr/bin/node
function f (n) {
  if (n === 0 || !n) {
    return (1);
  } else {
    return (f(n - 1) * n);
  }
}
const num = parseInt(process.argv[2]);
console.log(f(num));
