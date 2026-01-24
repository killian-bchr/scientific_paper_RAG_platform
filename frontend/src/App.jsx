import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Domains from "./pages/Domains";
import { authService } from "./services/authService";

function App() {
  const isAuthenticated = authService.isAuthenticated();

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/auth/login" element={<Login />} />

        <Route
          path="/"
          element={
            isAuthenticated ? <Domains /> : <Navigate to="/auth/login" />
          }
        />

        <Route
          path="*"
          element={<Navigate to={isAuthenticated ? "/" : "/auth/login"} />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
