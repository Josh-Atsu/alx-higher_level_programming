#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let incr = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { incr = incr + 1; }
  }
  return (incr);
};
