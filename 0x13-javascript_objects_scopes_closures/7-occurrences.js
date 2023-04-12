#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  if (!list || !searchElement) {
    return 0;
  } else {
    return list.filter((a) => a === searchElement).length;
  }
};
