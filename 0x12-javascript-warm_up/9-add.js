#!/usr/bin/node
// script that prints “Javascript is amazing”
if (isNaN(process.argv[2]) || isNaN(process.argv[3])) console.log('NaN');
else add(parseInt(process.argv[2]), parseInt(process.argv[3]));

function add (a, b) {
  console.log(a + b);
}
