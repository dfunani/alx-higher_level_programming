#!/usr/bin/node
const dict = require('./101-sorted.js').dict;
const res = {};
for (const key in dict) {
  if (!res[dict[key]]) {
    res[dict[key]] = [];
  }
  res[dict[key]].push(key);
}
console.log(res);
