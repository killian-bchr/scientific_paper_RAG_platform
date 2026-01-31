import styles from "./SubmitButton.module.css";

export default function SubmitButton({
  children,
  loading,
  disabled,
  ...props
}) {
  return (
    <button
      className={styles.button}
      type="submit"
      disabled={disabled || loading}
      {...props}
    >
      {loading ? "Loading..." : children}
    </button>
  );
}
