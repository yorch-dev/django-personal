setTimeout(function() {
    var messages = document.getElementsByClassName('alert');
    for (var i = 0; i < messages.length; i++) {
        messages[i].remove('show');
    }
}, 3000);

window.addEventListener('load', function() {
    var menuHeight = document.querySelector('.navbar').offsetHeight;
    document.querySelector('body').style.marginTop = menuHeight + 'px';
});

// Ajustar al redimensionar la ventana
window.addEventListener('resize', function() {
    var menuHeight = document.querySelector('.navbar').offsetHeight;
    document.querySelector('body').style.marginTop = menuHeight + 'px';
});