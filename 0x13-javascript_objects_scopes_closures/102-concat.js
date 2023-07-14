#!/usr/bin/node

const fs = require('fs');

const fileOne = fs.readFileSync(process.argv[2], 'utf8');
const fileTwo = fs.readFileSync(process.argv[3], 'utf8');

fs.writeFileSync(process.argv[4], fileOne + fileTwo);
