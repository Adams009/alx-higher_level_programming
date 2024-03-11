#!/usr/bin/node

let arg = process.argv.slice(2);

if (arg.length <= 1) {
  console.log(0);
} else {
  arg = arg.map(Number);
  arg.sort((a, b) => b - a);
  console.log(arg[1]);
}
