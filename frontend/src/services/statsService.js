import api from "./api";

export const statsService = {
  getStats: async () => {
    const { data } = await api.get("/stats");
    return data;
  },
};
