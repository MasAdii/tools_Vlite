document.getElementById("previewBtn").addEventListener("click", async () => {
  const box = document.getElementById("previewBox");
  if (box.classList.contains("hidden")) {
    const response = await fetch("tools.py");
    const text = await response.text();
    box.textContent = text;
    box.classList.remove("hidden");
  } else {
    box.classList.add("hidden");
  }
  playClickSound();
});

document.getElementById("copyBtn").addEventListener("click", async () => {
  const response = await fetch("tools.py");
  const text = await response.text();
  await navigator.clipboard.writeText(text);
  alert("📋 Isi file berhasil disalin ke clipboard!");
  playClickSound();
});

document.getElementById("darkModeBtn").addEventListener("click", () => {
  document.body.classList.toggle("dark");
  playClickSound();
});

function playClickSound() {
  const sound = document.getElementById("clickSound");
  sound.currentTime = 0;
  sound.play();
}
