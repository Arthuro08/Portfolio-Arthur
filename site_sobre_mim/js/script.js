const btn = document.getElementById("btnTop")
btn.addEventListener("click", function () {
    window.scrollTo(0, 0)
})

document.addEventListener("scroll", ocultar)

function ocultar() {
    if (window.scrollY > 10) {
        btn.style.display = "flex"
    } else {
        btn.style.display = "none"
    }
}

ocultar()

const sr = ScrollReveal({delay: 200, origin:'bottom', distance: '60px'});
sr.reveal('.principal', {reset: false});
sr.reveal('.trajetoria', {delay: 100, reset: true});
sr.reveal('.grafico', {delay: 100, reset: true});

