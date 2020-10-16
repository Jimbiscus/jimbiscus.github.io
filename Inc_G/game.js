var score = 0;
var petardPrice = 15;
var petards = 0;
var hero = 0;
var heroPrice = 50;
document.getElementById("score").innerHTML = score;

function buyPetard() {
    if (score >= petardPrice) {
    score = score - 15;
    petards++;
    petardPrice = Math.round(petardPrice * 1.05);
    document.getElementById("score").innerHTML = score;
    document.getElementById("petards").innerHTML = petards;
    document.getElementById("petardPrice").innerHTML = petardPrice;
    updateScorePerSecond();
    }
    else {
    document.getElementById("info").innerHTML = "Vous n'avez plus d'argent !";
    setInterval(() => {
        document.getElementById("info").innerHTML = ""
        
    }, 2000);
    
    }
}
function buyHero() {
    if (score >= heroPrice) {
    score = score - 50;
    hero++;
    heroPrice = Math.round(heroPrice * 1.15);
    document.getElementById("score").innerHTML = score;
    document.getElementById("hero").innerHTML = hero;
    document.getElementById("heroPrice").innerHTML = heroPrice;
    updateScorePerSecond();
    }
    else {
    document.getElementById("info").innerHTML = "Vous n'avez plus d'argent !";
    
    }
}

function addToScore(n) {
    score = score + n;
    document.getElementById("score").innerHTML = score;
}
function updateScorePerSecond() {
    Scps = petards + hero*4
    document.getElementById("Scps").innerHTML = Scps;
}

setInterval(function() {
    score = score + petards;
    score = score + hero * 4;
    document.getElementById("score").innerHTML = score;
    document.title = score + " - Tzako Simulator"
}, 1000);