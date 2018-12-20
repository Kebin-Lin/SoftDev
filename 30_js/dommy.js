var addToList = function() {
  var theList = document.getElementById("thelist");
  var newElm = document.createElement("li");
  newElm.innerHTML = "WORD";
  theList.appendChild(newElm);
  addTitleChanger(newElm);
};

var addFib = function() {
  var fibList = document.getElementById("fiblist");
  var newElm = document.createElement("li");
  var result;
  var children = fibList.children
  if (children.length < 2) result = 1;
  else result = parseInt(children[children.length - 1].innerHTML) + parseInt(children[children.length - 2].innerHTML);
  newElm.innerHTML = result;
  fibList.appendChild(newElm);
};

var addTitleChanger = function(elm) {
  elm.addEventListener('mouseover',
    function() {
      changeTitle(elm.innerHTML);
    });
  elm.addEventListener('mouseout', resetTitle)
};

var changeTitle = function(newTitle) {
  var header = document.getElementById("h");
  header.innerHTML = newTitle;
};

var resetTitle = function() {
  var header = document.getElementById("h");
  header.innerHTML = "Hello World!";
};

var b = document.getElementById("b");
var fb = document.getElementById("fb");

b.addEventListener("click", addToList);
fb.addEventListener('click', addFib);

var listChildren = document.getElementById('thelist').children;
console.log(listChildren);

var i;
for (i = 0; i < listChildren.length; i++) {
  addTitleChanger(listChildren[i]);
};
