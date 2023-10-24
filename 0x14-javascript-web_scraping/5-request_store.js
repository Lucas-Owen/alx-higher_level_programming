#!/usr/bin/node
const request = require('request');
const argv = require('process').argv;
const fs = require('fs');

if (argv[3]) {
  const url = argv[2];
  const filename = argv[3];

  request.get(url, (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    }
    if (response.statusCode === 200) {
      const content = new Uint8Array(Buffer.from(body));
      fs.writeFile(filename, content, (err) => {
        if (err) {
          console.error(err);
        }
      });
    } else {
      console.log('Request not successful');
    }
  });
} else {
  console.log('Insufficient arguments supplied');
}
