export default function PaperFilters({
  domains,
  categories,
  years,
  selectedDomain,
  selectedCategory,
  startYear,
  endYear,
  onDomainChange,
  onCategoryChange,
  onStartYearChange,
  onEndYearChange,
  onClear,
}) {
  return (
    <div style={{ display: "flex", gap: 16, marginBottom: 20 }}>
      <select value={selectedDomain} onChange={onDomainChange}>
        <option value="">All domains</option>
        {domains.map((d) => (
          <option key={d.id} value={d.id}>
            {d.name}
          </option>
        ))}
      </select>

      <select
        value={selectedCategory}
        onChange={onCategoryChange}
        disabled={!selectedDomain}
      >
        <option value="">All categories</option>
        {categories.map((c) => (
          <option key={c.id} value={c.id}>
            {c.name}
          </option>
        ))}
      </select>

      <select value={startYear} onChange={onStartYearChange}>
        <option value="">Start year</option>
        {years.map((y) => (
          <option key={y} value={y}>
            {y}
          </option>
        ))}
      </select>

      <select value={endYear} onChange={onEndYearChange}>
        <option value="">End year</option>
        {years.map((y) => (
          <option key={y} value={y}>
            {y}
          </option>
        ))}
      </select>

      <button onClick={onClear}>Clear filters</button>
    </div>
  );
}
