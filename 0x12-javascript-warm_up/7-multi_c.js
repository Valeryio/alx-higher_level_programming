#!/usr/bin/node

const process = require('process');

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurences');
}  else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
