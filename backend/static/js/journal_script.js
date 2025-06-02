document.addEventListener("DOMContentLoaded", function () {
  const pairList = document.getElementById("pairList");
  const pairButton = document.getElementById("dropdownMenuButton");
  const pairInput = document.getElementById("paire");

  const defaultPairs = ["EURUSD", "GBPUSD", "USDJPY", "XAUUSD", "BTCUSD"];
  let customPairs = JSON.parse(localStorage.getItem("customPairs") || "[]");
  let favorites = JSON.parse(localStorage.getItem("favPairs") || "[]");

  function renderPairs() {
    pairList.innerHTML = "";
    const allPairs = [...new Set([...favorites, ...defaultPairs, ...customPairs])];

    allPairs.forEach(pair => {
      const item = document.createElement("li");
      item.className = "dropdown-item d-flex justify-content-between align-items-center";

      const label = document.createElement("span");
      label.textContent = pair;
      label.onclick = () => {
        pairButton.textContent = pair;
        pairInput.value = pair;
      };

      const star = document.createElement("span");
      star.innerHTML = favorites.includes(pair) ? "â­" : "â";
      star.style.cursor = "pointer";
      star.onclick = (e) => {
        e.stopPropagation();
        if (favorites.includes(pair)) {
          favorites = favorites.filter(p => p !== pair);
        } else {
          favorites.unshift(pair);
        }
        localStorage.setItem("favPairs", JSON.stringify(favorites));
        renderPairs();
      };

      item.appendChild(label);
      item.appendChild(star);
      pairList.appendChild(item);
    });

    const addItem = document.createElement("li");
    addItem.className = "dropdown-item text-warning text-center";
    addItem.textContent = "+ Ajouter une paire";
    addItem.onclick = () => {
      document.getElementById("newPairInput").focus();
    };
    pairList.appendChild(addItem);
  }

  window.addNewPair = () => {
    const newPair = document.getElementById("newPairInput").value.toUpperCase();
    if (newPair && !customPairs.includes(newPair)) {
      customPairs.push(newPair);
      localStorage.setItem("customPairs", JSON.stringify(customPairs));
      renderPairs();
      document.getElementById("newPairInput").value = "";
    }
  };

  renderPairs();
});

function toggleTPMode() {
  const mode = document.getElementById("tpMode").value;
  document.getElementById("tpContainer").style.display = mode === "multiple" ? "block" : "none";
  document.getElementById("tpUniqueInput").style.display = mode === "unique" ? "block" : "none";
}

function generateTPInputs() {
  const count = parseInt(document.getElementById("tpCount").value);
  const container = document.getElementById("tpInputs");
  container.innerHTML = "";
  for (let i = 1; i <= count; i++) {
    const input = document.createElement("input");
    input.type = "number";
    input.step = "0.01";
    input.className = "form-control mb-2";
    input.placeholder = `TP${i}`;
    input.name = `tp${i}`;
    container.appendChild(input);
  }
}

function submitTrade(event) {
  event.preventDefault();
  alert("Formulaire prÃªt Ã  Ãªtre envoyÃ© au backend !");
}
