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
      const completed = {};
      body.forEach((task) => {
        if (task.completed) {
          if (task.userId in completed) {
            completed[task.userId]++;
          } else {
            completed[task.userId] = 1;
          }
        }
      });
      console.log(completed);
    } else {
      console.log('request not successful');
    }
  });
} else {
  console.log('No url supplied');
}
