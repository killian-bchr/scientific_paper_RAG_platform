import { useState } from "react";
import { useMutation, useQuery } from "@tanstack/react-query";
import { searchService } from "../services/searchService";
import { paperService } from "../services/paperService";
import PaperDetailsModal from "./PaperDetailsModal/PaperDetailsModal";
import SearchInput from "./SearchInput/SearchInput";
import PaperResultsList from "./PaperResultsList/PaperResultsList";

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
