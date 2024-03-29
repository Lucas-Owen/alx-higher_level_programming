#!/usr/bin/node
const request = require('request');
const argv = require('process').argv;
const url = 'https://swapi-api.alx-tools.com/api/films/';

if (argv[2]) {
  request.get(url + argv[2], { json: true }, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    if (response.statusCode === 200) {
      console.log(body.title);
    } else {
      console.log('request not successful');
    }
  });
} else {
  console.log('No id supplied');
}
