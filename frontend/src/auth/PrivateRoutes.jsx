import { Outlet, Navigate } from "react-router-dom";
import { useContext } from "react";
import AuthContext from "../context/AuthContext";

const PrivateRoutes = () => {
  const authContext = useContext(AuthContext);
  if (!authContext) {
    throw new Error("AuthContext is not available");
  }
  let { user } = authContext;

  return <>{user ? <Outlet /> : <Navigate to="/login" replace />}</>;
};

export default PrivateRoutes;
