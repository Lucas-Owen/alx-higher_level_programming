#!/usr/bin/node
const request = require('request');
const argv = require('process').argv;
const url = argv[2];

if (url) {
  request.get(url, { json: true }, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    if (response.statusCode === 200) {
      const films = body.results.filter((film => film.characters.some(link => link.endsWith('/18/'))))
      console.log(films.length);
    } else {
      console.log('request not successful');
    }
  });
} else {
  console.log('No movie id supplied');
}
