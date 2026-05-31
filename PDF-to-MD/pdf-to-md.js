const pdfInput = document.getElementById("pdfInput");
const fileName = document.getElementById("fileName");
const status = document.getElementById("status");
const markdownOutput = document.getElementById("markdownOutput");
const preview = document.getElementById("preview");
const convertBtn = document.getElementById("convertBtn");
const downloadBtn = document.getElementById("downloadBtn");
const accentColorInput = document.getElementById("accentColor");
const accentNoColor = document.getElementById("accentNoColor");
const { parseMarkdown } = window.MarkdownPreview;

const renderPreview = () => {
  preview.innerHTML = parseMarkdown(markdownOutput.value);
};

const hexToRgba = (hex, alpha) => {
  const match = hex.replace("#", "").match(/.{1,2}/g);
  if (!match || match.length < 3) {
    return `rgba(0, 0, 0, ${alpha})`;
  }
  const [r, g, b] = match.map((value) => parseInt(value, 16));
  return `rgba(${r}, ${g}, ${b}, ${alpha})`;
};

const getAccentStyles = () => {
  if (accentNoColor.checked) {
    return {
      accent: "#b9b0a3",
      soft: "transparent",
      shadow: "rgba(0, 0, 0, 0.15)",
    };
  }
  const base = accentColorInput.value;
  return {
    accent: base,
    soft: hexToRgba(base, 0.12),
    shadow: hexToRgba(base, 0.3),
  };
};

const applyAccentStyles = () => {
  const styles = getAccentStyles();
  document.documentElement.style.setProperty("--accent", styles.accent);
  document.documentElement.style.setProperty("--accent-soft", styles.soft);
  document.documentElement.style.setProperty("--accent-shadow", styles.shadow);
};

const setStatus = (message, tone = "info") => {
  status.textContent = message;
  status.dataset.tone = tone;
};

const updateSelectedFile = () => {
  const [file] = pdfInput.files;
  if (!file) {
    fileName.textContent = "No file selected.";
    downloadBtn.disabled = !markdownOutput.value.trim();
    return;
  }
  fileName.textContent = `${file.name} · ${(file.size / 1024).toFixed(1)} KB`;
  setStatus("File selected. Run the conversion when ready.");
};

const buildDownloadName = () => {
  const [file] = pdfInput.files;
  if (!file) {
    return "converted.md";
  }
  return file.name.replace(/\.pdf$/i, "") + ".md";
};

const downloadMarkdown = () => {
  const content = markdownOutput.value.trim();
  if (!content) {
    setStatus("There is no Markdown to download yet.", "error");
    return;
  }

  const blob = new Blob([`${markdownOutput.value.replace(/\s+$/, "")}\n`], {
    type: "text/markdown;charset=utf-8",
  });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = buildDownloadName();
  document.body.appendChild(anchor);
  anchor.click();
  anchor.remove();
  URL.revokeObjectURL(url);
};

const convertPdf = async () => {
  const [file] = pdfInput.files;
  if (!file) {
    setStatus("Choose a PDF file before converting.", "error");
    return;
  }

  convertBtn.disabled = true;
  downloadBtn.disabled = true;
  setStatus("Converting PDF to Markdown...");

  try {
    const formData = new FormData();
    formData.append("pdf", file);

    const response = await fetch("/api/pdf-to-md", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(errorText || "Conversion failed.");
    }

    const markdown = await response.text();
    markdownOutput.value = markdown;
    renderPreview();
    downloadBtn.disabled = !markdown.trim();
    setStatus("Conversion complete. Review the Markdown before downloading.", "success");
  } catch (error) {
    const message =
      error instanceof Error ? error.message : "Unable to convert the PDF right now.";
    setStatus(message, "error");
  } finally {
    convertBtn.disabled = false;
  }
};

pdfInput.addEventListener("change", updateSelectedFile);
markdownOutput.addEventListener("input", () => {
  renderPreview();
  downloadBtn.disabled = !markdownOutput.value.trim();
});
convertBtn.addEventListener("click", convertPdf);
downloadBtn.addEventListener("click", downloadMarkdown);
accentColorInput.addEventListener("input", applyAccentStyles);
accentNoColor.addEventListener("change", applyAccentStyles);

renderPreview();
applyAccentStyles();
