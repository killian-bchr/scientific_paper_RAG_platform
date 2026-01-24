import { useQuery } from "@tanstack/react-query";
import { authorService } from "../services/authorService";

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
    <div style={{ padding: 20 }}>
      <h1>👤 Authors</h1>

      <p>
        Total authors: <strong>{authors.length}</strong>
      </p>

      <ul>
        {authors.map((author) => (
          <li key={author.id}>{author.name}</li>
        ))}
      </ul>
    </div>
  );
}
