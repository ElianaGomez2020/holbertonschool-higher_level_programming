#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let a = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      a = a + 1;
    }
  }
  return (a);
};
