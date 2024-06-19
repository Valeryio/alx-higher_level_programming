#!/usr/bin/node

const dict = require('./101-data').dict;

let newObj;
let length = Object.keys(dict).length;
let i = 0;

console.log(dict, length);
for (const property in dict) {
  let newList = [];
  for (const newProperty in dict.slice(i)) {
    if (dict[property] === dict[newProperty]) {
      newList.push(newProperty);
    }
	    console.log(newList);
  }
  newObj[dict[i]] = newList;
}

console.log(newObj);
