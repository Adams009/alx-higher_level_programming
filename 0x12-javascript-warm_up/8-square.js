#!/usr/bin/node

const arg = process.argv[2];

const first = parseInt(arg);

let i;

if (isNaN(first)) {
  console.log('Missing size');
} else {
  for (i = 0; i < first; i++) {
    console.log('X'.repeat(first));
  }
}
