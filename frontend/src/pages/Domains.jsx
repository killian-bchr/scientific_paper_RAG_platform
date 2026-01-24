import { useEffect, useState } from "react";
import { domainService } from "../services/domainService";
import { authService } from "../services/authService";

export default function Domains() {
  const [domains, setDomains] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    domainService
      .getAll()
      .then(setDomains)
      .finally(() => setLoading(false));
  }, []);

  const handleLogout = () => {
    authService.logout();
    window.location.href = "/login";
  };

  if (loading) return <p>Loading...</p>;

  return (
    <div style={{ padding: 20 }}>
      <h2>Domains</h2>

      <button onClick={handleLogout}>Logout</button>

      <ul>
        {domains.map((d) => (
          <li key={d.id}>{d.name}</li>
        ))}
      </ul>
    </div>
  );
}
