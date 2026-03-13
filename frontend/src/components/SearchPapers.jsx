import { useState } from "react";
import { useMutation, useQuery } from "@tanstack/react-query";
import { searchService } from "../services/searchService";
import { paperService } from "../services/paperService";
import { domainService } from "../services/domainService";
import PaperDetailsModal from "./PaperDetailsModal/PaperDetailsModal";
import SearchInput from "./SearchInput/SearchInput";
import PaperResultsList from "./PaperResultsList/PaperResultsList";
import PaperFilters from "./PaperFilters/PaperFilters";

export default function SearchPapers() {
  const [query, setQuery] = useState("");
  const [selectedPaperId, setSelectedPaperId] = useState(null);
  const [hasSearched, setHasSearched] = useState(false);

  const [selectedDomain, setSelectedDomain] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("");
  const [startYear, setStartYear] = useState("");
  const [endYear, setEndYear] = useState("");

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

  const currentYear = new Date().getFullYear();
  const years = Array.from(
    { length: currentYear - 1970 + 1 },
    (_, i) => 1970 + i,
  );

  const {
    mutate,
    data: results = [],
    isPending: isSearching,
    isError,
    error,
  } = useMutation({
    mutationFn: searchService.searchPapers,
    onSuccess: (data) => {
      console.log("✅ Résultats reçus :", data);
      console.log("📦 Nombre de résultats :", data?.length);
      setSelectedPaperId(null);
    },
    onError: (err) => {
      console.error("❌ Erreur API :", err);
      console.error("📄 Détail :", err?.message, err?.response);
    },
    onMutate: (variables) => {
      console.log("🚀 Requête envoyée avec :", variables);
    },
  });

  const { data: paperDetail, isLoading: isLoadingPaper } = useQuery({
    queryKey: ["paper", selectedPaperId],
    queryFn: () => paperService.getPaperById(selectedPaperId),
    enabled: !!selectedPaperId,
  });

  const handleSearch = () => {
    if (!query.trim()) return;
    setHasSearched(true);

    mutate({
      query,
      domain_id: selectedDomain || undefined,
      category_id: selectedCategory || undefined,
      start_year: startYear || undefined,
      end_year: endYear || undefined,
    });
  };

  const clearFilters = () => {
    setSelectedDomain("");
    setSelectedCategory("");
    setStartYear("");
    setEndYear("");

    if (hasSearched && query.trim()) {
      handleSearch();
    }
  };

  return (
    <div style={{ marginTop: 32 }}>
      <h2>🔎 Search papers</h2>

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
        }}
        onCategoryChange={(e) => setSelectedCategory(e.target.value)}
        onStartYearChange={(e) => setStartYear(e.target.value)}
        onEndYearChange={(e) => setEndYear(e.target.value)}
        onClear={clearFilters}
      />

      <SearchInput
        value={query}
        onChange={setQuery}
        onSearch={handleSearch}
        placeholder="Search by keywords, concepts, abstract..."
      />

      {isSearching && (
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 8,
            marginTop: 16,
          }}
        >
          <span
            style={{
              display: "inline-block",
              width: 18,
              height: 18,
              border: "3px solid #e0e0e0",
              borderTopColor: "#1a73e8",
              borderRadius: "50%",
              animation: "spin 0.7s linear infinite",
            }}
          />
          <p style={{ margin: 0 }}>Searching…</p>
        </div>
      )}

      {hasSearched &&
        !isSearching &&
        (isError ? (
          <p style={{ color: "#e53935", marginTop: 16 }}>
            {error?.message?.includes("timeout")
              ? "⏱️ The search took too long. Try adding filters to narrow down the results."
              : `❌ An error occurred : ${error?.message}`}
          </p>
        ) : (
          <PaperResultsList results={results} onSelect={setSelectedPaperId} />
        ))}

      <PaperDetailsModal
        paper={paperDetail}
        isLoading={isLoadingPaper}
        onClose={() => setSelectedPaperId(null)}
      />

      <style>{`
        @keyframes spin {
          to { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
}
