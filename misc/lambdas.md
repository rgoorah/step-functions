exports.handler = (event, context, callback) => {
    // Create a support case using the input as the case ID, then return a confirmation message   
   var myCaseID = event.inputCaseID;
   var myMessage = "Case " + myCaseID + ": opened...";   
   var result = {Case: myCaseID, Message: myMessage};
   callback(null, result);    
};

exports.handler = (event, context, callback) => {    
    // Assign the support case and update the status message    
    var myCaseID = event.Case;    
    var myMessage = event.Message + "assigned...";    
    var result = {Case: myCaseID, Message: myMessage};
    callback(null, result);        
};

exports.handler = (event, context, callback) => {    
    // Generate a random number to determine whether the support case has been resolved, then return that value along with the updated message.
    var min = 0;
    var max = 1;    
    var myCaseStatus = Math.floor(Math.random() * (max - min + 1)) + min;
    var myCaseID = event.Case;
    var myMessage = event.Message;
    if (myCaseStatus == 1) {
        // Support case has been resolved    
        myMessage = myMessage + "resolved...";
    } else if (myCaseStatus == 0) {
        // Support case is still open
        myMessage = myMessage + "unresolved...";
    } 
    var result = {Case: myCaseID, Status : myCaseStatus, Message: myMessage};
    callback(null, result); 
};

exports.handler = (event, context, callback) => {    
    // Escalate the support case 
    var myCaseID = event.Case;    
    var myCaseStatus = event.Status;    
    var myMessage = event.Message + "escalating.";    
    var result = {Case: myCaseID, Status : myCaseStatus, Message: myMessage};
    callback(null, result);
};

exports.handler = (event, context, callback) => { 
    // Close the support case    
    var myCaseStatus = event.Status;    
    var myCaseID = event.Case;    
    var myMessage = event.Message + "closed.";    
    var result = {Case: myCaseID, Status : myCaseStatus, Message: myMessage};
    callback(null, result);
};
