document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".control").forEach((button) => {
        button.addEventListener("click", () => {
            const activeBtn = document.querySelector(".active-btn")
            if (activeBtn) {
                activeBtn.classList.remove("active-btn");
            }

            button.classList.add("active-btn");

            const activeContent = document.querySelector(".active")
            if (activeContent) {
                activeContent.classList.remove("active");
            }

            const targetContent = document.getElementById(button.dataset.id)
            if (targetContent) {
                targetContent.classList.add("active");
            }
        });
    });

    document.querySelector(".theme-btn").addEventListener("click", () => {
        document.body.classList.toggle("light-mode");
    });
});
