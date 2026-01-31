import { useState } from "react";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";
import { domainService } from "../services/domainService";
import { paperService } from "../services/paperService";
import { authService } from "../services/authService";
import PaperDetailsModal from "../components/PaperDetailsModal/PaperDetailsModal";
import PaperFilters from "../components/PaperFilters";
import Header from "../components/Header/Header";
import PaperResultsList from "../components/PaperResultsList/PaperResultsList";
import Button from "../components/Button/Button";

export default function Papers() {
  const navigate = useNavigate();
  const isAdmin = authService.isAdmin();
  const queryClient = useQueryClient();

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

  const handleDelete = async (paperId) => {
    if (!window.confirm("Are you sure you want to delete this paper?")) return;

    try {
      await paperService.deletePaper(paperId);
      queryClient.invalidateQueries(["papers"]);
      alert("Paper deleted");
    } catch (err) {
      console.error(err);
      alert("Error deleting paper");
    }
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
          {papers.length === 0 && <p>No papers found</p>}
          <PaperResultsList
            results={papers.map((p) => ({ paper: p }))}
            onSelect={setSelectedPaperId}
            showScore={false}
            actionsBuilder={(r) =>
              [
                <Button
                  key="chunks"
                  variant="default"
                  size="sm"
                  onClick={() => navigate(`/chunks/${r.paper.id}`)}
                >
                  View Chunks
                </Button>,
                isAdmin && (
                  <Button
                    key="delete"
                    variant="danger"
                    size="sm"
                    onClick={() => handleDelete(r.paper.id)}
                  >
                    Delete
                  </Button>
                ),
              ].filter(Boolean)
            }
          />
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
