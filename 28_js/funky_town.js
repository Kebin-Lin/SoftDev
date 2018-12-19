//Team Centigrade -- Kevin Lin and Thomas Lee
//SoftDev1 pd6
//K28 -- Sequential Progression
//2018-12-19

var fibonacci = function(n) {
  if (n < 2) return n;
  var a = 0;
  var b = 1;
  var temp;
  while (n > 1) {
    temp = b;
    b = a + b;
    a = temp;
    n--;
  }
  return b;
}

var gcd = function(a,b) {
  if (a == b) return a;
  else if (a > b) return gcd(a-b,b);
  else return gcd(b-a,a);
}

var students = ["Kevin","Thomas","Angela","Sophia"];

var randomStudent = function() {
  return students[Math.floor(Math.random() * students.length)];
}
