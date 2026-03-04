import PaperResultItem from "../PaperResultItem/PaperResultItem";

export default function PaperResultsList({
  results,
  onSelect,
  actionsBuilder,
  showScore = true,
}) {
  if (!results || results.length === 0) return <p>No results yet.</p>;

  return (
    <ul style={{ listStyle: "none", padding: 0 }}>
      {results.map((r) => (
        <PaperResultItem
          key={r.paper.id}
          paper={r.paper}
          score={showScore ? r.score : undefined}
          onSelect={onSelect}
          actions={actionsBuilder ? actionsBuilder(r) : []}
        />
      ))}
    </ul>
  );
}
