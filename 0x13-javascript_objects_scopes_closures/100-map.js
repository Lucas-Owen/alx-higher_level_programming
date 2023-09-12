#!/usr/bin/node

const list = require('./100-data').list;

const result = list.map((value, index) => value * index);
console.log(list);
console.log(result);
