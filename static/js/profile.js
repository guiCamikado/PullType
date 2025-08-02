async function getCurrentLink() {
    try {
        await navigator.clipboard.writeText(window.location.href);
        alert("Link copiado para a área de transferência!");
    } catch (err) {
        alert("Erro ao copiar link: " + err);
    }
}

async function goToProfileEditor() {
    window.location.replace("/profileEdit");
}