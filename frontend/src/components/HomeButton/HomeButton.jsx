import { useNavigate } from "react-router-dom";
import styles from "./HomeButton.module.css";

export default function HomeButton() {
  const navigate = useNavigate();

  return (
    <button
      className={styles.button}
      onClick={() => navigate("/")}
      aria-label="Go to home"
    >
      🏠 Home
    </button>
  );
}
