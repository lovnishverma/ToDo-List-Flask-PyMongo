function confirmDelete(taskId) {
    document.getElementById('deleteConfirmBtn').setAttribute('href', '/delete/' + taskId);
    var deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    deleteModal.show();
}

// Dark Mode Toggle
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
    var isDark = document.body.classList.contains("dark-mode");
    localStorage.setItem("darkMode", isDark);
    
    // Update icon if it exists
    let icon = document.getElementById("darkModeToggleIcon");
    if(icon) {
        icon.className = isDark ? "bi bi-sun-fill fs-5 text-warning" : "bi bi-moon-fill fs-5";
    }
}

// Load dark mode preference
document.addEventListener("DOMContentLoaded", function() {
    if (localStorage.getItem("darkMode") === "true") {
        document.body.classList.add("dark-mode");
        let icon = document.getElementById("darkModeToggleIcon");
        if(icon) icon.className = "bi bi-sun-fill fs-5 text-warning";
    }
});
