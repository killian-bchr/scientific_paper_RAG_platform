import api from "./api";

export const paperService = {
  getFilteredPapers: async ({
    domain_id,
    category_id,
    start_year,
    end_year,
  }) => {
    const params = {};

    if (domain_id) params.domain_id = domain_id;
    if (category_id) params.category_id = category_id;
    if (start_year) params.start_year = start_year;
    if (end_year) params.end_year = end_year;

    const response = await api.get("/papers", { params });
    return response.data;
  },

  getPaperById: async (paperId) => {
    const response = await api.get(`/papers/${paperId}`);
    return response.data;
  },

  getPaperChunks: async (paperId) => {
    const response = await api.get(`/papers/${paperId}/chunks`);
    return response.data;
  },
};
