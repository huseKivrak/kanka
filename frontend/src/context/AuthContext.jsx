import { createContext, useState, useEffect } from "react";
import jwt_decode from "jwt-decode";
import { Navigate } from "react-router-dom";
import axios from "axios";

const AuthContext = createContext();
export default AuthContext;

const BASE_API_URL = "http://127.0.0.1:8000/";

export const AuthProvider = ({ children }) => {
  const [authTokens, setAuthTokens] = useState(() =>
    localStorage.getItem("authTokens")
      ? JSON.parse(localStorage.getItem("authTokens"))
      : null
  );
  const [user, setUser] = useState(() =>
    localStorage.getItem("authTokens")
      ? jwt_decode(localStorage.getItem("authTokens"))
      : null
  );
  const [loading, setLoading] = useState(true);

  const loginUser = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${BASE_API_URL}/api/token/`, {
        username: e.target.username.value,
        password: e.target.password.value,
      });
      const { data } = response;

      if (response.status === 200) {
        setAuthTokens(data);
        setUser(jwt_decode(data.access));
        localStorage.setItem("authTokens", JSON.stringify(data));
        return true;  // return true on successful login
      } else {
        alert("Something went wrong!");
        return false;
      }
    } catch (error) {
      alert("Something went wrong!");
      return false;
    }
  };

const logoutUser = () => {
    setAuthTokens(null);
    setUser(null);
    localStorage.removeItem("authTokens");
    return true; // return true on successful logout
};

  const contextData = {
    user,
    authTokens,
    setAuthTokens,
    setUser,
    loginUser,
    logoutUser,
  };

  useEffect(() => {
    if (authTokens) {
      setUser(jwt_decode(authTokens.access));
    }
    setLoading(false);
  }, [authTokens, loading]);

  return (
    <AuthContext.Provider value={contextData}>
      {loading ? null : children}
    </AuthContext.Provider>
  );
};
