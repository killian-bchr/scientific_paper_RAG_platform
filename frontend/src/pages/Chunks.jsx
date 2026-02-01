import { useParams, useNavigate } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { paperService } from "../services/paperService";
import { useState } from "react";

export default function Chunks() {
  const { paperId } = useParams();
  const navigate = useNavigate();
  const [selectedType, setSelectedType] = useState("");

  const {
    data: chunks = [],
    isLoading,
    error,
  } = useQuery({
    queryKey: ["chunks", paperId],
    queryFn: () => paperService.getPaperChunks(paperId),
  });

  if (isLoading) return <p>Loading chunks...</p>;
  if (error) return <p>Error loading chunks</p>;

  const chunkTypes = Array.from(new Set(chunks.map((c) => c.chunk_type)));
  const filteredChunks =
    selectedType && selectedType !== "ALL"
      ? chunks.filter((c) => c.chunk_type === selectedType)
      : chunks;

  return (
    <div style={{ padding: 24 }}>
      <h1>📦 Chunks for Paper {paperId}</h1>

      <button onClick={() => navigate(-1)} style={{ marginBottom: 16 }}>
        ← Back to Papers
      </button>

      <div style={{ marginBottom: 16 }}>
        <label>Filter by type: </label>
        <select
          value={selectedType}
          onChange={(e) => setSelectedType(e.target.value)}
        >
          <option value="ALL">ALL</option>
          {chunkTypes.map((type) => (
            <option key={type} value={type}>
              {type}
            </option>
          ))}
        </select>
      </div>

      <p>📦 Number of chunks: {filteredChunks.length}</p>

      <div>
        {filteredChunks.map((chunk, i) => (
          <details key={i} style={{ marginBottom: 12 }}>
            <summary>
              {i + 1}. {chunk.chunk_type} | page {chunk.page_no}
            </summary>
            <p>{chunk.content}</p>
          </details>
        ))}
      </div>
    </div>
  );
}
