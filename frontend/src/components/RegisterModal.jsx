import { useState } from "react";
import { userService } from "../services/userService";

export default function RegisterModal({ isOpen, onClose }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  if (!isOpen) return null;

  const handleRegister = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      await userService.register({ username, password });
      alert("User created! You can now login.");
      onClose();
    } catch (err) {
      const message = err.response?.data?.detail || "Internal server error";
      setError(message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.overlay} onClick={onClose}>
      <div style={styles.modal} onClick={(e) => e.stopPropagation()}>
        <button style={styles.close} onClick={onClose}>
          ✖
        </button>
        <h3>Register</h3>
        <form
          onSubmit={handleRegister}
          style={{ display: "flex", flexDirection: "column", gap: 12 }}
        >
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button type="submit" disabled={loading}>
            {loading ? "Registering..." : "Register"}
          </button>
          {error && <p style={{ color: "red", fontSize: 12 }}>{error}</p>}
        </form>
      </div>
    </div>
  );
}

const styles = {
  overlay: {
    position: "fixed",
    inset: 0,
    background: "rgba(0,0,0,0.4)",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    zIndex: 1000,
  },
  modal: {
    background: "white",
    padding: 24,
    borderRadius: 8,
    width: 300,
    position: "relative",
  },
  close: {
    position: "absolute",
    top: 8,
    right: 8,
    border: "none",
    background: "transparent",
    fontSize: 18,
    cursor: "pointer",
  },
};
