#!/usr/bin/node
const argv = require('process').argv;
const fs = require('fs');

if (argv[3]) {
  const content = new Uint8Array(Buffer.from(body));
  fs.writeFile(argv[2], content, (err) => {
    if (err) {
      console.error(err);
    }
  });
} else {
  console.log('Insufficient arguments supplied');
}
