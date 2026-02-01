import api from "./api";

export const domainService = {
  getAll: async () => {
    const response = await api.get("/domains/");
    return response.data;
  },

  getById: async (id) => {
    const response = await api.get(`/domains/${id}`);
    return response.data;
  },

  getCategories: async (domainId) => {
    const response = await api.get(`/domains/${domainId}/categories`);
    return response.data;
  },
};
