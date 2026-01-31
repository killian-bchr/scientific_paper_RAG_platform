import { useQuery } from "@tanstack/react-query";
import { authorService } from "../services/authorService";
import EntityList from "../components/EntityList/EntityList";

export default function Authors() {
  const {
    data: authors,
    isLoading,
    error,
  } = useQuery({
    queryKey: ["authors"],
    queryFn: authorService.getAll,
    staleTime: 5 * 60 * 1000,
  });

  if (isLoading) return <p>Loading authors...</p>;
  if (error) return <p>Error loading authors</p>;

  return (
    <EntityList
      title="👤 Authors"
      items={authors}
      renderItem={(a) => <li key={a.id}>{a.name}</li>}
    />
  );
}
