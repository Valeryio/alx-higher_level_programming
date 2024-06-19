#!/usr/bin/node

exports.esrever = function (list) {
  for (let i = 0; i < list.length / 2; i++) {
    let tmp = 0;
    tmp = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = tmp;
  }
  return list;
};
