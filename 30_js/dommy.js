//Team Centigrade -- Kevin Lin and Thomas Lee
//SoftDev1 pd6
//K28 -- Sequential Progression III: Season of the Witch
//2018-12-21

var addToList = function() {
  var theList = document.getElementById("thelist"); //List of words
  var newElm = document.createElement("li"); //New element to be inserted
  newElm.innerHTML = "WORD"; //Changes element to say WORD
  theList.appendChild(newElm); //Adds the element to the list
  addListElmListeners(newElm); //Adds listeners for the element
};

var addFib = function() {
  var fibList = document.getElementById("fiblist"); //Fibonacci number list
  var newElm = document.createElement("li"); //New element to be added
  var result;
  var children = fibList.children //List of elements already in the list
  if (children.length < 2) result = 1; //First two numbers of sequence
  //Adds previous two numbers for next number of the sequence
  else result = parseInt(children[children.length - 1].innerHTML) + parseInt(children[children.length - 2].innerHTML);
  newElm.innerHTML = result; //Changes element to the result
  fibList.appendChild(newElm); //Adds element to the list
};

var addListElmListeners = function(elm) {
  //Listener for changing the title to the element content
  elm.addEventListener('mouseover',
    function() {
      changeTitle(elm.innerHTML);
    });
  //Listener to reverting to Hello World!
  elm.addEventListener('mouseout', resetTitle);
  //Listener to delete element when clicked
  elm.addEventListener('click',
    function() {
      elm.remove();
      resetTitle();
    });
};

//Changes title based on string input
var changeTitle = function(newTitle) {
  var header = document.getElementById("h");
  header.innerHTML = newTitle;
};

//Resets title to Hello World!
var resetTitle = function() {
  var header = document.getElementById("h");
  header.innerHTML = "Hello World!";
};

//Button vars
var b = document.getElementById("b");
var fb = document.getElementById("fb");

//Button listeners
b.addEventListener("click", addToList);
fb.addEventListener('click', addFib);

//Children list
var listChildren = document.getElementById('thelist').children;
console.log(listChildren);

//Adds listeners for already existing items
var i;
for (i = 0; i < listChildren.length; i++) {
  addListElmListeners(listChildren[i]);
};
