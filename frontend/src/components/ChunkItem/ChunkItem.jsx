import styles from "./ChunkItem.module.css";

export default function ChunkItem({ chunk, score }) {
  return (
    <div className={styles.chunk}>
      {score !== undefined && (
        <div className={styles.score}>Score: {score.toFixed(3)}</div>
      )}

      <p className={styles.content}>
        {chunk.content.length > 250
          ? chunk.content.slice(0, 250) + "..."
          : chunk.content}
      </p>
    </div>
  );
}
