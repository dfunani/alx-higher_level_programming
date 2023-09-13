#!/usr/bin/node
// script that prints “Javascript is amazing”
if (!isNaN(process.argv[2])) console.log('My number: ' + process.argv[2]);
else console.log('Not a number');
