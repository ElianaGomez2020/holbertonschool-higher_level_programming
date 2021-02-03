#!/usr/bin/node

let arg = parseInt(process.argv[2]);

if (isNaN(arg)){
    console.log('Missing size');
} else {
    for (let x = 0; x < arg; x++){
        console.log('X'.repeat(arg));
    }
}
