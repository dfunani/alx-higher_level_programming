#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let res = '';
      for (let j = 0; j < this.width; j++) {
        res += 'X';
      }
      console.log(res);
    }
  }
};
