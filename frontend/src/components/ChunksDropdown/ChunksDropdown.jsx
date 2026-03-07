import { useState } from "react";
import ChunkItem from "../ChunkItem/ChunkItem";
import styles from "./ChunksDropdown.module.css";

export default function ChunksDropdown({ chunks }) {
  const [open, setOpen] = useState(false);

  if (!chunks || chunks.length === 0) return null;

  return (
    <div className={styles.container}>
      <button className={styles.toggle} onClick={() => setOpen(!open)}>
        {open ? "Hide ▲" : `Relevant passages (${chunks.length}) ▼`}
      </button>

      {open && (
        <div className={styles.dropdown}>
          {chunks.map((c, i) => (
            <ChunkItem key={i} chunk={c.chunk} score={c.score} />
          ))}
        </div>
      )}
    </div>
  );
}
