function handleError(id, isError) {
    let inputElem = document.getElementById(id);
    let errorElem = document.getElementById('error-'+id);
    if (isError) {
        inputElem.style.borderBottomColor = "red";
        errorElem.style.display = "inline";
    }
    else {
        inputElem.style.borderBottomColor = "#8d09b2";
        errorElem.style.display = "none";
    }
}

function validateName() {
    let name = document.getElementById('fullName').value;
    //if name contains whitespace or special chars or numbers
    let patternMatch = Boolean(name.match(/[^\w\s]|[0-9]/g)); //if name's value matches this regex
    // if name is empty OR pattern matches
    let condition = name == "" || patternMatch;

    handleError('fullName', condition);   // handles error when second parameter is true, i.e, if name matches
    return !condition; // return if name matches (i.e. return if it matches when not supposed to)
}

function validateUsername() {
    let username = document.getElementById('username').value;
    // if name contains whitespace or anything special symbols except '.' and '-'
    let patternMatch = Boolean(username.match(/[^\w\S]|[^.-\w]/g));
    let condition =  username=="" || patternMatch;
    handleError('username', condition);
    return !condition;
}

function validatePassword() {
    let pass = document.getElementById('password').value;
    // if any special character (spaces, tabs)
    let patternMatch = Boolean(pass.match(/[\s]/g));
    let condition = pass == "" || patternMatch;
    handleError('password', condition);
    return !condition;
}

function validateEmail() {
    let email = document.getElementById('email').value;
    let patternMatch = Boolean(email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/));
    let condition = email == '' || !patternMatch;
    handleError('email',condition);
    return !condition;
}

function validateMatch(originalId) {
    let originalValue = document.getElementById(originalId).value;
    let confirmValue = document.getElementById("confirm-"+originalId).value;
    handleError('confirm-'+originalId, originalValue!=confirmValue);
    return originalValue == confirmValue;
}

function validatePhone() {
    let phone = document.getElementById('phoneNumber').value;
    // if everything except first character is a number or a space
    let patternMatch = Boolean(phone.substr(1).match(/[^\d ]/g));
    // if phone is empty OR phone doesnt include + OR doesnt match pattern OR phone number has less than 8 digits
    let condition = phone == '' || !phone.includes('+') || patternMatch || phone.replace(/\s/g,'').length < 12;
    handleError('phoneNumber', condition);
    return !condition;
}

function validateCreditNum() {
    let creditNum = document.getElementById('creditNum').value;
    let pureCreditNum = creditNum.replace(/\s/g, '');
    let condition = creditNum == "" || isNaN(pureCreditNum) || pureCreditNum.length != 16;
    handleError('creditNum', condition);
    return !condition;
}

function validateExpiry() {
    let expiryDate = document.getElementById('expDate').value;
    let condition = expiryDate == "" || (parseInt(expiryDate.substr(0,4)) < 2024);
    handleError('expDate', condition);
    return !condition;
}

function validateCVV() {
    let cvv = document.getElementById('CVV').value;
    let condition = cvv.length != 3 && cvv.length != 4;
    handleError('CVV', condition);
    return !condition;
}

function validateBuildingNo() {
    let buildingNo = document.getElementById('buildingNo').value;
    let condition = buildingNo == "" || isNaN(buildingNo);
    handleError('buildingNo', condition);
    return !condition;
}

function validateStreet() {
    let street = document.getElementById('street').value;
    let condition = street == "";
    handleError('street', condition);
    return !condition;
}

function validateDate() {
    let date = document.getElementById('dateOfBirth').value;
    let condition = date === '' ||  !(parseInt(date.substr(0,4)) < 2024);
    handleError('dateOfBirth',condition);
    return !condition;
}

function validateMessage() {
    let message = document.getElementById('message').value;
    let condition = message == "";
    handleError('message', condition);
    return !condition;
}

// For Subscribe Page

function validateRegistration() {
    return validateName() && validateUsername() && validatePassword() && validateMatch('password') &&
    validateEmail() && validateMatch('email') && validatePhone() && validateDate() &&
    validateCreditNum() && validateExpiry() && validateCVV() &&
    validateStreet() && validateBuildingNo();
}

// For Contact Us Page

function validateContactField() {
    return validateName() && validateEmail() && validatePhone() && validateMessage();
}