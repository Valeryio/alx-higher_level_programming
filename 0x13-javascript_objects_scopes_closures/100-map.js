#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map((item) => item * list.indexOf(item));
console.log(newList);