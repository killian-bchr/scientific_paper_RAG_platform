import api from "./api";
import { jwtDecode } from "jwt-decode";

export const authService = {
  login: async (username, password) => {
    const params = new URLSearchParams();
    params.append("username", username);
    params.append("password", password);

    const response = await api.post("/auth/login", params, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });

    const token = response.data.access_token;
    localStorage.setItem("token", token);

    return token;
  },

  logout: () => {
    localStorage.removeItem("token");
  },

  isAuthenticated: () => {
    return !!localStorage.getItem("token");
  },

  getDecodedToken: () => {
    const token = localStorage.getItem("token");
    if (!token) return null;

    try {
      return jwtDecode(token);
    } catch (e) {
      console.error("JWT decode error:", e);
      return null;
    }
  },

  getUserId: () => {
    const decoded = authService.getDecodedToken();
    return decoded?.id ?? null;
  },

  getRole: () => {
    const decoded = authService.getDecodedToken();
    return decoded?.role ?? null;
  },

  isAdmin: () => authService.getRole() === "admin",
};
