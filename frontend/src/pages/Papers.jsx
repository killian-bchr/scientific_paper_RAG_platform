import { useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";
import { domainService } from "../services/domainService";
import { paperService } from "../services/paperService";

export default function Papers() {
  const navigate = useNavigate();

  const [selectedDomain, setSelectedDomain] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("");
  const [startYear, setStartYear] = useState("");
  const [endYear, setEndYear] = useState("");
  const [selectedPaperId, setSelectedPaperId] = useState(null);

  const currentYear = new Date().getFullYear();
  const years = Array.from(
    { length: currentYear - 1970 + 1 },
    (_, i) => 1970 + i,
  );

  const { data: domains = [] } = useQuery({
    queryKey: ["domains"],
    queryFn: domainService.getAll,
  });

  const { data: categories = [] } = useQuery({
    queryKey: ["categories", selectedDomain],
    queryFn: () =>
      selectedDomain ? domainService.getCategories(selectedDomain) : [],
    enabled: !!selectedDomain,
  });

  const { data: papers = [] } = useQuery({
    queryKey: ["papers", selectedDomain, selectedCategory, startYear, endYear],
    queryFn: () =>
      paperService.getFilteredPapers({
        domain_id: selectedDomain || undefined,
        category_id: selectedCategory || undefined,
        start_year: startYear || undefined,
        end_year: endYear || undefined,
      }),
    keepPreviousData: true,
  });

  const selectedPaper = papers.find((p) => p.id === selectedPaperId);

  const clearFilters = () => {
    setSelectedDomain("");
    setSelectedCategory("");
    setStartYear("");
    setEndYear("");
    setSelectedPaperId(null);
  };

  return (
    <div style={{ padding: 24 }}>
      <h1>📄 Papers</h1>

      <div style={{ display: "flex", gap: 16, marginBottom: 20 }}>
        <select
          value={selectedDomain}
          onChange={(e) => {
            setSelectedDomain(e.target.value);
            setSelectedCategory("");
            setSelectedPaperId(null);
          }}
        >
          <option value="">All domains</option>
          {domains.map((d) => (
            <option key={d.id} value={d.id}>
              {d.name}
            </option>
          ))}
        </select>

        <select
          value={selectedCategory}
          onChange={(e) => setSelectedCategory(e.target.value)}
          disabled={!selectedDomain}
        >
          <option value="">All categories</option>
          {categories.map((c) => (
            <option key={c.id} value={c.id}>
              {c.name}
            </option>
          ))}
        </select>

        <select
          value={startYear}
          onChange={(e) => setStartYear(e.target.value)}
        >
          <option value="">Start year</option>
          {years.map((y) => (
            <option key={y} value={y}>
              {y}
            </option>
          ))}
        </select>

        <select value={endYear} onChange={(e) => setEndYear(e.target.value)}>
          <option value="">End year</option>
          {years.map((y) => (
            <option key={y} value={y}>
              {y}
            </option>
          ))}
        </select>

        <button onClick={clearFilters}>Clear Filters</button>
      </div>

      <div style={{ display: "flex", gap: 20 }}>
        <div style={{ flex: 1 }}>
          <h3>📄 Papers List</h3>
          {papers.length === 0 && <p>No papers found</p>}
          <ul>
            {papers.map((p) => (
              <li key={p.id}>
                <button
                  onClick={() => setSelectedPaperId(p.id)}
                  style={{
                    background:
                      selectedPaperId === p.id ? "#ddd" : "transparent",
                    border: "none",
                    cursor: "pointer",
                  }}
                >
                  {p.title}
                </button>

                <button
                  onClick={() => navigate(`/chunks/${p.id}`)}
                  style={{ cursor: "pointer" }}
                >
                  View Chunks
                </button>
              </li>
            ))}
          </ul>
        </div>

        {selectedPaper && (
          <div style={{ flex: 2, border: "1px solid #ddd", padding: 16 }}>
            <h3>📌 Paper Details</h3>
            <p>
              <strong>Title:</strong> {selectedPaper.title}
            </p>
            <p>
              <strong>Authors:</strong>{" "}
              {selectedPaper.authors.map((a) => a.name).join(", ")}
            </p>
            <p>
              <strong>Domains:</strong>{" "}
              {selectedPaper.domains.map((d) => d.name).join(", ")}
            </p>
            <p>
              <strong>Categories:</strong>{" "}
              {selectedPaper.categories.map((c) => c.name).join(", ")}
            </p>
            <p>
              <strong>Abstract:</strong> {selectedPaper.abstract}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
