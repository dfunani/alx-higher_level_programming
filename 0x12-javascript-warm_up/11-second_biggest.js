#!/usr/bin/node
// script that prints “Javascript is amazing”
if (process.argv.length <= 3) console.log(0);
else {
  const temp = process.argv.slice(2);
  temp.sort((a, b) => parseInt(b) - parseInt(a));
  console.log(temp[1]);
}
