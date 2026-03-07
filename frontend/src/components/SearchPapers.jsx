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

      {isSearching && <p>Searching…</p>}
      {hasSearched && !isSearching && (
        <PaperResultsList results={results} onSelect={setSelectedPaperId} />
      )}

      <PaperDetailsModal
        paper={paperDetail}
        isLoading={isLoadingPaper}
        onClose={() => setSelectedPaperId(null)}
      />
    </div>
  );
}
