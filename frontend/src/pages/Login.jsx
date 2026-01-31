import { useState } from "react";
import { authService } from "../services/authService";
import RegisterModal from "../components/RegisterModal/RegisterModal";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [isRegisterOpen, setIsRegisterOpen] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      await authService.login(username, password);
      window.location.href = "/";
    } catch (err) {
      if (err.response) {
        const { status, data } = err.response;

        if (status === 401) {
          setError(data?.detail || "Authentication failed");
        } else if (status === 500) {
          setError("Server error, please try again later");
        } else {
          setError("Unexpected error");
        }
      } else {
        setError("Network error — backend unreachable");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <form onSubmit={handleSubmit} style={styles.form}>
        <h2>Connection</h2>

        {error && <p style={styles.error}>{error}</p>}

        <input
          type="username"
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
          {loading ? "Connection..." : "Login"}
        </button>

        <button
          type="button"
          style={styles.registerButton}
          onClick={() => setIsRegisterOpen(true)}
        >
          Register
        </button>
      </form>

      <RegisterModal
        isOpen={isRegisterOpen}
        onClose={() => setIsRegisterOpen(false)}
      />
    </div>
  );
}

const styles = {
  container: {
    minHeight: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  },
  form: {
    width: 300,
    display: "flex",
    flexDirection: "column",
    gap: 12,
  },
  error: {
    color: "red",
    fontSize: 14,
  },
  registerButton: {
    marginTop: 8,
    padding: "6px 12px",
    borderRadius: 4,
    border: "1px solid #007bff",
    background: "#007bff",
    color: "white",
    cursor: "pointer",
  },
};
