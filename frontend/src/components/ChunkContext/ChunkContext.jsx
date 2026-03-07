import { useEffect, useState } from "react";
import { chunkService } from "../../services/chunkService";
import styles from "./ChunkContext.module.css";

export default function ChunkContext({ chunkId, initialWindowSize = 2 }) {
  const [contextChunks, setContextChunks] = useState([]);
  const [windowSize, setWindowSize] = useState(initialWindowSize);

  useEffect(() => {
    async function fetchContext() {
      try {
        const data = await chunkService.getChunkContext(chunkId, windowSize);
        setContextChunks(data);
      } catch (err) {
        console.error("Failed to fetch chunk context", err);
      }
    }

    fetchContext();
  }, [chunkId, windowSize]);

  if (!contextChunks || contextChunks.length === 0) return null;

  const handleWindowChange = (e) => {
    let val = parseInt(e.target.value, 10);
    if (isNaN(val)) val = 0;
    if (val < 0) val = 0;
    if (val > 10) val = 10;
    setWindowSize(val);
  };

  return (
    <div className={styles.contextContainer}>
      <div className={styles.windowControl}>
        <label>
          Window size:{" "}
          <input
            type="number"
            value={windowSize}
            min={0}
            max={10}
            onChange={handleWindowChange}
          />
        </label>
      </div>

      <div className={styles.context}>
        {contextChunks.map((chunk) => {
          const isCenter = chunk.id === chunkId;
          return (
            <div key={chunk.id} className={isCenter ? styles.centerChunk : ""}>
              {chunk.content}
            </div>
          );
        })}
      </div>
    </div>
  );
}
