import React from 'react';
import { Link } from 'react-router-dom';
import './styles.css';

function WelcomePage() {
    return (
        <>
            {/* Navbar */}
            <nav className="navbar">
                <div className="logo">TicTacToe Mania</div>
                <ul>
                    <li><Link to="/whats-this">What's This?</Link></li>
                    <li><Link to="/get-started" className="get-started-btn">Jump In!</Link></li>
                </ul>
            </nav>

            {/* Welcome Section */}
            <section className="welcome">
                <h1>Are You Tic-Tac-Toe-nough?</h1>
                <p>Welcome to the world’s most competitive Tic Tac Toe arena! Ready to challenge your brain and your friends in a battle of wits? Buckle up, because it’s about to get real!</p>
                <Link to="/sign-up" className="btn">Let's Get Tic-Tac-Crackin'!</Link>
            </section>

            {/* Dashboard (Placeholder) */}
            <div id="dashboard" style={{ display: 'none' }}>
                {/* Profile Component */}
                <section className="profile">
                    <h2>Player Profile</h2>
                    <p><strong>Username:</strong> <span id="username">TheUltimateToe</span></p>
                    <p><strong>Win/Loss Ratio:</strong> <span id="win-loss"// Make sure this path matches your project structure>42 Wins / 7 Losses</span></p>
                    <button onClick={() => alert('Edit Profile Coming Soon!')}>Revamp Your Persona</button>
                </section>

                {/* History Games Component */}
                <section className="history-games">
                    <h2>Your Legendary Battles</h2>
                    <ul id="game-history">
                        <li>Game 1: Crushed It! (Win)</li>
                        <li>Game 2: Close Call... (Loss)</li>
                    </ul>
                </section>
            </div>

            {/* Footer */}
            <footer>
                <p>&copy; 2024 Web Tic Tac Toe - Where X's and O's Live Happily Ever After</p>
                <ul>
                    <li><Link to="/privacy-policy">Privacy Policy (We Keep Secrets!)</Link></li>
                    <li><Link to="/terms-of-service">Terms of Service (No Toe Left Behind)</Link></li>
                </ul>
            </footer>
        </>
    );
}

export default WelcomePage;
