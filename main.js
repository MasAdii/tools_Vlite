const themes = {
  blue: {
    "--bg": "#0f2027",
    "--text": "#ffffff",
    "--accent": "#00ffe7",
    "--button": "#2979ff",
    "--button-hover": "#1565c0"
  },
  green: {
    "--bg": "#102d23",
    "--text": "#ffffff",
    "--accent": "#00e676",
    "--button": "#00c853",
    "--button-hover": "#00b248"
  },
  pink: {
    "--bg": "#2a0a23",
    "--text": "#ffffff",
    "--accent": "#ff4081",
    "--button": "#ec407a",
    "--button-hover": "#d81b60"
  },
  dark: {
    "--bg": "#1e1e1e",
    "--text": "#e0e0e0",
    "--accent": "#aaaaaa",
    "--button": "#444",
    "--button-hover": "#333"
  }
};

function applyTheme(name) {
  const root = document.documentElement;
  const theme = themes[name];
  for (const key in theme) {
    root.style.setProperty(key, theme[key]);
  }
  localStorage.setItem("selectedTheme", name);
}

const selector = document.getElementById("themeSelector");
selector.addEventListener("change", () => applyTheme(selector.value));

const savedTheme = localStorage.getItem("selectedTheme") || "blue";
selector.value = savedTheme;
applyTheme(savedTheme);
