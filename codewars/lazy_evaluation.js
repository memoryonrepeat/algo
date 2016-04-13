// http://www.codewars.com/kata/lazy-evaluation/javascript

function Lazy() {
  this.fns = [];
  
  this.add = function(){
    this.fns.push(Array.prototype.slice.call(arguments));
    return this;
  };
  
  this.invoke = function(){
    var currentVal = arguments[0];
    for (var i=0; i<this.fns.length; i++){
      var currentFn = this.fns[i][0];
      currentVal = currentFn.apply(currentFn,this.fns[i].slice(1).concat(currentVal));
    }
    return currentVal;
  }
  
}