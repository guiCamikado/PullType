// showHideInput
// showHideIcon

document.addEventListener('click', function(event) {
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

function submitLogin(event) {
    console.log("Fetch enviado via front");
    
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
    .then(res => {
        if (res.ok) {
            alert("Ok!");
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