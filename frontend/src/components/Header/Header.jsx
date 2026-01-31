import { useNavigate } from "react-router-dom";
import Button from "../Button/Button";
import styles from "./Header.module.css";

export default function Header({ title }) {
  const navigate = useNavigate();

  return (
    <header className={styles.container}>
      <div className={styles.left}>
        {title && <h1 className={styles.title}>{title}</h1>}
      </div>

      <Button
        variant="default"
        onClick={() => navigate("/")}
        aria-label="Go to home"
      >
        🏠 Home
      </Button>
    </header>
  );
}
