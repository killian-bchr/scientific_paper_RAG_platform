import styles from "./ReliabilityScore.module.css";

function getReliabilityLabel(score) {
  if (score >= 0.8) return "🟢 High Reliability";
  if (score >= 0.6) return "🟡 Good Reliability";
  if (score >= 0.4) return "🟠 Medium Reliability";
  return "🔴 Low Reliability";
}

export default function ReliabilityScore({ score }) {
  if (score === null || score === undefined) {
    return <p>Reliability score not available</p>;
  }

  const roundedScore = Number(score).toFixed(2);
  const label = getReliabilityLabel(score);

  return (
    <div className={styles.container}>
      <div className={styles.label}>{label}</div>

      <div className={styles.barBackground}>
        <div
          className={styles.barFill}
          style={{
            width: `${score * 100}%`,
            backgroundColor:
              score >= 0.8
                ? "#2ecc71"
                : score >= 0.6
                  ? "#f1c40f"
                  : score >= 0.4
                    ? "#e67e22"
                    : "#e74c3c",
          }}
        />
      </div>

      <div className={styles.scoreText}>Score: {roundedScore}</div>
    </div>
  );
}
