import { useState } from "react";
import { useMutation, useQuery } from "@tanstack/react-query";
import { searchService } from "../services/searchService";
import { paperService } from "../services/paperService";
import PaperDetailsModal from "../components/PaperDetailsModal";

export default function SearchPapers() {
  const [query, setQuery] = useState("");
  const [selectedPaperId, setSelectedPaperId] = useState(null);

  const {
    mutate,
    data: results = [],
    isLoading: isSearching,
  } = useMutation({
    mutationFn: searchService.searchPapers,
    onSuccess: () => setSelectedPaperId(null),
  });

  const { data: paperDetail, isLoading: isLoadingPaper } = useQuery({
    queryKey: ["paper", selectedPaperId],
    queryFn: () => paperService.getPaperById(selectedPaperId),
    enabled: !!selectedPaperId,
  });

  const handleSearch = () => {
    if (!query.trim()) return;
    mutate(query);
  };

  return (
    <div style={{ marginTop: 32 }}>
      <h2>🔎 Search papers</h2>

      <div style={{ display: "flex", gap: 12, marginBottom: 20 }}>
        <input
          type="text"
          placeholder="Search by keywords, concepts, abstract..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{ flex: 1, padding: 8 }}
          onKeyDown={(e) => e.key === "Enter" && handleSearch()}
        />
        <button onClick={handleSearch}>Search</button>
      </div>

      {isSearching && <p>Searching…</p>}
      {results.length === 0 && !isSearching && <p>No results yet.</p>}

      <div style={{ display: "flex", gap: 24 }}>
        <div style={{ flex: 1 }}>
          <h3>📄 Results</h3>
          <ul>
            {results.map((r, index) => (
              <li key={r.paper.id} style={{ marginBottom: 8 }}>
                <button
                  onClick={() => setSelectedPaperId(r.paper.id)}
                  style={{
                    background: "transparent",
                    border: "none",
                    cursor: "pointer",
                    textAlign: "left",
                  }}
                >
                  <strong>
                    {index + 1}. {r.paper.title}
                  </strong>
                  <div style={{ fontSize: 12, color: "#666" }}>
                    Score: {r.score.toFixed(3)}
                  </div>
                </button>
              </li>
            ))}
          </ul>
        </div>
      </div>

      <PaperDetailsModal
        paper={paperDetail}
        isLoading={isLoadingPaper}
        onClose={() => setSelectedPaperId(null)}
      />
    </div>
  );
}
