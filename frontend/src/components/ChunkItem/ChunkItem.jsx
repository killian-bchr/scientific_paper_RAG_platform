import { useState } from "react";
import styles from "./ChunkItem.module.css";
import ChunkContext from "../ChunkContext/ChunkContext";

export default function ChunkItem({ chunk, score }) {
  const [showContext, setShowContext] = useState(false);

  return (
    <div className={styles.chunk}>
      {chunk.chunk_type && (
        <div className={styles.chunkType}>{chunk.chunk_type}</div>
      )}

      {score !== undefined && (
        <div className={styles.score}>Score: {score.toFixed(3)}</div>
      )}

      <p className={styles.contentPreview}>
        {chunk.content.length > 250
          ? chunk.content.slice(0, 250) + "..."
          : chunk.content}
      </p>

      <button
        className={styles.viewButton}
        onClick={() => setShowContext(true)}
      >
        View Context
      </button>

      {showContext && (
        <div className={styles.overlay} onClick={() => setShowContext(false)}>
          <div className={styles.modal} onClick={(e) => e.stopPropagation()}>
            <button
              className={styles.close}
              onClick={() => setShowContext(false)}
            >
              ✖
            </button>

            <ChunkContext chunkId={chunk.id} />
          </div>
        </div>
      )}
    </div>
  );
}
