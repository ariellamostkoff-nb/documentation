// Northbeam docs — small global interactions.
// Auto-loaded by Mintlify (any .js in the content dir is injected site-wide).

// The home page's underline search field opens the real search modal.
document.addEventListener("click", (e) => {
  if (!e.target.closest(".nb-search")) return;
  const entry =
    document.getElementById("search-bar-entry") ||
    document.getElementById("search-bar-entry-mobile");
  if (entry) entry.click();
});
document.addEventListener("keydown", (e) => {
  if ((e.key === "Enter" || e.key === " ") && e.target.closest?.(".nb-search")) {
    e.preventDefault();
    const entry =
      document.getElementById("search-bar-entry") ||
      document.getElementById("search-bar-entry-mobile");
    if (entry) entry.click();
  }
});
