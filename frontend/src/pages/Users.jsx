import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { userService } from "../services/userService";
import Header from "../components/Header";
import { authService } from "../services/authService";

export default function Users() {
  const queryClient = useQueryClient();
  const currentUserId = authService.getUserId();

  const {
    data: users = [],
    isLoading,
    error,
  } = useQuery({
    queryKey: ["users"],
    queryFn: userService.getAll,
    staleTime: 5 * 60 * 1000,
  });

  const deleteMutation = useMutation({
    mutationFn: (id) => userService.deleteById(id),
    onSuccess: () => queryClient.invalidateQueries(["users"]),
  });

  const handleDelete = (user) => {
    if (
      window.confirm(`Are you sure you want to delete user "${user.username}"?`)
    ) {
      deleteMutation.mutate(user.id);
    }
  };

  if (isLoading) return <p>Loading users...</p>;
  if (error) return <p>Error loading users</p>;

  return (
    <div style={{ padding: 20 }}>
      <Header title="👤 Users" />

      <ul>
        {users.map((u) => (
          <li
            key={u.id}
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              maxWidth: 400,
              padding: "6px 0",
            }}
          >
            <div>
              <span>{u.username}</span>{" "}
              <span
                style={{
                  fontSize: 12,
                  padding: "2px 6px",
                  borderRadius: 4,
                  background: u.role === "admin" ? "#dc3545" : "#6c757d",
                  color: "white",
                  marginLeft: 8,
                }}
              >
                {u.role}
              </span>
            </div>

            {u.id !== currentUserId && (
              <button
                onClick={() => handleDelete(u)}
                style={{
                  fontSize: 12,
                  padding: "2px 6px",
                  borderRadius: 4,
                  background: "#dc3545",
                  color: "white",
                  border: "none",
                  cursor: "pointer",
                }}
              >
                Delete
              </button>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
