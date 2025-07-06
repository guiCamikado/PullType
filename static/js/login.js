// showHideInput
// showHideIcon

document.addEventListener('click', function (event) {
    if (event.target.id === "showHideIcon") {
        var iconSrc = event.target.src;
        if (iconSrc.includes("hide.png")) {
            event.target.src = "images/show.png";
            document.getElementById("showHideInput").type = "text";
        } else {
            event.target.src = "images/hide.png";
            document.getElementById("showHideInput").type = "password";
        }
    }
});

async function submitLogin(event) {
    event.preventDefault(); // Impede o comportamento padrão do form

    const form = document.querySelector("form");
    const inputs = form.querySelectorAll(".input");


    const data = {
        login: inputs[0].value,
        senha: inputs[1].value,
    };

    fetch("/DBAction/sendLoginRequest", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(res => {
        console.log(res.success);
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