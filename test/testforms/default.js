function getElementByEvent(evt){
  return evt.srcElement;
}

function getNameByEvent(evt){
  return getElementByEvent(evt).getAttribute('name');
}


function logMessage(message) {
  var log = document.getElementById('log');
  var item = document.createElement('PARAGRAPH');
  var br = document.createElement('BR');

  item.innerText = message;

  log.appendChild(item);
  log.appendChild(br);
}

function logChange(evt, suffix='') {
  var name = getNameByEvent(evt);
  var message = name + ':' + evt.type + suffix;
  logMessage(message);
}

function logClick(evt) {
  logChange(evt);
}

function logTextChange(evt){
  var value = getElementByEvent(evt).value;
  logChange(evt, suffix='->'+value);
}

function logSelectChange(evt) {
  var value = getElementByEvent(evt).selectedOptions[0].innerText;
  logChange(evt, suffix='->'+value);
}



function addLogger(element, eventType, callback, suffix=''){
  var name = element.getAttribute('name');
  var message = name + ':' + eventType + suffix;
  window.autoform_tests.push(message);
  element.addEventListener(eventType, callback)
}

function addClickLogger(element) {
  addLogger(element, 'click', logClick);
}

function addTextLogger(element, testValue){
  addLogger(element, 'change', logTextChange, suffix='->'+testValue);
}

function addSelectLogger(element, testValue){
  addLogger(element, 'change', logSelectChange, suffix='->'+testValue);
}



function validate(){
  var requiredLogItems = window.autoform_tests;
  //console.log(requiredLogItems);
  var log = document.getElementById('log');

  var numChildren = log.children.length;
  var logItems = [];

  for (var i=0; i<numChildren; i+=2){
    logItems.push(log.children[i].innerText);
  }

  var numLogged = logItems.length;
  var numRequired = requiredLogItems.length;
  var completed = [];

  for (var i=0; i<numRequired; i++){
    for (var j=0; j<numLogged; j++){
      if (requiredLogItems[i] == logItems[j]){
        completed.push(requiredLogItems[i]);
      }
    }
  }

  var numCompleted = completed.length;
  var progress = numCompleted / numRequired;
  var progressCents = progress * 100;

  //console.log('Completed (' +  progressCents + ' %): ' + numCompleted + ' of ' + numRequired);

  var isValid = (numCompleted >= numRequired);

  return isValid;
}
