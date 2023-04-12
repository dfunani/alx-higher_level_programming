#!/usr/bin/node

function factorial (a) {
  if (a <= 1) {
    return 1;
  }
  return a * factorial(a - 1);
}

if (!isNaN(process.argv[2])) {
  console.log(factorial(process.argv[2]));
}
