#!/usr/bin/node

const sizeNum = Math.floor(Number(process.argv[2]));

if (isNaN(sizeNum)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < sizeNum; x++) {
    let row = '';
    for (let y = 0; y < sizeNum; y++) row += 'X';
    console.log(row);
  }
}
