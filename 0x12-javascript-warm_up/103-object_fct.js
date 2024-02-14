#!/usr/bin/node
// increments function value
const myObject = {

    type: 'object',
    value: 12
  };
  console.log(myObject);
  myObject.incr = function () {
    this.value++;
  };
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);
  myObject.incr();
  console.log(myObject);


  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