import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import PrivateRoutes from "./auth/PrivateRoutes";
import { AuthProvider } from "./context/AuthContext";
import Header from "./components/Header";
import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import LetterDetail from './pages/LetterDetail';
import ErrorPage from './pages/ErrorPage';


function App() {
  return (
    <div className="App">
      <AuthProvider>
        <BrowserRouter>
          <Header />
          <Routes>
            <Route element={<PrivateRoutes />}>
              <Route element={<HomePage />} path="/" />
              <Route element={<LetterDetail />} path="/letters/:id" />
            </Route>
            <Route element={<LoginPage />} path="/login" />
            <Route element={<ErrorPage />} path="*" />
          </Routes>
        </BrowserRouter>
      </AuthProvider>
    </div>
  );
}

export default App;
