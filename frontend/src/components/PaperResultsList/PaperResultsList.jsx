import PaperResultItem from "../PaperResultItem/PaperResultItem";

export default function PaperResultsList({
  results,
  onSelect,
  actionsBuilder,
  showScore = true,
}) {
  if (!results || results.length === 0) {
    return (
      <p style={{ marginTop: 16, color: "#666" }}>
        No results found for your search.
      </p>
    );
  }

  const sortedResults = [...results].sort((a, b) => b.score - a.score);

  return (
    <ul style={{ listStyle: "none", padding: 0 }}>
      {sortedResults.map((r) => (
        <PaperResultItem
          key={r.paper.id}
          paper={r.paper}
          score={showScore ? r.score : undefined}
          chunks={r.chunks}
          onSelect={onSelect}
          actions={actionsBuilder ? actionsBuilder(r) : []}
        />
      ))}
    </ul>
  );
}
