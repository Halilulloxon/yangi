document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("downloadZipBtn");

    btn.addEventListener("click", async function () {
        const table = document.getElementById("myTable");
        const workbook = XLSX.utils.table_to_book(table, { sheet: "Jadval" });
        const base64 = XLSX.write(workbook, { bookType: "xlsx", type: "base64" });
        const excelDataUrl = "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64," + base64;

        const rows = table.tBodies[0].rows;
        const last = rows[0].cells.length - 1;
        const fileList = [];

        for (let i = 0; i < rows.length; i++) {
            const a = rows[i].cells[last].querySelector("a");
            let fileUrl = a ? a.getAttribute("href") : "";
            const idx = fileUrl.indexOf("/media/");
            if (idx !== -1) fileList.push(fileUrl.substring(idx + 7));
        }

        const res = await fetch("/download-zip/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ excel: excelDataUrl, files: fileList })
        });

        const blob = await res.blob();
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        const b = date;
        a.href = url;
        a.download = `export_${new Date().toISOString().slice(0, 10)}.zip`; 
        document.body.appendChild(a);
        a.click();
        a.remove();
        URL.revokeObjectURL(url);
    });
});
