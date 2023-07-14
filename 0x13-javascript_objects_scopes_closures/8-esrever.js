#!/usr/bin/node

exports.esrever = function (list) {
  const listReverse = list.map((_, index, arr) => arr[arr.length - 1 - index]);
  return listReverse;
};
