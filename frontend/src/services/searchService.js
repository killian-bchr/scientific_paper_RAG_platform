import api from "./api";

export const searchService = {
  searchPapers: async (query) => {
    const { data } = await api.post("/search", {
      query,
    });
    return data;
  },
};
