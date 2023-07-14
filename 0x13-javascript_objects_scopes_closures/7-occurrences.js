#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(current => {
    if (current === searchElement) count++;
  });
  return count;
};
