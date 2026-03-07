import api from "./api";

export const chunkService = {
  getById: async (id) => {
    const response = await api.get(`/chunks/${id}`);
    return response.data;
  },

  getChunkContext: async (id, windowSize = 2) => {
    const response = await api.get(`/chunks/${id}/context`, {
      params: { window: windowSize },
    });

    return response.data;
  },
};
