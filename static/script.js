const gallery = document.getElementById("gallery");
const popup = document.getElementById("popup");
const chickenName = document.getElementById("chickenName");
const optionsDiv = document.getElementById("options");

// Load chickens from backend
fetch("/api/chickens")
    .then(res => res.json())
    .then(data => {
        data.forEach(chicken => {

            const card = document.createElement("div");
            card.className = "chicken-card";

            const img = document.createElement("img");
            img.src = `/static/${chicken.image}`;
            img.className = "chicken";
            img.onclick = () => openChicken(chicken.id);

            const name = document.createElement("p");
            name.innerText = chicken.name;
            name.className = "chicken-name";

            card.appendChild(img);
            card.appendChild(name);
            gallery.appendChild(card);
        });
    });

function openChicken(id) {
    fetch(`/api/chicken/${id}`)
        .then(res => res.json())
        .then(data => {
            chickenName.innerText = data.name;
            optionsDiv.innerHTML = "";

            data.options.forEach(option => {
                const btn = document.createElement("button");
                btn.innerText = option;
                optionsDiv.appendChild(btn);
            });

            popup.style.display = "flex";
        });
}

function closePopup() {
    popup.style.display = "none";
}