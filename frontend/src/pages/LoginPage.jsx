import React, { useState, useContext } from 'react';
import AuthContext from '../context/AuthContext';
import { Navigate } from "react-router-dom";

const LoginPage = () => {
    const { loginUser } = useContext(AuthContext);
    const [shouldNavigate, setShouldNavigate] = useState(false);

    const handleLogin = async (e) => {
        e.preventDefault();
        const success = await loginUser(e);
        if (success) {
            setShouldNavigate(true);
        }
    };

    if (shouldNavigate) {
        return <Navigate to="/" replace />
    }

    return (
        <div>
            <form onSubmit={handleLogin}>
                <input type="text" name="username" placeholder="Enter Username" />
                <input type="password" name="password" placeholder="Enter Password" />
                <input type="submit"/>
            </form>
        </div>
    );
};

export default LoginPage;
