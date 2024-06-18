#!/usr/bin/node

const process = require('process');

const i = 2;

if (process.argv.length < 3) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
