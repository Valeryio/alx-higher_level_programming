#!/usr/bin/node

exports.converter = function (base) {
  return function (data, newBase = base) {
    return data.toString(newBase);
  };
};
