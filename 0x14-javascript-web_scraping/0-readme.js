#!/usr/bin/node
const argv = require('process').argv;
const fs = require('fs');

if (argv[2]) {
  fs.readFile(argv[2], 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
} else {
  console.log('No argument');
}
