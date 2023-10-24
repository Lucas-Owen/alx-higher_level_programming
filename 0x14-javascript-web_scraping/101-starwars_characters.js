#!/usr/bin/node
const request = require('request');
const argv = require('process').argv;
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

function requestCharacter (url) {
  return new Promise((resolve, reject) => {
    request.get(url, { json: true }, (error, response, character) => {
      if (error || response.statusCode !== 200) {
        reject(error);
      } else {
        resolve(character.name);
      }
    });
  });
}

function requestFilm (url) {
  return new Promise((resolve, reject) => {
    request.get(url, { json: true }, (error, response, body) => {
      if (error) {
        reject(error);
      }
      if (response.statusCode === 200) {
        resolve(body);
      } else {
        console.log('request not successful');
        reject(error);
      }
    });
  });
}

async function main () {
  if (argv[2]) {
    try {
      const film = await requestFilm(apiUrl + argv[2]);
      for (let i = 0; i < film.characters.length; i++) {
        const charUrl = film.characters[i];
        const character = await requestCharacter(charUrl);
        console.log(character);
      }
    } catch (error) {
      console.error(error);
    }
  } else {
    console.log('No movie id supplied');
  }
}

main();
