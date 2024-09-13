const btnHide = (check) => {
  if (check) {
    if (!document.querySelector("#btn").classList.contains("disabled")) {
        document.querySelector("#btn").classList.add("disabled");
    }
} else {
    if (document.querySelector("#btn").classList.contains("disabled")) {
        document.querySelector("#btn").classList.remove("disabled");
    }
  }
};
const checkPhone = () => {
  let value = document.querySelector("#phone").value;
  if (value.length !== 10) {
    document.querySelector("#warning1").innerText =
      "Phone Number is not valid!";
    btnHide(true);
} else {
    document.querySelector("#warning1").innerText = "";
  }
};

const checkAccNo = () => {
  let value1 = document.getElementById("account_number").value;
  let value2 = document.getElementById("caccount_number").value;
  if (value1 !== value2 && value1 !== "" && value2 !== "") {
    document.querySelector("#warning2").innerText =
      "Account Number is not matched!";
    document.querySelector("#warning3").innerText =
      "Account Number is not matched!";
    btnHide(true);
  } else {
    document.querySelector("#warning2").innerText = "";
    document.querySelector("#warning3").innerText = "";
  }
};
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

const checkPercentage = (id, warningId) => {
  let value = document.getElementById(id).value;
  if ((parseInt(value) <= 100 && parseInt(value) >= 0) || value === "") {
    document.getElementById(warningId).innerText = "";
  } else {
    document.getElementById(warningId).innerText = "Percentage is invalid!";
    btnHide(true);
  }
};
