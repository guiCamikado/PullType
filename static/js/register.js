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
    } else if (passwordValue !== passwordVerificationValue){
        password.style.border = '2px solid red';
        passwordVerification.style.border = '2px solid red';
        sweetAlertProblem("Passwords must be equal");
    } else {
        submitRegistration()
    }
}

function submitRegistration(event) {
    console.log("Fetch enviado via front");
    
    event.preventDefault(); // Impede o comportamento padrão do form

    const form = document.querySelector("form");
    const inputs = form.querySelectorAll(".input");

    const data = {
        usuario: inputs[0].value,
        email: inputs[1].value,
        nome: inputs[2].value,
        sobrenome: inputs[3].value,
        senha: inputs[4].value,
        confirmarSenha: inputs[5].value,
        dataNascimento: inputs[6].value,
        termosAceitos: document.getElementById("read-and-accepted").checked
    };

    fetch("/DBAction/sendRegistrationRequest", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => {
        if (res.ok) {
            alert("Conta criada com sucesso!");
            form.reset();
        } else {
            return res.json().then(err => {
                throw new Error(err.message || "Erro ao criar conta.");
            });
        }
    })
    .catch(err => {
        alert("Erro: " + err.message);
    });
}

function sweetAlertProblem(problema) {
    Swal.fire({
        icon: "error",
        text: problema,
    });
}