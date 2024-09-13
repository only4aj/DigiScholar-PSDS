
const PREVIOUS_YEAR = 30;
document.getElementById("date").max = `${new Date().getFullYear()}-12-31`;
document.getElementById("date").min = `${new Date().getFullYear() - PREVIOUS_YEAR}-12-31`;

// Next Button Disabled Function
const btnHide = (check) => {
    check ?
        document.querySelector("#btn").disabled = true :
        document.querySelector("#btn").disabled = false;
};

// Phone Number validation Check
const checkPhone = () => {
    let value = document.querySelector("#phone").value;
    if ((value.length !== 12 && value !== "") || !value.startsWith("91")) {
        document.querySelector("#warning1").innerText = "Phone Number is not valid!";
        btnHide(true);
    } else {
        document.querySelector("#warning1").innerText = "";
    }
};

// Check account number is same with confirm account number or not
const checkAccNo = () => {
    let value1 = document.getElementById("account_number").value;
    let value2 = document.getElementById("caccount_number").value;
    if (value1 !== value2 && value1 !== "" && value2 !== "") {
        document.querySelector("#warning2").innerText = "Account Number is not matched!";
        document.querySelector("#warning3").innerText = "Account Number is not matched!";
        btnHide(true);
    } else {
        document.querySelector("#warning2").innerText = "";
        document.querySelector("#warning3").innerText = "";
    }
};

// Check precentage value is valid or not
const checkPercentage = (id, warningId) => {
    let value = document.getElementById(id).value;
    if ((parseInt(value) <= 100 && parseInt(value) >= 0) || value === "") {
        document.getElementById(warningId).innerText = "";
    } else {
        document.getElementById(warningId).innerText = "Percentage is invalid!";
        btnHide(true);
    }
};

// Check Complete Form fill or not
const checkFillForm = () => {
    let inputGroup = Array.from(document.querySelectorAll(".form-control"));
    let check = false;
    for (let i in inputGroup) {
        if (inputGroup[i].value === "") {
            check = true;
            break;
        } else {
            check = false;
        }
    }
    btnHide(check);
};

// Extra checker for checking  error in every stage
const checker = () => {
    let inputgroup = Array.from(document.querySelectorAll(".form-control"));
    for (let i in inputgroup) {
        if (inputgroup[i].value !== "" && inputgroup[i].id === "phone") {
            checkPhone();
        }
        if (inputgroup[i].value !== "" && inputgroup[i].id === "10percentage") {
            checkPercentage("10percentage", "warning4");
        }
        if (inputgroup[i].value !== "" && inputgroup[i].id === "12percentage") {
            checkPercentage('12percentage', 'warning5');
        }
        if (inputgroup[i].value !== "" && inputgroup[i].id === "account_number") {
            checkAccNo();
        }
    }

}