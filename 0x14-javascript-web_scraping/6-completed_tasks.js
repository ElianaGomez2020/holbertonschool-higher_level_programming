#!/usr/bin/node

const request = require('request');
const args = process.argv;
const todo = {};

request(args[2], function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    const bodyJ = JSON.parse(body);
    for (const i of bodyJ) {
      if (i.completed === true) {
        if (todo[i.userId]) {
          todo[i.userId] += 1;
        } else {
          todo[i.userId] = 1;
        }
      }
    }
  }
  console.log(todo);
});
