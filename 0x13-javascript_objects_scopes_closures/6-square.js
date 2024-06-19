#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (symbol = 'X') {
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.height; j++) {
        process.stdout.write(symbol);
      }
      console.log('');
    }
  }
}

module.exports = Square;
