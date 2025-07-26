// showHideInput
// showHideIcon

document.addEventListener('click', function (event) {
    if (event.target.id === "showHideIcon") {
        const icon = event.target;
        const showSrc = icon.dataset.showSrc;
        const hideSrc = icon.dataset.hideSrc;
        const input = document.getElementById("showHideInput");

        if (icon.src.includes("hide.png")) {
            icon.src = showSrc;
            input.type = "text";
        } else {
            icon.src = hideSrc;
            input.type = "password";
        }
    }
});

async function submitLogin(event) {
    event.preventDefault(); // Impede o comportamento padrão do form

    const form = document.querySelector("form");
    const inputs = form.querySelectorAll(".input");
    let rememberMe = document.getElementById("checkbox_input_camp")

    if (rememberMe.checked) {
        rememberMe = 'true'
    } else{
        rememberMe = 'false'
    }

    const data = {
        login: inputs[0].value,
        senha: inputs[1].value,
        rememberMe: rememberMe
    };
    console.log(data);
    

    fetch("/DBAction/sendLoginRequest", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(res => {
        if (res.success) {
            form.reset();
        } else {
            alert("Email ou Senha incorretos")
        }
    })
        .catch(err => {
            alert("Erro: " + err.message);
        });
}