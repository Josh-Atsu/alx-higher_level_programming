#!/usr/bin/node
exports.addMeMaybe = function addMeMaybe (number, theFunction) {
  number = number + 1;
  theFunction(number);
}
