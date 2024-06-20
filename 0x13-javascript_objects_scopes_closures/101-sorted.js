#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const Ids in dict) {
  const Occ = dict[Ids];
  if (!newDict[Occ]) newDict[Occ] = []
  newDict[Occ].push(Ids)
};
console.log(newDict);
