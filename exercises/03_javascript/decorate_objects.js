function addPersonMethods(input){
  var person = {
    name : input.name,
    age  : input.age,
    greet : function(greetingString){
      console.log (greetingString + ", my name is "+this.name);
    },
    compareAge : function(otherObject){
      if( this.age < otherObject.age ){
        console.log("My name is "+this.name+ " and I'm younger than "+otherObject.name);
      }
      if( this.age > otherObject.age ){
        console.log("My name is "+this.name+ " and I'm older than "+otherObject.name);
      }
      if( this.age == otherObject.age ){
        console.log("My name is "+this.name+ " and I'm equally young as "+otherObject.name);
      }
    },
    namesake:function(anotherPersonObject){
      if (this.name === anotherPersonObject.name){
        console.log("We have the same name, "+anotherPersonObject.name+" and I!");
      } else{
        console.log("We have different names, "+anotherPersonObject.name+" and I.");
      }
    }
  };
  return person;
}
