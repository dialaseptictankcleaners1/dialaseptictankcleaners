import subprocess
import os

def render_pdf(html_path, pdf_path):
    edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    abs_html = os.path.abspath(html_path)
    abs_pdf = os.path.abspath(pdf_path)
    
    cmd = [
        edge_path,
        '--headless',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={abs_pdf}',
        f'file:///{abs_html}'
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(abs_pdf) and os.path.getsize(abs_pdf) > 1000:
        print(f"SUCCESS: Generated {pdf_path} ({os.path.getsize(abs_pdf)} bytes)")
        return True
    else:
        print(f"FAILED to generate {pdf_path}: {res.stderr}")
        return False

# CSS common style
COMMON_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');

@page {
    size: A4;
    margin: 18mm 16mm 18mm 16mm;
    @bottom-right {
        content: counter(page);
    }
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
    line-height: 1.6;
    font-size: 13.5px;
}

.page {
    page-break-after: always;
    position: relative;
    padding-bottom: 20px;
}
.page:last-child {
    page-break-after: avoid;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #0284c7;
    padding-bottom: 12px;
    margin-bottom: 20px;
}

.brand-badge {
    font-size: 11px;
    font-weight: 700;
    color: #0284c7;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    background: #e0f2fe;
    padding: 4px 10px;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 4px;
}

.brand-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: #0f172a;
}

.header-meta {
    text-align: right;
    font-size: 11.5px;
    color: #64748b;
}

.header-meta strong {
    color: #0f172a;
}

.doc-hero {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0369a1 100%);
    color: white;
    padding: 30px 26px;
    border-radius: 12px;
    margin-bottom: 24px;
    box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.15);
}

.doc-hero h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 26px;
    font-weight: 700;
    line-height: 1.25;
    margin-bottom: 10px;
    color: #ffffff;
}

.doc-hero p {
    font-size: 13.5px;
    color: #cbd5e1;
    max-width: 680px;
}

.doc-tag {
    display: inline-block;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.25);
    color: #38bdf8;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 600;
    margin-bottom: 12px;
}

h2 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 17px;
    font-weight: 700;
    color: #0f172a;
    border-left: 4px solid #0284c7;
    padding-left: 10px;
    margin-top: 22px;
    margin-bottom: 12px;
}

h3 {
    font-size: 14.5px;
    font-weight: 600;
    color: #1e293b;
    margin-top: 14px;
    margin-bottom: 6px;
}

p {
    margin-bottom: 10px;
    color: #334155;
}

.grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 16px;
}

.grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-bottom: 16px;
}

.card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 14px;
}

.card-accent {
    border-top: 3px solid #0284c7;
}

.card-warn {
    border-top: 3px solid #f59e0b;
}

.card-success {
    border-top: 3px solid #10b981;
}

.card h4 {
    font-size: 13.5px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 6px;
}

.card p, .card ul {
    font-size: 12px;
    color: #475569;
}

ul {
    padding-left: 18px;
    margin-bottom: 10px;
}

li {
    margin-bottom: 4px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0 18px 0;
    font-size: 12px;
}

th {
    background: #0f172a;
    color: #ffffff;
    text-align: left;
    padding: 8px 10px;
    font-weight: 600;
}

td {
    padding: 8px 10px;
    border-bottom: 1px solid #e2e8f0;
    color: #334155;
}

tr:nth-child(even) td {
    background: #f8fafc;
}

.badge {
    display: inline-block;
    padding: 2px 7px;
    border-radius: 4px;
    font-size: 10.5px;
    font-weight: 600;
}

.badge-blue { background: #e0f2fe; color: #0369a1; }
.badge-green { background: #dcfce7; color: #15803d; }
.badge-amber { background: #fef3c7; color: #b45309; }
.badge-red { background: #fee2e2; color: #b91c1c; }

.callout {
    background: #f0fdf4;
    border-left: 4px solid #22c55e;
    padding: 12px 14px;
    border-radius: 0 6px 6px 0;
    margin: 14px 0;
}

.callout-title {
    font-weight: 700;
    color: #15803d;
    font-size: 13px;
    margin-bottom: 4px;
}

.highlight-box {
    background: #f0f9ff;
    border: 1px dashed #0284c7;
    padding: 12px 14px;
    border-radius: 8px;
    margin: 12px 0;
}

.footer {
    border-top: 1px solid #e2e8f0;
    padding-top: 8px;
    display: flex;
    justify-content: space-between;
    font-size: 10.5px;
    color: #94a3b8;
    margin-top: 24px;
}
"""

print("Common CSS ready")
