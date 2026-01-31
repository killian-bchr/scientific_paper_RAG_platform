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
          path="/"
          element={isAuthenticated ? <Home /> : <Navigate to="/auth/login" />}
        />

        {/* Public authenticated pages */}
        <Route
          path="/authors"
          element={
            authService.isAuthenticated() ? (
              <Authors />
            ) : (
              <Navigate to="/auth/login" />
            )
          }
        />

        <Route
          path="/categories"
          element={
            authService.isAuthenticated() ? (
              <Categories />
            ) : (
              <Navigate to="/auth/login" />
            )
          }
        />

        <Route
          path="/domains"
          element={
            authService.isAuthenticated() ? (
              <Domains />
            ) : (
              <Navigate to="/auth/login" />
            )
          }
        />

        <Route
          path="/papers"
          element={
            authService.isAuthenticated() ? (
              <Papers />
            ) : (
              <Navigate to="/auth/login" />
            )
          }
        />

        <Route
          path="/chunks/:paperId"
          element={
            authService.isAuthenticated() ? (
              <Chunks />
            ) : (
              <Navigate to="/auth/login" />
            )
          }
        />

        {/* Admin only */}
        <Route
          path="/users"
          element={
            <AdminRoute>
              <Users />
            </AdminRoute>
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
