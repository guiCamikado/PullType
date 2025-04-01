function openLogin() { // faz aparecer a login de login
    let login = document.getElementById('loginpopup')
    let register = document.getElementById('registerpopup')

    if (login.style.display === "none") {
        console.log("logNone");

        login.style.display = "block"
        register.style.display = "none"

    } else if (login.style.display === "block") {
        console.log("logBlock");

        login.style.display = "none"
        register.style.display = "none"
    }
}

function openRegister() { // faz aparecer a login de login
    let login = document.getElementById('loginpopup')
    let register = document.getElementById('registerpopup')
    console.log(login);

    if (register.style.display === "none") {
        register.style.display = "flex"
        login.style.display = "none"
    } else if (register.style.display === "flex") {
        register.style.display = "none"
        login.style.display = "none"
    }
}

function closeLoginAndRegister() {
    let login = document.getElementById('loginpopup')
    let register = document.getElementById('registerpopup')

    if (register.style.display === "flex") {
        register.style.display = "none"
        login.style.display = "none"
    }

    if (login.style.display === "block") {

        login.style.display = "none"
        register.style.display = "none"
    }
}

function goToMainPage() {
    const baseUrl = window.location.origin + '/';
    const mainUrl = 'index.html';
    
    window.location.href = mainUrl;
}

includeTopMenuHTMLAjax()
function includeTopMenuHTMLAjax() {
    var z, i, element, file, xhttp;
    z = document.getElementsByTagName("*");
    for (i = 0; i < z.length; i++) {
        element = z[i];
        file = element.getAttribute("topMenu");
        if (file) {
            xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4) {
                    if (this.status == 200) { element.innerHTML = this.responseText; }
                    if (this.status == 404) { element.innerHTML = this.responseText; }

                    // if (this.status == 404) { element.innerHTML = "Page not found. =("; }
                    element.removeAttribute("topMenu");
                    includeTopMenuHTMLAjax();
                }
            }
            xhttp.open("GET", file, true);
            xhttp.send();
            return;
        }
    }
}
