#!/usr/bin/node

const numBer = Math.trunc(process.argv[2]);

if (isNaN(numBer)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${numBer}`);
}
