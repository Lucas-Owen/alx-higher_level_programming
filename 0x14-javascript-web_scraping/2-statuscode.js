#!/usr/bin/node
const request = require('request');
const argv = require('process').argv;

if (argv[2]) {
  request.get(argv[2], (error, response, _) => {
    if (error) {
      console.error(error);
      return;
    }
    console.log('code: ' + response.statusCode);
  });
} else {
  console.log('No url supplied');
}
