#!/usr/bin/node

const process = require('process');
const newArray = process.argv.slice(2, process.argv.length);

let bigNumber;

if (process.argv.length < 3) {
  console.log(0);
} else {
  bigNumber = newArray[0];
  for (let i = 1; i < newArray.length; i++) {
    if (bigNumber < newArray[i]) {
      bigNumber = newArray[i];
    }
  }
  console.log(bigNumber);
}
