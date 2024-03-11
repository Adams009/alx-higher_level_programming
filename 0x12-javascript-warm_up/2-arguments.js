#!/usr/bin/node

const myargs = process.argv.slice(2);

if (myargs.length === 0) {
  console.log('No argument');
} else if (myargs.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
