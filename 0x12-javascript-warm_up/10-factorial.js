#!/usr/bin/node

const process = require('process');
const x = parseInt(process.argv[2]);

function fact(x) {
  if (x === 0) {
    return 1;
  }
  return x * fact(x - 1);
}

if (x === undefined || isNaN(x)) {
  console.log(1);
} else {
  console.log(fact(x));
}
