import styles from "./OpenPDFButton.module.css";

export default function OpenPDFButton({ url }) {
  if (!url) return null;

  return (
    <a
      href={url}
      target="_blank"
      rel="noopener noreferrer"
      className={styles.button}
    >
      📄 Open PDF
    </a>
  );
}
