import Button from "../Button/Button";
import ReliabilityScore from "../ReliabilityScore/ReliabilityScore";
import styles from "./PaperDetailsModal.module.css";

export default function PaperDetailsModal({ paper, isLoading, onClose }) {
  if (!paper && !isLoading) return null;

  return (
    <div className={styles.overlay} onClick={onClose}>
      <div className={styles.modal} onClick={(e) => e.stopPropagation()}>
        <Button
          variant="close"
          onClick={onClose}
          className={styles.close}
          aria-label="Close modal"
        >
          ✖
        </Button>

        <h3>📌 Paper Details</h3>

        {isLoading && !paper && <p>Loading paper details...</p>}

        {paper && (
          <>
            <p>
              <strong>{paper.title}</strong>
            </p>
            <p>
              <strong>Authors:</strong>{" "}
              {paper.authors?.map((a) => a.name).join(", ") || "—"}
            </p>
            {paper.publication_date && (
              <p>
                <strong>Published:</strong> {paper.publication_date}
              </p>
            )}
            {paper.journal && (
              <p>
                <strong>Journal:</strong> {paper.journal}
              </p>
            )}
            <p>
              <strong>Domains:</strong>{" "}
              {paper.domains?.map((d) => d.name).join(", ") || "—"}
            </p>
            <p>
              <strong>Categories:</strong>{" "}
              {paper.categories
                ? Array.from(new Set(paper.categories.map((c) => c.name))).join(
                    ", ",
                  )
                : "—"}
            </p>

            <ReliabilityScore score={paper.reliability_score} />

            <h4>Abstract</h4>
            <p>{paper.abstract || "No abstract available"}</p>
          </>
        )}
      </div>
    </div>
  );
}
