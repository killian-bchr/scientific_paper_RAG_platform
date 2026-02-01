import Button from "../Button/Button";
import styles from "./SearchInput.module.css";

export default function SearchInput({
  value,
  onChange,
  onSearch,
  placeholder,
}) {
  return (
    <div className={styles.container}>
      <input
        type="text"
        placeholder={placeholder}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && onSearch()}
        className={styles.input}
      />
      <Button variant="primary" size="sm" onClick={onSearch}>
        Search
      </Button>
    </div>
  );
}
