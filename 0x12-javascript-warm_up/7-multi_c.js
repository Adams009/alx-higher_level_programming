#!/usr/bin/node

const arg = process.argv[2];

const first = parseInt(arg);

let i;

if (!isNaN(first)) {
  for (i = 0; i < first; i++) {
  console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
