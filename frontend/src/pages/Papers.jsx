import { useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";
import { domainService } from "../services/domainService";
import { paperService } from "../services/paperService";
import PaperDetailsModal from "../components/PaperDetailsModal";
import PaperFilters from "../components/PaperFilters";
import Header from "../components/Header";

export default function Papers() {
  const navigate = useNavigate();

  const [selectedDomain, setSelectedDomain] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("");
  const [startYear, setStartYear] = useState("");
  const [endYear, setEndYear] = useState("");
  const [selectedPaperId, setSelectedPaperId] = useState(null);

  const { data: paperDetail, isLoading: isPaperLoading } = useQuery({
    queryKey: ["paper", selectedPaperId],
    queryFn: () => paperService.getPaperById(selectedPaperId),
    enabled: selectedPaperId !== null,
  });

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

  const clearFilters = () => {
    setSelectedDomain("");
    setSelectedCategory("");
    setStartYear("");
    setEndYear("");
    setSelectedPaperId(null);
  };

  return (
    <div style={{ padding: 24 }}>
      <Header title="📄 Papers" />

      <PaperFilters
        domains={domains}
        categories={categories}
        years={years}
        selectedDomain={selectedDomain}
        selectedCategory={selectedCategory}
        startYear={startYear}
        endYear={endYear}
        onDomainChange={(e) => {
          setSelectedDomain(e.target.value);
          setSelectedCategory("");
          setSelectedPaperId(null);
        }}
        onCategoryChange={(e) => setSelectedCategory(e.target.value)}
        onStartYearChange={(e) => setStartYear(e.target.value)}
        onEndYearChange={(e) => setEndYear(e.target.value)}
        onClear={clearFilters}
      />

      <div style={{ display: "flex", gap: 20 }}>
        <div style={{ flex: 1 }}>
          <h3>📄 Papers List</h3>
          {papers.length === 0 && <p>No papers found</p>}
          <ul>
            {papers.map((p) => (
              <li key={p.id}>
                {p.title}

                <button onClick={() => setSelectedPaperId(p.id)}>
                  View details
                </button>

                <button
                  onClick={() => navigate(`/chunks/${p.id}`)}
                  style={{ cursor: "pointer" }}
                >
                  View Chunks
                </button>

                {p.pdf_url && (
                  <a
                    href={p.pdf_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    style={{
                      marginLeft: 8,
                      padding: "4px 8px",
                      background: "#007bff",
                      color: "white",
                      borderRadius: 4,
                      textDecoration: "none",
                      cursor: "pointer",
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

      <PaperDetailsModal
        paper={paperDetail}
        isLoading={isPaperLoading}
        onClose={() => setSelectedPaperId(null)}
      />
    </div>
  );
}
