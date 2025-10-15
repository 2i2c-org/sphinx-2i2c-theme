// Fix for sidebar toggle buttons.
// The parent theme only attaches to the first .primary-toggle button,
// but this theme has multiple buttons. This attaches to all of them.
document.addEventListener("DOMContentLoaded", function() {
    const checkbox = document.getElementById("pst-primary-sidebar-checkbox");
    document.querySelectorAll(".primary-toggle").forEach(function(btn) {
        btn.onclick = function() { checkbox.checked = !checkbox.checked; };
    });
});
