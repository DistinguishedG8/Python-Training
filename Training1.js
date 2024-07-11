
// -> Opening comment
let test = "Hello World";

// -> Testing different methods of displaying data
console.log(test);
    /* -> Multi line comment
    ** -> window.alert(test);
    ** -> window.print(test);
    */

// -> Testing out a for loop, counts and adds 1 until 10
for (let steps = 1; steps <= 10; steps++){console.log(steps)};

// -> Testing functions
function testLog() {console.log(test)};

// -> Call the function
testLog();

// -> Testing multiple different variable types
let animal, is_Hungry, age;

animal = "dog"; // -> String type
is_Hungry = true; // -> Boolean
age = 12; // -> Number

// -> merging values into a string
console.log("My " + animal + " is " + age + " years old." + " But is he hungry? " + is_Hungry);
if (is_Hungry){console.log("My " + animal + " is Hungry!")};

// -> Requesting user input
let firstName = window.prompt("Firstname: ");
let lastName = prompt("Lastname: ");

// -> cannot modify const, it stays the same as declared
const testerVar = 0;

// -> Testing math :D
var add;
add = 3 + 1;
console.log(add);

// -> setting function to add values
function addTwo(a, b){ 
    test = a + b
    return test
};

// -> testing function
console.log(addTwo(3,1));
