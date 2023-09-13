#!/usr/bin/node
// script that prints “Javascript is amazing”
if (isNaN(process.argv[2])) console.log('Missing size');
else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    let temp = '';
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      temp += 'x';
    }
    console.log(temp);
  }
}
