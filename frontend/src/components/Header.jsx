import { useNavigate } from "react-router-dom";
import { authService } from "../services/authService";

export default function Header({ title }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    authService.logout();
    navigate("/auth/login");
  };

  return (
    <div style={styles.container}>
      {title && <h1 style={styles.title}>{title}</h1>}

      <button onClick={() => navigate("/")} style={styles.homeButton}>
        🏠 Home
      </button>
    </div>
  );
}

const styles = {
  container: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: 24,
  },
  left: {
    display: "flex",
    alignItems: "center",
    gap: 16,
  },
  title: {
    margin: 0,
  },
  homeButton: {
    padding: "6px 12px",
    borderRadius: 6,
    border: "1px solid #ddd",
    background: "#f5f5f5",
    cursor: "pointer",
  },
  logoutButton: {
    padding: "6px 12px",
    borderRadius: 6,
    border: "none",
    background: "#dc3545",
    color: "white",
    cursor: "pointer",
  },
};
