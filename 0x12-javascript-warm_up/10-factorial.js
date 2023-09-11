#!/usr/bin/node
const argv = require('process').argv;

function factorial (value) {
  const result = 1;
  if (isNaN(value)) return result;
  if (value === 1) return result;
  return value * factorial(value - 1);
}

console.log(factorial(parseInt(argv[2])));
