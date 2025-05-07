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

function changesShowHideButton(par) {

}