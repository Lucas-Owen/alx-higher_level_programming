#!/usr/bin/node
const argv = require('process').argv;

let biggest = Number.MIN_SAFE_INTEGER;
let secondBiggest = Number.MIN_SAFE_INTEGER;
let value;
if (argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    value = parseInt(argv[i]);
    if (value > biggest) {
      secondBiggest = biggest;
      biggest = value;
    } else if (value > secondBiggest) {
      secondBiggest = value;
    }
  }
  console.log(secondBiggest);
}
