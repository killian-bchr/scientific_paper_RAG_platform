import Button from "../Button/Button";
import ChunksDropdown from "../ChunksDropdown/ChunksDropdown";
import styles from "./PaperResultItem.module.css";

export default function PaperResultItem({
  paper,
  onSelect,
  actions = [],
  score,
  chunks = [],
}) {
  return (
    <li className={styles.item}>
      <div className={styles.rowTop}>
        <button
          className={styles.titleButton}
          onClick={() => onSelect(paper.id)}
        >
          <div>
            <strong>{paper.title}</strong>
            {score !== undefined && score !== null && (
              <div className={styles.score}>Score: {score.toFixed(3)}</div>
            )}
          </div>
        </button>

        <div className={styles.actions}>
          {paper.pdf_url && (
            <Button
              as="a"
              variant="primary"
              size="sm"
              href={paper.pdf_url}
              target="_blank"
            >
              📄 Open PDF
            </Button>
          )}

          {actions.map((action, idx) => (
            <span key={idx}>{action}</span>
          ))}
        </div>
      </div>

      {chunks.length > 0 && (
        <div className={styles.rowBottom}>
          <ChunksDropdown chunks={chunks} />
        </div>
      )}
    </li>
  );
}
