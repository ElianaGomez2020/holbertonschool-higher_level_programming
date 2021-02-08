#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  const lis = [];
  let a = 0;
  for (i = list.length; i > 0; i--) {
    lis[a] = list[i - 1];
    a++;
  }
  return (lis);
};
