#!/usr/bin/node

const argument = process.argv.slice(2);
const firstArg = argument[0];

if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
