import React, { useState, useContext } from 'react'
import { Link } from 'react-router-dom'
import AuthContext from '../context/AuthContext'
import { Navigate } from "react-router-dom";

const Header = () => {
    const { user, logoutUser } = useContext(AuthContext)
    const [shouldNavigate, setShouldNavigate] = useState(false);

    const handleLogout = () => {
        const success = logoutUser();
        if (success) {
            setShouldNavigate(true);
        }
    };

    if (shouldNavigate) {
        return <Navigate to="/login" replace />
    }

    return (
        <div>
            <Link to="/">Home</Link>
            <span> | </span>
            {user ? (
                <p onClick={handleLogout}>Logout</p>
            ): (
                <Link to="/login">Login</Link>
            )}

            {user && <p>Hello {user.username}</p>}
        </div>
    )
}

export default Header
