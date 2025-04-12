document.addEventListener("DOMContentLoaded", () => {
  const themeSelector = document.getElementById("themeSelector");

  const themes = {
    blue: {
      "--bg": "linear-gradient(135deg, #0f0c29, #302b63, #24243e)",
      "--accent": "#00ffe7",
      "--link-hover": "#ff00ff",
      "--button-download": "#00c853",
      "--button-download-hover": "#00e676",
      "--button-preview": "#2979ff",
      "--button-preview-hover": "#5393ff",
      "--card-shadow": "rgba(0, 255, 255, 0.3)",
      "--footer-link-hover": "#ff4081"
    },
    green: {
      "--bg": "linear-gradient(135deg, #0f2027, #2c5364, #00bf8f)",
      "--accent": "#00ff9c",
      "--link-hover": "#00e6a3",
      "--button-download": "#43a047",
      "--button-download-hover": "#66bb6a",
      "--button-preview": "#00897b",
      "--button-preview-hover": "#26a69a",
      "--card-shadow": "rgba(0, 255, 179, 0.3)",
      "--footer-link-hover": "#00e676"
    },
    pink: {
      "--bg": "linear-gradient(135deg, #833ab4, #fd1d1d, #fcb045)",
      "--accent": "#ffb6c1",
      "--link-hover": "#ff69b4",
      "--button-download": "#e91e63",
      "--button-download-hover": "#f06292",
      "--button-preview": "#f48fb1",
      "--button-preview-hover": "#f8bbd0",
      "--card-shadow": "rgba(255, 105, 180, 0.3)",
      "--footer-link-hover": "#ff4081"
    },
    dark: {
      "--bg": "linear-gradient(135deg, #232526, #414345)",
      "--accent": "#cfcfcf",
      "--link-hover": "#aaaaaa",
      "--button-download": "#555",
      "--button-download-hover": "#777",
      "--button-preview": "#888",
      "--button-preview-hover": "#aaa",
      "--card-shadow": "rgba(255, 255, 255, 0.1)",
      "--footer-link-hover": "#eee"
    }
  };

  themeSelector.addEventListener("change", (e) => {
    const selectedTheme = themes[e.target.value];
    for (const varName in selectedTheme) {
      document.documentElement.style.setProperty(varName, selectedTheme[varName]);
    }
  });

  themeSelector.value = "blue";
  const initTheme = themes["blue"];
  for (const varName in initTheme) {
    document.documentElement.style.setProperty(varName, initTheme[varName]);
  }
});
