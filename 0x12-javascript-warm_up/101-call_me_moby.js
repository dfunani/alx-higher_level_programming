#!/usr/bin/node
// script that prints “Javascript is amazing”
exports.callMeMoby = function (x, myFunction) {
  for (let i = 0; i < x; i++) {
    myFunction();
  }
}
