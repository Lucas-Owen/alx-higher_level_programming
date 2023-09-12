#!/usr/bin/node

const { readFile, writeFile } = require('fs');

const argv = require('process').argv;

if (argv.length === 5) {
  const fileA = argv[2];
  const fileB = argv[3];
  const fileC = argv[4];

  readFile(fileA, (errA, dataA) => {
    if (errA) {
      throw errA;
    }
    readFile(fileB, (errB, dataB) => {
      if (errB) {
        throw errB;
      }
      writeFile(fileC, dataA.toString() + dataB.toString(), (err) => { throw err; });
    });
  });
}
