#!/usr/bin/node
// script that prints “Javascript is amazing”
if (isNaN(process.argv[2])) console.log(1);
else console.log(factorial(process.argv[2]));

function factorial (num) {
  if (num <= 1) return 1;
  else return num * factorial(num - 1);
}
