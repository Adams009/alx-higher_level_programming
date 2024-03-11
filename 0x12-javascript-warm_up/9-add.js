#!/usr/bin/node

const argFt = process.argv[2];
const argSd = process.argv[3];

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

if (argFt === undefined || argSd === undefined || isNaN(argFt) || isNaN(argSd)) {
  console.log('NaN');
} else {
  const addNum = add(argFt, argSd);
  console.log(addNum);
}
