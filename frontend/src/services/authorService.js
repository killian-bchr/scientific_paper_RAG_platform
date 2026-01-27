import api from "./api";

export const authorService = {
  getAll: async () => {
    const response = await api.get("/authors");
    return response.data;
  },
};
