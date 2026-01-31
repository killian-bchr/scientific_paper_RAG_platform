import HomeButton from "../HomeButton/HomeButton";
import styles from "./Header.module.css";

export default function Header({ title }) {
  return (
    <header className={styles.container}>
      <div className={styles.left}>
        {title && <h1 className={styles.title}>{title}</h1>}
      </div>

      <HomeButton />
    </header>
  );
}
