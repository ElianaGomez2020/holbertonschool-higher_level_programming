#!/usr/bin/node
const request = require('request');
const args = process.argv;

request('https://swapi-api.hbtn.io/api/films/' + args[2], function (error, response, body) {
  if (error) {
    return console.error('code:', error);
  } else {
    // console.log('code:', response.statusCode);
    console.log(JSON.parse(body).title);
  }
});
