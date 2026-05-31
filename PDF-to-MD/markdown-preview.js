(() => {
  const escapeHtml = (value) =>
    value
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/\"/g, "&quot;");

  const parseInline = (value) => {
    let parsed = escapeHtml(value);
    parsed = parsed.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
    parsed = parsed.replace(/__(.+?)__/g, "<em>$1</em>");
    return parsed;
  };

  const closeLists = (listStack, htmlParts) => {
    while (listStack.length > 0) {
      const listType = listStack.pop();
      htmlParts.push(listType === "ol" ? "</ol>" : "</ul>");
    }
  };

  const HARD_BREAK_TOKEN = "[[BR]]";

  const buildParagraphText = (parts) => {
    let output = "";
    parts.forEach((part) => {
      if (part === HARD_BREAK_TOKEN) {
        output += HARD_BREAK_TOKEN;
        return;
      }
      if (!output || output.endsWith("<br>")) {
        output += part;
        return;
      }
      output += ` ${part}`;
    });
    return output.trim();
  };

  const parseMarkdown = (text) => {
    const lines = text.replace(/\r\n?/g, "\n").split("\n");
    const htmlParts = [];
    const listStack = [];
    let inBlockquote = false;
    let inTable = false;
    let tableRows = [];
    let paragraph = [];

    const closeParagraph = () => {
      const paragraphText = buildParagraphText(paragraph);
      if (paragraphText.trim()) {
        const parsed = parseInline(paragraphText).split(HARD_BREAK_TOKEN).join("<br>");
        htmlParts.push(`<p>${parsed}</p>`);
      }
      paragraph = [];
    };

    const closeBlockquote = () => {
      if (inBlockquote) {
        htmlParts.push("</blockquote>");
        inBlockquote = false;
      }
    };

    const parseTableRow = (line) =>
      line
        .replace(/^\|/, "")
        .replace(/\|$/, "")
        .split("|")
        .map((cell) => cell.trim());

    const isSeparatorRow = (line) =>
      /^\|?(\s*:?-+:?\s*\|)+\s*:?-+:?\s*\|?$/.test(line.trim());

    const closeTable = () => {
      if (!inTable) return;
      if (tableRows.length >= 2) {
        const headerCells = tableRows[0];
        const bodyRows = tableRows.slice(1);
        let html = "<table><thead><tr>";
        headerCells.forEach((cell) => {
          html += `<th>${parseInline(cell)}</th>`;
        });
        html += "</tr></thead><tbody>";
        const colCount = headerCells.length;
        bodyRows.forEach((row) => {
          html += "<tr>";
          for (let i = 0; i < colCount; i++) {
            const cell = row[i] || "";
            html += `<td>${parseInline(cell)}</td>`;
          }
          html += "</tr>";
        });
        html += "</tbody></table>";
        htmlParts.push(html);
      }
      inTable = false;
      tableRows = [];
    };

    lines.forEach((rawLine) => {
      const line = rawLine.replace(/\t/g, "  ");

      if (!line.trim()) {
        closeParagraph();
        closeLists(listStack, htmlParts);
        closeBlockquote();
        closeTable();
        return;
      }

      const isTableRow = /^\|.+\|/.test(line.trim());
      if (isTableRow || inTable) {
        if (isSeparatorRow(line)) return;
        if (isTableRow) {
          if (!inTable) {
            closeParagraph();
            closeLists(listStack, htmlParts);
            closeBlockquote();
            inTable = true;
          }
          tableRows.push(parseTableRow(line));
          return;
        }
      }

      if (inTable) closeTable();

      const headingMatch = line.match(/^(#{1,6})\s+(.*)$/);
      if (headingMatch) {
        closeParagraph();
        closeLists(listStack, htmlParts);
        closeBlockquote();
        const level = headingMatch[1].length;
        const content = headingMatch[2];
        htmlParts.push(`<h${level}>${parseInline(content)}</h${level}>`);
        return;
      }

      const hrMatch = line.trim().match(/^-{3,}\s*$/);
      if (hrMatch) {
        closeParagraph();
        closeLists(listStack, htmlParts);
        closeBlockquote();
        htmlParts.push("<hr>");
        return;
      }

      const blockMatch = line.trim().startsWith(">") ? line.trim() : null;
      if (blockMatch) {
        closeParagraph();
        closeLists(listStack, htmlParts);
        if (!inBlockquote) {
          htmlParts.push("<blockquote>");
          inBlockquote = true;
        }
        const content = blockMatch.replace(/^>\s?/, "");
        htmlParts.push(`<p>${parseInline(content)}</p>`);
        return;
      }

      const orderedMatch = line.match(/^(\s*)(\d+)\.\s+(.*)$/);
      const bulletMatch = line.match(/^(\s*)([-*+])\s+(.*)$/);
      if (orderedMatch || bulletMatch) {
        closeParagraph();
        closeBlockquote();

        const indent = (orderedMatch || bulletMatch)[1].length;
        const level = Math.floor(indent / 2);
        const text = (orderedMatch || bulletMatch)[3];
        const listType = orderedMatch ? "ol" : "ul";

        while (listStack.length > level + 1) {
          const currentType = listStack.pop();
          htmlParts.push(currentType === "ol" ? "</ol>" : "</ul>");
        }
        if (listStack[level] && listStack[level] !== listType) {
          const currentType = listStack.pop();
          htmlParts.push(currentType === "ol" ? "</ol>" : "</ul>");
        }
        while (listStack.length < level + 1) {
          htmlParts.push(listType === "ol" ? "<ol>" : "<ul>");
          listStack.push(listType);
        }

        htmlParts.push(`<li>${parseInline(text)}</li>`);
        return;
      }

      if (listStack.length) {
        closeLists(listStack, htmlParts);
      }
      closeBlockquote();
      const hardBreak = /\s{2}$/.test(line) || /\\$/.test(line.trim());
      const cleanLine = line.replace(/\s{2}$|\s*\\$/, "").trim();
      paragraph.push(cleanLine);
      if (hardBreak) {
        paragraph.push(HARD_BREAK_TOKEN);
      }
    });

    closeParagraph();
    closeLists(listStack, htmlParts);
    closeBlockquote();
    closeTable();

    return htmlParts.join("");
  };

  window.MarkdownPreview = {
    parseMarkdown,
  };
})();
