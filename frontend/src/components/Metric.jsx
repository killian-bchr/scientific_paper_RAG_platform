import { useNavigate } from "react-router-dom";

export default function Metric({ label, value, to }) {
  const navigate = useNavigate();

  return (
    <div
      onClick={() => navigate(to)}
      style={{
        padding: 20,
        borderRadius: 8,
        border: "1px solid #ddd",
        textAlign: "center",
        cursor: "pointer",
        transition: "all 0.2s ease",
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.boxShadow = "0 4px 12px rgba(0,0,0,0.1)";
        e.currentTarget.style.transform = "translateY(-2px)";
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.boxShadow = "none";
        e.currentTarget.style.transform = "none";
      }}
    >
      <h3 style={{ marginBottom: 8 }}>
        {label} <span style={{ fontSize: 14 }}>➜</span>
      </h3>
      <p style={{ fontSize: 28, fontWeight: "bold", margin: 0 }}>{value}</p>
    </div>
  );
}
