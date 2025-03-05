 function confirmDelete(taskId) {
            document.getElementById('deleteConfirmBtn').setAttribute('href', '/delete/' + taskId);
            var deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
            deleteModal.show();
        }

        // Dark Mode Toggle
        function toggleDarkMode() {
            document.body.classList.toggle("dark-mode");
            localStorage.setItem("darkMode", document.body.classList.contains("dark-mode"));
        }

        // Load dark mode preference
        document.addEventListener("DOMContentLoaded", function() {
            if (localStorage.getItem("darkMode") === "true") {
                document.body.classList.add("dark-mode");
                document.getElementById("darkModeToggle").checked = true;
            }
        });