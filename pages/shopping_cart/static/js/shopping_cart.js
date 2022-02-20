

function checkValidPhone(phoneNum,note){
    const inpObj = document.getElementById(phoneNum);
    if (!inpObj.checkValidity()) {
    document.getElementById(note).innerHTML = inpObj.validationMessage;
    }
}

// function onChangeFunction(formID,quantity ){
//     console.log("enter")
//     console.log(formID)
//     const inpObj = document.getElementById(quantity);
//     if (!inpObj.checkValidity()) {
//         if (typeof (inpObj)!="number"){
//             document.getElementById(note).innerHTML = inpObj.validationMessage;
//         }
//         else if (inpObj <= 0 ){
//             document.getElementById(note).innerHTML = "הסר מוצר מהסל בעזרת לחצן ההסרה";
//         }
//         else {
//             document.getElementById(note).innerHTML = "להזמנה מעל 9 יחידות צור קשר עם החנות";
//         }
//     }
//     else{
//         let text1 = "quantityForm";
//         let text2 = formID.toString();
//         let result = text1.concat(text2);
//         console.log(result)
//         var form = document.getElementById(result);
//         form.submit();
//     }
// }

function onChangeFunction(formID,quantity ){
    console.log("enter")
    console.log(formID)
    const inpObj = document.getElementById(quantity);
    if (!inpObj.checkValidity()) {
        document.getElementById(note).innerHTML = inpObj.validationMessage;
    }
    else {
        let text1 = "quantityForm";
        let text2 = formID.toString();
        let result = text1.concat(text2);
        console.log(result)
        var form = document.getElementById(result);
        form.submit();
    }
}
