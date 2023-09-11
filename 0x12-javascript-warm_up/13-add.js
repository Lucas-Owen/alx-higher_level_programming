#!/usr/bin/node

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  a = parseInt(a);
  b = parseInt(b);
  return a + b;
}

exports.add = add;
