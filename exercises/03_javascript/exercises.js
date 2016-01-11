function keywordusage(text, keywords){
    var result = [];
    var words = text.split(" ");
    for (var i = 0; i < keywords.length; i++) {
        eachResult = false;
        for (var j = 0; j< words.length; j++) {
          if (keywords[i] === words[j]){
            eachResult = true;
            break;
          }
        }
        result.push(eachResult);
      //Do something
    }
    return result;
}

function frequencies(text, wordlist){
  var result = new Object();
  var count = 0;
  for (var i = 0; i< wordlist.length; i++) {
    var attr = wordlist[i];
    count = (text.match(new RegExp(attr,'g')) || []).length;
    result[attr] = count;
  }
  return result;
}

function rotate(inputArray,steps){
  if(typeof steps === "undefined"){
    steps = 1;
  }
  var tmp;
  if ( steps > 0){
    for (var i=0; i<steps; i++){
      tmp = inputArray.pop();
      inputArray.unshift(tmp);
    }
  }
  else if (steps < 0 ){
    for (var j=0; j>steps; j--){
      tmp = inputArray.shift();
      inputArray.push(tmp);
    }
  }
  return inputArray;
}
