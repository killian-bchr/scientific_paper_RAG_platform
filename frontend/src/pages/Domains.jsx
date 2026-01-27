import { useQuery } from "@tanstack/react-query";
import { domainService } from "../services/domainService";
import Header from "../components/Header";

export default function Domains() {
  const {
    data: domains,
    isLoading,
    error,
  } = useQuery({
    queryKey: ["domains"],
    queryFn: domainService.getAll,
    staleTime: 5 * 60 * 1000,
  });

  if (isLoading) return <p>Loading Domains...</p>;
  if (error) return <p>Error loading domains</p>;

  return (
    <div style={{ padding: 20 }}>
      <Header title="🌐 Domains" />

      <ul>
        {domains.map((d) => (
          <li key={d.id}>{d.name}</li>
        ))}
      </ul>
    </div>
  );
}
