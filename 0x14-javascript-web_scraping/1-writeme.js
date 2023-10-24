#!/usr/bin/node
const argv = require('process').argv;
const fs = require('fs');

if (argv[3]) {
  fs.writeFile(argv[2], argv[3], (err) => {
    if (err) {
      console.error(err);
    }
  });
} else {
  console.log('Insufficient arguments supplied');
}
