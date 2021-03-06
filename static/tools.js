var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    document.getElementById("result").innerHTML = this.responseText;
    document.getElementById('result').scrollIntoView();
    $('[data-toggle="popover"]').popover({
      container: 'body'
    });
    var clipboard = new ClipboardJS('.close');
    if(document.getElementById("htmltext")){
       var myCodeMirror = CodeMirror.fromTextArea(document.getElementById("htmltext"), {mode: "text/html",theme: "monokai",readOnly:true,lineWrapping:true,viewportMargin:Infinity});
    }
  }
};
function autoCrypto(){
  xhttp.open("POST", "/autoCrypto", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  if(document.getElementById("ignore").checked){
    xhttp.send("text="+encodeURIComponent(document.getElementById("autoCryptotext").value)+"&ignore=1");
  }else{
    xhttp.send("text="+encodeURIComponent(document.getElementById("autoCryptotext").value));
  }
}
function caesar(i){
  xhttp.open("POST", "/caesar", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("text="+document.getElementById("ciphertext").value+"&n="+i);
}
function vigenere(encode=false){
  xhttp.open("POST", "/vigenere", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  var request = "text="+document.getElementById("vigeneretext").value+"&pass="+document.getElementById("vigenerepass").value;
  if(encode){
    request += "&encode=1";
  }
  xhttp.send(request)
}
function letternum(encode=false){
  seperator = encodeURIComponent(document.getElementById("letternumseperator").value);
  xhttp.open("POST", "/letternum", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  payload = "text="+encodeURIComponent(document.getElementById("letternumtext").value)
  if(encode){
    xhttp.send(payload+"&encode=1&seperator="+seperator);
  }else{
    xhttp.send(payload+"&seperator="+seperator);
  }
}
function base(x,encode=false){
  xhttp.open("POST", "/base"+x, true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  if(encode){
    xhttp.send("text="+document.getElementById("base"+x+"text").value+"&encode=1"); 
  }else{
    if (x == 85){
      xhttp.send("text="+encodeURIComponent(document.getElementById("base85text").value));
    }
    else{
      xhttp.send("text="+document.getElementById("base"+x+"text").value);      
    }
  }
}
function ascii85(encode=false){
  xhttp.open("POST", "/ascii85", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  var payload = "text="+encodeURIComponent(document.getElementById("ascii85text").value);
  if(encode){
    payload += "&encode=1"
  }
  xhttp.send(payload);
}
function rot47(){
  xhttp.open("POST", "/rot47", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("text="+document.getElementById("rot47text").value);
}
function xor(){
  xhttp.open("POST", "/xor", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  var text = encodeURIComponent(document.getElementById("xortext").value);
  var key = encodeURIComponent(document.getElementById("xorkey").value);
  xhttp.send("text="+text+"&selecttext="+document.getElementById("selecttext").innerHTML+"&key="+key+"&selectkey="+document.getElementById("selectkey").innerHTML);
}
function xorBrute(){
  xhttp.open("POST", "/xorBrute", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  var text = encodeURIComponent(document.getElementById("xortext").value);
  xhttp.send("text="+text+"&selecttext="+document.getElementById("selecttext").innerHTML);
}
function malbolge(){
  xhttp.open("POST", "/malbolge", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("text="+encodeURIComponent(document.getElementById("malbolgetext").value));
}
function clearMal(){
  document.getElementById("malbolgetext").value = "";
}
function decryptRSA(){
  document.getElementById("result").innerHTML = "<h3>Loading...</h3>"+
                                                '<div class="progress ht-tm-element" style="height:30px;">'+
                                                '<div class="progress-bar progress-bar-striped progress-bar-animated bg-success" role="progressbar" aria-valuemin="0" aria-valuemax="100" style="width: 100%"></div>' +
                                                '</div>'
  xhttp.open("POST", "/decryptRSAValues", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  var payload = "values="+encodeURIComponent(document.getElementById("values").value);
  let delta = document.getElementById("delta").value;
  let m = document.getElementById("m").value;
  if(delta){
    payload += "&delta=" + delta;
  }
  if(m){
    payload += "&m=" + m;
  }
  xhttp.send(payload);
}
function clearRSA(n){
  if(n <= 1){
    document.getElementById("n").value = "";
    document.getElementById("e").value = "";
    document.getElementById("c").value = "";
  }
  if(n >= 1){
    document.getElementById("values").value = "";
  }
}
function exampleRSA(){
  document.getElementById("values").value = "n = 0xdf93c950b2ce52b5\ne = 65537\nc = 4255952323097241533"
}
function clearXOR(){
  document.getElementById("xortext").value = "";
  document.getElementById("xorkey").value = "";
}
function morse(encode=false){
  seperator = encodeURIComponent(document.getElementById("seperator").value);
  xhttp.open("POST", "/morse", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  payload = "text="+encodeURIComponent(document.getElementById("morsetext").value)
  if(encode){
    xhttp.send(payload+"&encode=1&seperator="+seperator);
  }else{
    xhttp.send(payload+"&seperator="+seperator);
  }
}
function gcd(){
  xhttp.open("POST", "/gcd", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("a="+document.getElementById("a").value+"&b="+document.getElementById("b").value);
}
function clearGCD(){
  document.getElementById("a").value = "";
  document.getElementById("b").value = "";
}
function numbertoascii(){
  seperator = document.getElementById("numberseperator");
  format = document.getElementById("format");
  xhttp.open("POST", "/number_to_ascii", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  payload = "text="+document.getElementById("numbertext").value;
  xhttp.send(payload+"&seperator="+encodeURIComponent(seperator.options[seperator.selectedIndex].value)+"&mode="+format.options[format.selectedIndex].value);
}
$(document).ready(function(){
  $(".custom-file-input").on("change", function() {
    var fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
  });
});
function uploadFile(file){
  xhttp.setRequestHeader("Content-Type", "multipart/form-data");
  var formData = new FormData();
  formData.append("afile", file);
  xhttp.send(formData);
}
function ocr(){
  var afile = document.getElementById("customFile").files[0];
  xhttp.open("POST", "/ocr", true);
  uploadFile(afile)
}
/*function zsteg(){
  var afile = document.getElementById("customFile").files[0];
  xhttp.open("POST", "/zsteg", true);
  uploadFile(afile);
}
function jsteg(){
  var afile = document.getElementById("customFile").files[0];
  xhttp.open("POST", "/jsteg", true);
  uploadFile(afile);
}
function strings(){
  var afile = document.getElementById("customFile").files[0];
  xhttp.open("POST", "/strings", true);
  uploadFile(afile);
}
function stegsolve(){
  var afile = document.getElementById("customFile").files[0];
  xhttp.open("POST", "/stegsolve", true);
  uploadFile(afile);
}*/
function fernet(encode=false){
  xhttp.open("POST", "/fernet", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  payload = "text="+encodeURIComponent(document.getElementById("fernettext").value)+"&key="+encodeURIComponent(document.getElementById("fernetkey").value);
  if(encode){
    xhttp.send(payload+"&encode=1");
  }else{
    xhttp.send(payload);
  }
}
function webSource(){
  xhttp.open("POST","/webSource",true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("text="+encodeURIComponent(document.getElementById("urltext").value));
}
function pythonScript(){
  cm.save();
  xhttp.open("POST","/pythonScript",true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("text="+encodeURIComponent(document.getElementById("pythontext").value)+"&password="+document.getElementById("pythonpassword").value);
}
function clearPython(){
  document.getElementById("pythontext").value = "";
}
function hastad(){
  xhttp.open("POST","/hastad",true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("values="+encodeURIComponent(document.getElementById("hastadvalues").value));
}
function clearHastad(){
  document.getElementById("hastadvalues").value = "";
}
