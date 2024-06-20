#!/usr/bin/node
exports.esrever = function (list) {
  const mylist = [];
  const len = list.length; let j = 0;
  for (let i = len - 1; i >= 0; i--) {
    mylist[j] = list[i]; j++;
  }
  return (mylist);
};
