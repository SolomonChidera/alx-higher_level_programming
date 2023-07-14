#!/usr/bin/node

const dict = require('./101-data').dict;

const newDictOccurence = {};

for (const [key, value] of Object.entries(dict)) {
  if (newDictOccurence[value]) {
    newDictOccurence[value].push(key);
  } else {
    (newDictOccurence[value] = [key]);
  }
}

console.log(newDictOccurence);
