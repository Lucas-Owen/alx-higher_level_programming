#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (!(isNaN(w) || isNaN(h) || parseInt(w) <= 0 || parseInt(h) <= 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let line = '';
    for (let i = 0; i < this.width; i++) {
      line += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
