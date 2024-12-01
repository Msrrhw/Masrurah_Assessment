// Update balance on page load
window.onload = function () {
    fetch("/api/get_balance")
      .then((response) => response.json())
      .then((data) => {
        document.getElementById("balance").innerText = `Current Balance: $${data.balance.toFixed(2)}`;
      });
  };
  
  // Deposit money
  function deposit() {
    const amount = parseFloat(document.getElementById("amount").value);
    fetch("/api/deposit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ amount }),
    })
      .then((response) => response.json())
      .then((data) => {
        updateUI(data);
      });
  }
  
  // Withdraw money
  function withdraw() {
    const amount = parseFloat(document.getElementById("amount").value);
    fetch("/api/withdraw", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ amount }),
    })
      .then((response) => response.json())
      .then((data) => {
        updateUI(data);
      });
  }
  
  // Update UI with balance and message
  function updateUI(data) {
    const balanceElement = document.getElementById("balance");
    const messageElement = document.getElementById("message");
  
    balanceElement.innerText = `Current Balance: $${data.balance.toFixed(2)}`;
    messageElement.innerText = data.message;
    messageElement.style.color = data.success ? "green" : "red";
  }
  