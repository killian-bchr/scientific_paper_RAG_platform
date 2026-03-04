import { useQuery } from "@tanstack/react-query";
import { categoryService } from "../services/categoryService";
import EntityList from "../components/EntityList/EntityList";

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
    <EntityList
      title="🧩 Categories"
      items={uniqueCategories}
      renderItem={(c) => <li key={c.id}>{c.name}</li>}
    />
  );
}
