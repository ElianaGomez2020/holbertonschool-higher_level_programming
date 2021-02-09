#!/usr/bin/node
const request = require('request');
const args = process.argv;

request(args[2], function (error, response) {
  if (error) {
    return console.log('code:', error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
