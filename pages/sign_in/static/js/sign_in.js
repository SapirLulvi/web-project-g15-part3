
function checkValidMail(mail,note){
    const inpObj = document.getElementById(mail);
    if (!inpObj.checkValidity()) {
    document.getElementById(note).innerHTML = inpObj.validationMessage;
    }
}

function checkValidPass(pass,note){
    const inpObj = document.getElementById(pass);
    if (!inpObj.checkValidity()) {
    document.getElementById(note).innerHTML = inpObj.validationMessage;
    }
}




