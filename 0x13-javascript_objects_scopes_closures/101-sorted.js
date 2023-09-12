#!/usr/bin/node
const dict = require('./101-data').dict;
const keys = Object.keys(dict);
const sorted = {};
for (let i = 0; i < keys.length; i++) {
  if (sorted[dict[keys[i]]]) {
    sorted[dict[keys[i]]].push(keys[i]);
  } else {
    sorted[dict[keys[i]]] = [keys[i]];
  }
}
console.log(sorted);
