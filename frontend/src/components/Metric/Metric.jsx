import { useNavigate } from "react-router-dom";
import styles from "./Metric.module.css";

export default function Metric({ label, value, to }) {
  const navigate = useNavigate();

  return (
    <div
      className={styles.card}
      onClick={() => navigate(to)}
      role="button"
      tabIndex={0}
      onKeyDown={(e) => e.key === "Enter" && navigate(to)}
    >
      <h3 className={styles.label}>
        {label} <span className={styles.arrow}>➜</span>
      </h3>
      <p className={styles.value}>{value}</p>
    </div>
  );
}
