import { useQuery } from "@tanstack/react-query";
import { categoryService } from "../services/categoryService";
import Header from "../components/Header";

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

  const uniqueCategories = Array.from(
    new Map(categories.map((c) => [c.name, c])).values(),
  );

  return (
    <div style={{ padding: 20 }}>
      <Header title="🧩 Categories" />

      <ul>
        {uniqueCategories.map((c) => (
          <li key={c.id}>{c.name}</li>
        ))}
      </ul>
    </div>
  );
}
