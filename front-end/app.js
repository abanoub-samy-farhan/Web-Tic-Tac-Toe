
n navigateToSignUp() {
    document.getElementById('dashboard').style.display = 'block';
}

// Placeholder function for editing profile
function editProfile() {
    const username = prompt('Enter new username:');
    if (username) {
        document.getElementById('username').textContent = username;
    }
}

// Example of expanding with a dynamic history section
function addGameHistory(result) {
    const historyList = document.getElementById('game-history');
    const newItem = document.createElement('li');
    newItem.textContent = `Game ${historyList.children.length + 1}: ${result}`;
    historyList.appendChild(newItem);
}

// Example: addGameHistory('Win');
// Example: addGameHistory('Loss');
