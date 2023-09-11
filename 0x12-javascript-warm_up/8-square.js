#!/usr/bin/node
const argv = require('process').argv;

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(argv[2]);
  let line = '';
  for (let i = 0; i < size; i++) {
    line += 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(line);
  }
}
