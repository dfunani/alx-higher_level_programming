#!/usr/bin/node

exports.addMeMaybe = function (number, myFunction) {
  myFunction(number += 1);
}
