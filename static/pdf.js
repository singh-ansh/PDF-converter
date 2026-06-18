document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const status = document.getElementById("status");
    const button = document.getElementById("convert-btn");

    form.addEventListener("submit", function () {

        status.innerText = "Converting PDF... Please Wait ⏳";

        button.disabled = true;

        button.innerText = "Converting...";
    });

});

const dropZone = document.getElementById("drop-zone");
const fileInput = document.getElementById("file-input");
const fileText = document.getElementById("file-text");

fileInput.addEventListener("change", () => {

    if (fileInput.files.length > 0) {

        const file = fileInput.files[0];

        fileText.innerHTML = `
            ✅ ${file.name}<br>
            ${(file.size / 1024 / 1024).toFixed(2)} MB
        `;
    }

});

dropZone.addEventListener("click", () => {
    fileInput.click();
});

dropZone.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropZone.classList.add("dragover");
});

dropZone.addEventListener("dragleave", () => {
    dropZone.classList.remove("dragover");
});

dropZone.addEventListener("drop", (e) => {

    e.preventDefault();

    dropZone.classList.remove("dragover");

    fileInput.files = e.dataTransfer.files;

    if (fileInput.files.length > 0) {

        const file = fileInput.files[0];

        fileText.innerHTML = `
            ✅ ${file.name}<br>
            ${(file.size / 1024 / 1024).toFixed(2)} MB
        `;
    }

});

