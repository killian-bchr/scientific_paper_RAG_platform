import Metric from "../Metric/Metric";
import styles from "./MetricsGrid.module.css";

export default function MetricsGrid({ metrics }) {
  if (!metrics || metrics.length === 0) return null;

  return (
    <div className={styles.grid}>
      {metrics.map((m) => (
        <Metric key={m.label} label={m.label} value={m.value} to={m.to} />
      ))}
    </div>
  );
}
