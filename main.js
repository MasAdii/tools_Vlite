document.getElementById("previewBtn").addEventListener("click", async () => {
  const box = document.getElementById("previewBox");
  try {
    const response = await fetch("tools.py");
    const text = await response.text();
    if (response.ok) {
      box.textContent = text;
      box.classList.remove("hidden");
    } else {
      throw new Error("Failed to fetch file");
    }
  } catch (error) {
    console.error(error);
    alert("Gagal memuat file.");
  }
  playClickSound();
});

document.getElementById("copyBtn").addEventListener("click", async () => {
  try {
    const response = await fetch("tools.py");
    const text = await response.text();
    if (response.ok) {
      await navigator.clipboard.writeText(text);
      alert("📋 Isi file berhasil disalin ke clipboard!");
    } else {
      throw new Error("Failed to fetch file");
    }
  } catch (error) {
    console.error(error);
    alert("Gagal menyalin file.");
  }
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
