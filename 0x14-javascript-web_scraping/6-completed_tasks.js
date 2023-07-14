#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }

  const todos = JSON.parse(body);
  const data = {};

  todos.forEach((todo) => {
    if (todo.completed && data[todo.userId] === undefined) {
      data[todo.userId] = 1;
    } else if (todo.completed) {
      data[todo.userId] += 1;
    }
  });

  console.log(data);
});
