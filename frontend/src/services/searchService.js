import api from "./api";

export const searchService = {
  searchPapers: async (params) => {
    const { data } = await api.post("/search", params);
    return data;
  },
};
