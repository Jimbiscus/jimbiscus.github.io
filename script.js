function nightmode() {
    var btn = document.querySelector("button");

    btn.style.backgroundColor = "green";

    if (btn.innerText === "MODE NUIT") {
        btn.innerText = "MODE JOUR";
        document.body.style.color = "black";
        document.body.style.backgroundColor = "#DCDCDC";
        
    }
    else if (btn.innerText === "MODE JOUR") {
        btn.innerText = "MODE NUIT";
        document.body.style.color = "white";
        document.body.style.backgroundColor = "#2B2C33";
    }


}
//
// function daymode() {
//    document.body.style.color = "black"
//    document.body.style.backgroundColor = "#DCDCDC"
// }
