#!/usr/bin/node
const argv = require('process').argv;

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log(NaN);
    return;
  }
  a = parseInt(a);
  b = parseInt(b);
  console.log(a + b);
}

add(argv[2], argv[3]);
