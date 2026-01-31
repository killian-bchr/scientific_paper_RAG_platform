import { useState } from "react";
import { userService } from "../../services/userService";
import CloseButton from "../CloseButton/CloseButton";
import Button from "../Button/Button"; // <-- ici
import styles from "./RegisterModal.module.css";

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
    <div className={styles.overlay} onClick={onClose}>
      <div className={styles.modal} onClick={(e) => e.stopPropagation()}>
        <CloseButton className={styles.close} onClick={onClose} />

        <h3>Register</h3>

        <form className={styles.form} onSubmit={handleRegister}>
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

          <Button type="submit" variant="primary" disabled={loading}>
            {loading ? "Registering..." : "Register"}
          </Button>

          {error && <p className={styles.error}>{error}</p>}
        </form>
      </div>
    </div>
  );
}
