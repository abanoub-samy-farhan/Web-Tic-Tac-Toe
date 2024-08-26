import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav className="navbar">
            <div className="logo">
                <Link to="/">TicTacToe Mania</Link>
            </div>
            <ul>
                <li><Link to="/">Back to Home</Link></li>
                <li><Link to="/get-started">Get Started</Link></li>
            </ul>
        </nav>
    );
}

export default Navbar;
