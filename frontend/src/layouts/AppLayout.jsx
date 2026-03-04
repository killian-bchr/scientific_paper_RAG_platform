import { Outlet } from "react-router-dom";
import styles from "./AppLayout.module.css";

export default function AppLayout() {
  return (
    <main className={styles.container}>
      <div className={styles.content}>
        <Outlet />
      </div>
    </main>
  );
}
