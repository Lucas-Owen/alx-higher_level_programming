#!/usr/bin/node
exports.logMe = (function (count) {
  return function (arg) {
    console.log(count++ + ': ' + arg);
  };
}(0));
