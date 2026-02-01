import styles from "./Button.module.css";

export default function Button({
  children,
  as,
  onClick,
  variant = "default",
  size = "md",
  className = "",
  ...props
}) {
  const Tag = as || "button";
  return (
    <Tag
      onClick={onClick}
      className={`${styles.button} ${styles[variant]} ${styles[size]} ${className}`}
      {...props}
    >
      {children}
    </Tag>
  );
}
