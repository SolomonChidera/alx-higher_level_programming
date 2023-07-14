#!/usr/bin/node

const fs = require('fs');
const fName = process.argv[2];
const data = process.argv[3];

fs.writeFile(fName, data, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
