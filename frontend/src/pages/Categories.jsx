import { useQuery } from "@tanstack/react-query";
import { categoryService } from "../services/categoryService";

export default function Categories() {
  const {
    data: categories,
    isLoading,
    error,
  } = useQuery({
    queryKey: ["categories"],
    queryFn: categoryService.getAll,
    staleTime: 5 * 60 * 1000,
  });

  if (isLoading) return <p>Loading Categories...</p>;
  if (error) return <p>Error loading categories</p>;

  return (
    <div style={{ padding: 20 }}>
      <h2>🧩 Categories</h2>

      <ul>
        {categories.map((c) => (
          <li key={c.id}>{c.name}</li>
        ))}
      </ul>
    </div>
  );
}
