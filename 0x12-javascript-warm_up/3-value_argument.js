#!/usr/bin/node

const process = require('process');
let i = 2;

if (process.argv.length < 3) {
  console.log("No argument");
}
else {
	while (process.argv[i] != undefined)
	{
		console.log(process.argv[i]);
		i++;
	}
}
