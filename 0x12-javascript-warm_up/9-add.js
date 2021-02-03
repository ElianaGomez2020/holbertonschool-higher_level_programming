#!/usr/bin/node

let arg = process.argv;

function add(a, b){
    return (parseInt(a) + parseInt(b));
}
console.log(add(process.argv[2], process.argv[3]));
