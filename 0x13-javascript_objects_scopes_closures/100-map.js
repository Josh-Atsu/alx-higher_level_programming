#!/usr/bin/node
const array = require('./100-data.js').list;
console.log(array);
const mapA = array.map((item, index) => item * index);
console.log(mapA);
