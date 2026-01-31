import { Navigate } from "react-router-dom";
import { authService } from "../services/authService";

export default function AdminRoute({ children }) {
  const isAuthenticated = authService.isAuthenticated();

  if (!isAuthenticated) {
    return <Navigate to="/auth/login" replace />;
  }

  let isAdmin = false;
  try {
    isAdmin = authService.isAdmin();
  } catch (e) {
    console.error("AdminRoute error:", e);
    return <Navigate to="/" replace />;
  }

  if (!isAdmin) {
    return <Navigate to="/" replace />;
  }

  return children;
}
