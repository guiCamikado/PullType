const password = document.getElementById("password");
const passwordVerification = document.getElementById("password-confirmation");

password.addEventListener('input', function () { checkPasswordIsEven() });
passwordVerification.addEventListener('input', function () { checkPasswordIsEven() })

function checkPasswordIsEven() {
    const passwordValue = document.getElementById("password").value;
    const passwordVerificationValue = document.getElementById("password-confirmation").value;

    if (passwordValue.length < 8) {
        password.style.border = '2px solid red';
        passwordVerification.style.border = '2px solid red';
        console.log("password must be at least eigth (8) caracters Long");

    } else if (!/[A-Z]/.test(passwordValue)) {
        password.style.border = '2px solid red';
        passwordVerification.style.border = '2px solid red';
        console.log('Password must contain at least one uppercase letter');
        return;
    } else if (!/[a-z]/.test(passwordValue)) {
        password.style.border = '2px solid red';
        passwordVerification.style.border = '2px solid red';
        console.log('Password must contain at least one lowercase letter');
        return;
    } else if (!/[^A-Za-z0-9]/.test(passwordValue)) {
        password.style.border = '2px solid red';
        passwordVerification.style.border = '2px solid red';
        console.log('Password must contain at least one special character');
    } else if (passwordValue === passwordVerificationValue) {
        password.style.border = '2px solid green';
        passwordVerification.style.border = '2px solid green';
        console.log("Passwords are equal");
    } else {
        password.style.border = '2px solid red';
        passwordVerification.style.border = '2px solid red';
        console.log("Passwords must be equal");
    }
}

function checkPasswordIsEvenButton() {
    const passwordValue = document.getElementById("password").value;
    const passwordVerificationValue = document.getElementById("password-confirmation").value;

    if (passwordValue.length < 8) {
        password.style.border = '2px solid red';
        passwordVerification.style.border = '2px solid red';
        sweetAlertProblem("password must be at least eigth (8) caracters Long");

    } else if (!/[A-Z]/.test(passwordValue)) {
        password.style.border = '2px solid red';
        passwordVerification.style.border = '2px solid red';
        sweetAlertProblem('Password must contain at least one uppercase letter');
        return;
    } else if (!/[a-z]/.test(passwordValue)) {
        password.style.border = '2px solid red';
        passwordVerification.style.border = '2px solid red';
        sweetAlertProblem('Password must contain at least one lowercase letter');
        return;
    } else if (!/[^A-Za-z0-9]/.test(passwordValue)) {
        password.style.border = '2px solid red';
        passwordVerification.style.border = '2px solid red';
        sweetAlertProblem('Password must contain at least one special character');
    } else if (passwordValue === passwordVerificationValue) {
        password.style.border = '2px solid green';
        passwordVerification.style.border = '2px solid green';
    } else {
        password.style.border = '2px solid red';
        passwordVerification.style.border = '2px solid red';
        sweetAlertProblem("Passwords must be equal");
    }
}

function sweetAlertProblem(problema) {
    Swal.fire({
      icon: "error",
      text: problema,
    });
}
