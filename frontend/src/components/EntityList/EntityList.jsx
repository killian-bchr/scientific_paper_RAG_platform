import Header from "../Header/Header";
import styles from "./EntityList.module.css";

export default function EntityList({ title, items, renderItem }) {
  const count = items?.length ?? 0;

  return (
    <div className={styles.container}>
      <Header title={title} />

      <p className={styles.count}>
        Total: <strong>{count}</strong>
      </p>

      <ul>{items.map(renderItem)}</ul>
    </div>
  );
}
