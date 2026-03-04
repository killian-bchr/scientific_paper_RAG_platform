import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Home from "./pages/Home";
import Authors from "./pages/Authors";
import Categories from "./pages/Categories";
import Domains from "./pages/Domains";
import Papers from "./pages/Papers";
import Chunks from "./pages/Chunks";
import Users from "./pages/Users";
import AdminRoute from "./components/AdminRoute";
import AppLayout from "./layouts/AppLayout";
import { authService } from "./services/authService";

function App() {
  const isAuthenticated = authService.isAuthenticated();

  return (
    <BrowserRouter>
      <Routes>
        {/* Auth */}
        <Route path="/auth/login" element={<Login />} />

        {/* Home */}
        <Route
          element={
            isAuthenticated ? <AppLayout /> : <Navigate to="/auth/login" />
          }
        >
          <Route path="/" element={<Home />} />
          <Route path="/authors" element={<Authors />} />
          <Route path="/categories" element={<Categories />} />
          <Route path="/domains" element={<Domains />} />
          <Route path="/papers" element={<Papers />} />
          <Route path="/chunks/:paperId" element={<Chunks />} />

          <Route
            path="/users"
            element={
              <AdminRoute>
                <Users />
              </AdminRoute>
            }
          />
        </Route>

        <Route
          path="*"
          element={<Navigate to={isAuthenticated ? "/" : "/auth/login"} />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
