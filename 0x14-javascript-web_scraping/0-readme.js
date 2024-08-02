#!/usr/bin/node
cmd_first = process.argv[2];
const fs = require('fs');
fs.readFile(cmd_first, 'utf8', (err, data) => {
if (err) {
console.log(err)
} else {
console.log(data)
}
});
