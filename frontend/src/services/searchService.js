import api from "./api";

export const searchService = {
  searchPapers: async (params) => {
    const { data } = await api.post("/search", params, {
      timeout: 60000,
    });
    return data;
  },
};
