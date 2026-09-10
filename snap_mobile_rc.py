import subprocess, os

# Render ratecard preview page on mobile size
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html_abs = os.path.abspath('ratecard_preview_page.html')
out_png = os.path.abspath('mobile_ratecard_view.png')

cmd = [
    edge_path,
    '--headless',
    '--disable-gpu',
    '--window-size=390,1200',
    f'--screenshot={out_png}',
    f'file:///{html_abs}'
]
subprocess.run(cmd)
print("Mobile rate card snap exists:", os.path.exists(out_png))
