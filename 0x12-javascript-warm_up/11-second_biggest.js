#!/usr/bin/node

const process = require('process');

let newArray = process.argv.slice(2);
let tmp;

if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 0; i < newArray.length; i++) {
    for (let j = 0; j < newArray.length - 1 - i; j++) { // Fixed the loop condition
      if (newArray[j] < newArray[j + 1]) {
        tmp = newArray[j];
        newArray[j] = newArray[j + 1];
        newArray[j + 1] = tmp;
      }
    }
  }
  console.log(newArray[1]);
}

