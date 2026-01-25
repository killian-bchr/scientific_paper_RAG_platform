import { useQuery } from "@tanstack/react-query";
import { statsService } from "../services/statsService";
import { authService } from "../services/authService";
import SearchPapers from "../components/SearchPapers";

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

  return (
    <div style={{ padding: 24 }}>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <h1>📚 Paper Database RAG Platform</h1>
        <button onClick={handleLogout} style={styles.logoutButton}>
          Logout
        </button>
      </div>

      <div style={styles.grid}>
        <Metric label="📄 Papers" value={data.total_papers} />
        <Metric label="👤 Authors" value={data.total_authors} />
        <Metric label="🏷️ Domains" value={data.total_domains} />
        <Metric label="📂 Categories" value={data.total_categories} />
      </div>

      <SearchPapers />
    </div>
  );
}

function Metric({ label, value }) {
  return (
    <div style={styles.card}>
      <h3>{label}</h3>
      <p style={styles.value}>{value}</p>
    </div>
  );
}

const styles = {
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(4, 1fr)",
    gap: 16,
    marginTop: 24,
  },
  card: {
    padding: 20,
    borderRadius: 8,
    border: "1px solid #ddd",
    textAlign: "center",
  },
  value: {
    fontSize: 28,
    fontWeight: "bold",
  },
};
