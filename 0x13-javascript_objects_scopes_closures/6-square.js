#!/usr/bin/node

const SquareParent = require('./5-square');

module.exports = class Square extends SquareParent {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let line = '';
    for (let i = 0; i < this.width; i++) {
      line += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
};
