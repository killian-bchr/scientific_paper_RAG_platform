export default function CloseButton({ onClick, className }) {
  return (
    <button className={className} onClick={onClick} aria-label="Close">
      ✖
    </button>
  );
}
