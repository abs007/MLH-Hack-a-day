var info = [0,0,0,0,0,0,0];
var result = 0;

function setAge(){
    info[0] = document.querySelector('#age').value;
}

function setSex(){
    info[1] = document.querySelector('input[name="sex"]:checked').value;
}

function setTrestbps(){
    info[2] = document.querySelector('#trestbps').value;
}

function setChol(){
    info[3] = document.querySelector('#chol').value;
}

function setFbs(){
    info[4] = document.querySelector('#fbs').value;
}

function setThalach(){
    info[5] = document.querySelector('#thalach').value;
}

function setExang(){
    info[6] = document.querySelector('input[name="exang"]:checked').value;
}

function predict(){
console.log('predicting');
$.ajax({
  type: "POST",
  url: "~/app.py",
  data: { param: info}
}).done(function( o ) {
   // do something
   result = o;
});
console.log('done predicting. Result: ' + result);
}