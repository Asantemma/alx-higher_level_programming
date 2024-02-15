#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let count = 0;
    list.forEach((ocur) => {
      if (ocur === searchElement) count++;
    });
    return count;
};