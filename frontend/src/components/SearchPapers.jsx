import { useState } from "react";
import { useMutation, useQuery } from "@tanstack/react-query";
import { searchService } from "../services/searchService";
import { paperService } from "../services/paperService";
import PaperDetailsModal from "./PaperDetailsModal/PaperDetailsModal";

export default function SearchPapers() {
  const [query, setQuery] = useState("");
  const [selectedPaperId, setSelectedPaperId] = useState(null);
  const [hasSearched, setHasSearched] = useState(false);

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
    setHasSearched(true);
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
      {hasSearched && !isSearching && results.length === 0 && (
        <p>No results yet.</p>
      )}

      {hasSearched && (
        <div style={{ display: "flex", gap: 24 }}>
          <div style={{ flex: 1 }}>
            <h3>📄 Results</h3>
            <ul style={{ listStyle: "none", padding: 0 }}>
              {results.map((r, index) => (
                <li
                  key={r.paper.id}
                  style={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    padding: "8px 0",
                    borderBottom: "1px solid #eee",
                  }}
                >
                  <button
                    onClick={() => setSelectedPaperId(r.paper.id)}
                    style={{
                      background: "transparent",
                      border: "none",
                      cursor: "pointer",
                      textAlign: "left",
                      padding: 0,
                    }}
                  >
                    <div>
                      <strong>
                        {index + 1}. {r.paper.title}
                      </strong>
                      <div style={{ fontSize: 12, color: "#666" }}>
                        Score: {r.score.toFixed(3)}
                      </div>
                    </div>
                  </button>

                  {r.paper.pdf_url && (
                    <a
                      href={r.paper.pdf_url}
                      target="_blank"
                      rel="noopener noreferrer"
                      style={{
                        padding: "4px 10px",
                        background: "#007bff",
                        color: "white",
                        borderRadius: 6,
                        textDecoration: "none",
                        fontSize: 12,
                        whiteSpace: "nowrap",
                      }}
                    >
                      📄 Open PDF
                    </a>
                  )}
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}

      <PaperDetailsModal
        paper={paperDetail}
        isLoading={isLoadingPaper}
        onClose={() => setSelectedPaperId(null)}
      />
    </div>
  );
}
