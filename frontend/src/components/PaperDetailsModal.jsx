export default function PaperDetailsModal({ paper, isLoading, onClose }) {
  if (!paper && !isLoading) return null;

  return (
    <div style={styles.overlay} onClick={onClose}>
      <div style={styles.modal} onClick={(e) => e.stopPropagation()}>
        <button style={styles.close} onClick={onClose}>
          ✖
        </button>

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
            <h4>Abstract</h4>
            <p>{paper.abstract || "No abstract available"}</p>
          </>
        )}
      </div>
    </div>
  );
}

const styles = {
  overlay: {
    position: "fixed",
    inset: 0,
    background: "rgba(0,0,0,0.4)",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    zIndex: 1000,
  },
  modal: {
    background: "white",
    padding: 24,
    borderRadius: 8,
    width: "70%",
    maxHeight: "80vh",
    overflowY: "auto",
    position: "relative",
  },
  close: {
    position: "absolute",
    top: 10,
    right: 10,
    border: "none",
    background: "transparent",
    fontSize: 18,
    cursor: "pointer",
  },
};
