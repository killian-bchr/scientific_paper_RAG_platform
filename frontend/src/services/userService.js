import api from "./api";

export const userService = {
  register: async ({ username, password }) => {
    const response = await api.post("/auth/register", {
      username,
      password,
    });
    return response.data;
  },

  getAll: async () => {
    const response = await api.get("/users/");
    return response.data;
  },

  getById: async (id) => {
    const response = await api.get(`/users/${id}`);
    return response.data;
  },

  deleteById: async (id) => {
    const response = await api.delete(`/users/${id}`);
    return response.data;
  },
};
