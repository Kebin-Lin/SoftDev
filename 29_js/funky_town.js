//Team BoLin Green -- Kevin Lin & Bo Hui Lu
//SoftDev1 pd6
//K28 -- Sequential Progression II: Electric Boogaloo...
//2018-12-20

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
  };
  console.log(b);
  return b;
};

var gcd = function(a,b) {
  while (a != b) {
    if (a > b) a -= b;
    else b -= a;
  };
  console.log(a);
  return a;
};

var students = ["Kevin","Thomas","Angela","Sophia"];

var randomStudent = function() {
  var result = students[Math.floor(Math.random() * students.length)];
  console.log(result);
  return result;
};

var fibButton = function() {
  var result = fibonacci(3);
  //Replaces whatever text is inside fibResult with the new result
  document.getElementById("fibResult").innerHTML = result;
};

var gcdButton = function() {
  var result = gcd(3,6);
  //Replaces whatever text is inside gcdResult with the new result
  document.getElementById("gcdResult").innerHTML = result;
};

var randButton = function() {
  var result = randomStudent();
  //Replaces whatever text is inside randResult with the new result
  document.getElementById("randResult").innerHTML = result;
}

//Button elements
var fibButt = document.getElementById("fib");
var gcdButt = document.getElementById("gcd");
var randButt = document.getElementById("rand");

//Listeners for elements
fibButt.addEventListener('click', fibButton);
gcdButt.addEventListener('click', gcdButton);
randButt.addEventListener('click', randButton);
