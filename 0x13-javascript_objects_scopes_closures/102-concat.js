#!/usr/bin/node

// This program open two files and concat their content

const fs = require('fs');

try {
  const dataFileA = fs.readFileSync('./fileA', 'utf8');
  const dataFileB = fs.readFileSync('./fileB', 'utf8');
  const data = dataFileA + dataFileB;
  try {
    fs.writeFileSync('./fileC', data);
  } catch (err) {
      console.log('Writing Error');
  }
} catch (err) {
  console.log('Reading Error');
}
