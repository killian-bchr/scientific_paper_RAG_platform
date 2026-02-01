import { useQuery } from "@tanstack/react-query";
import { statsService } from "../services/statsService";
import { authService } from "../services/authService";
import SearchPapers from "../components/SearchPapers";
import MetricsGrid from "../components/MetricsGrid/MetricsGrid";
import Button from "../components/Button/Button";

export default function Home() {
  const { data, isLoading, error } = useQuery({
    queryKey: ["stats"],
    queryFn: statsService.getStats,
    staleTime: 5 * 60 * 1000,
  });

  const handleLogout = () => {
    authService.logout();
    window.location.href = "/auth/login";
  };

  if (isLoading) return <p>Loading home page...</p>;
  if (error) return <p>Error loading stats</p>;

  const metrics = [
    { label: "📄 Papers", value: data.total_papers, to: "/papers" },
    { label: "👤 Authors", value: data.total_authors, to: "/authors" },
    { label: "🏷️ Domains", value: data.total_domains, to: "/domains" },
    { label: "📂 Categories", value: data.total_categories, to: "/categories" },
  ];

  return (
    <div>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: "16px",
        }}
      >
        <h1>📚 Paper Database RAG Platform</h1>
        <Button variant="danger" size="lg" onClick={handleLogout}>
          Logout
        </Button>
      </div>

      <MetricsGrid metrics={metrics} />

      <SearchPapers />
    </div>
  );
}
