#!/usr/bin/node

const size = 'Missing size';
if (isNaN(process.argv[2])) {
  console.log(size);
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    let res = '';
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
	    res += '*';
    }
    console.log(res);
  }
}
