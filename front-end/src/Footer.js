import React from 'react';
import { Link } from 'react-router-dom';

function Footer() {
    return (
        <footer>
            <p>&copy; 2024 Web Tic Tac Toe - Play Fair, Play Smart, Play Tic Tac Toe</p>
            <ul>
                <li><Link to="/privacy-policy">Privacy Policy</Link></li>
                <li><Link to="/terms-of-service">Terms of Service</Link></li>
            </ul>
        </footer>
    );
}

export default Footer;
