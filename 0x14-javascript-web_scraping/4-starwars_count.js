#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const filmData = JSON.parse(body).results;
    let count = 0;
    for (const filmIndex in filmData) {
      const filmChar = filmData[filmIndex].charaters;
      for (const charIndex in filmChar) {
        if (filmChar[charIndex].includes('18')) {
	  count++;
	}
      }
    }
    console.log(count);
  } else {
    console.log('An error occured');
  }
})
