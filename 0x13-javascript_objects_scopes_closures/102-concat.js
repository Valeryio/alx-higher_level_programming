#!/usr/bin/node

// This program open two files and concat their content

const process = require('process');
const fs = require('fs');

try {
  const dataFileA = fs.readFileSync(process.argv[3], 'utf8');
  const dataFileB = fs.readFileSync(process.argv[2], 'utf8');
  const data = dataFileA + dataFileB;
  try {
    fs.writeFileSync(process.argv[4], data);
  } catch (err) {
    console.log('Writing Error');
  }
} catch (err) {
  console.log('Reading Error');
}
