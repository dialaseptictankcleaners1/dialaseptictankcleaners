import os
from pdf_common import COMMON_CSS, render_pdf

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Business Plan of Action - Dial-a-Septic Tank Cleaners</title>
<style>
{COMMON_CSS}
</style>
</head>
<body>

<!-- PAGE 1: Strategic Vision & Go-to-Market -->
<div class="page">
    <div class="header">
        <div>
            <div class="brand-badge">Operational & Commercial Roadmap</div>
            <div class="brand-title">DIAL-A-SEPTIC TANK CLEANERS</div>
        </div>
        <div class="header-meta">
            <div><strong>Location:</strong> Madhapur, Hyderabad</div>
            <div><strong>Objective:</strong> Market Leadership in Cyberabad</div>
            <div><strong>Date:</strong> 2026 Strategy Document</div>
        </div>
    </div>

    <div class="doc-hero">
        <div class="doc-tag">Deliverable 02 / 03 • Business Plan of Action</div>
        <h1>Strategic Business Plan of Action & Operations Roadmap</h1>
        <p>A comprehensive commercial blueprint outlining go-to-market execution, client acquisition channels, operational SLAs, fleet deployment protocols, B2B recurring AMC packages, and a phased 30-60-90 day milestone plan.</p>
    </div>

    <h2>1. Strategic Vision & Core Value Proposition</h2>
    <p>
        <strong>Vision:</strong> To become Hyderabad’s foremost digitized, mechanized, and environmentally compliant industrial hygiene and wastewater evacuation enterprise, eliminating operational downtime for residential societies, IT parks, hospitality giants, and industrial complexes.
    </p>
    <p>
        <strong>Core Value Proposition (The "Dial-a-Septic" Guarantee):</strong>
    </p>
    <div class="grid-3">
        <div class="card card-accent">
            <h4>1. Rapid 45-Min Dispatch</h4>
            <p>Strategic fleet staging in Madhapur ensures guaranteed rapid response to high-priority emergencies across Western Hyderabad.</p>
        </div>
        <div class="card card-success">
            <h4>2. 100% Mechanized & Safe</h4>
            <p>Zero manual scavenging. Modern high-vacuum suction pumps, high-pressure jetting, and gas-monitored safety protocols.</p>
        </div>
        <div class="card card-warn">
            <h4>3. Transparent Fixed Pricing</h4>
            <p>Standardized digital rate card, GST compliance, digital payment processing, and transparent volumetric billing.</p>
        </div>
    </div>

    <h2>2. Dual-Engine Client Acquisition Model</h2>
    <div class="grid-2">
        <div class="card card-accent">
            <h4>ENGINE A: High-Intent B2C & Emergency Inbound</h4>
            <p><strong>Goal:</strong> Capture immediate emergency service inquiries with sub-5-minute lead response.</p>
            <ul>
                <li><strong>Hyperlocal SEO:</strong> Dedicated landing pages for 20 service areas (e.g., <em>"Septic Tank Cleaning in Kondapur"</em>, <em>"Emergency Drainage Cleaning in Gachibowli"</em>).</li>
                <li><strong>Google Local Services & Maps:</strong> Optimizing Google Business Profile for "near me" instant clicks.</li>
                <li><strong>WhatsApp Direct Booking:</strong> One-tap WhatsApp chat with automated location sharing and vehicle dispatch status.</li>
                <li><strong>Sticky Click-to-Call Buttons:</strong> Immediate telephonic conversion for panicked homeowners or store managers.</li>
            </ul>
        </div>
        <div class="card card-accent">
            <h4>ENGINE B: Predictable High-Margin B2B Contracts (AMC)</h4>
            <p><strong>Goal:</strong> Secure stable recurring revenue through multi-year Annual Maintenance Contracts.</p>
            <ul>
                <li><strong>Residential Societies (RWAs):</strong> Quarterly septic & drain de-silting retainers for gated communities (Nallagandla, Tellapur, Manikonda).</li>
                <li><strong>Corporate IT Campuses:</strong> Monthly/bi-monthly STP aeration, SBR tank, and filter feed maintenance in Hitech City and Gachibowli.</li>
                <li><strong>Hospitality Chains & Cloud Kitchens:</strong> Fortnightly grease trap and kitchen line hydro-jetting contracts across Madhapur and Jubilee Hills.</li>
                <li><strong>Construction & Infrastructure:</strong> Weekly scheduled portable toilet cleaning and pumping for general contractors.</li>
            </ul>
        </div>
    </div>
</div>

<!-- PAGE 2: Standard Operating Procedure (SOP) -->
<div class="page">
    <div class="header">
        <div>
            <div class="brand-badge">Operations & Service Protocols</div>
            <div class="brand-title">DIAL-A-SEPTIC TANK CLEANERS</div>
        </div>
        <div class="header-meta">
            <div>Document: <strong>Business Plan of Action</strong></div>
            <div>Page: <strong>02 of 04</strong></div>
        </div>
    </div>

    <h2>3. 5-Stage Standard Operating Procedure (SOP)</h2>
    <p>To differentiate from unorganized contractors, Dial-a-Septic Tank Cleaners enforces a disciplined, mechanized 5-stage service workflow on every job site:</p>

    <div class="highlight-box">
        <h4 style="color: #0369a1; margin-bottom: 4px;">Stage 1: Booking & Automated Rapid Dispatch</h4>
        <p style="margin-bottom: 0;">Customer books via website/WhatsApp/Call. Geolocation, tank capacity, and basement level (Ground, B1, B2, B3) are captured. Nearest vacuum tanker unit dispatched with live SMS/WhatsApp notification.</p>
    </div>

    <div class="highlight-box">
        <h4 style="color: #0369a1; margin-bottom: 4px;">Stage 2: On-Site Safety Inspection & Gas Screening</h4>
        <p style="margin-bottom: 0;">Technicians arrive in full PPE (respirators, protective suits, boots, heavy-duty gloves). Chamber lid cracked safely; 4-gas digital detector deployed to monitor toxic H2S and combustible methane levels. Air exhaust blower deployed if required.</p>
    </div>

    <div class="highlight-box">
        <h4 style="color: #0369a1; margin-bottom: 4px;">Stage 3: Mechanized High-Vacuum Extraction</h4>
        <p style="margin-bottom: 0;">Vacuum tanker PTO engaged. Reinforced spiral suction hoses coupled. Heavy bottom sludge agitated using high-pressure jetting water lances and thoroughly sucked into the sealed vacuum tanker without messy spills or foul air release.</p>
    </div>

    <div class="highlight-box">
        <h4 style="color: #0369a1; margin-bottom: 4px;">Stage 4: High-Pressure Wall Wash & Bio-Enzyme Treatment</h4>
        <p style="margin-bottom: 0;">Chamber walls, baffles, and outlet pipes hydro-washed with high-pressure water jets. Eco-friendly bacterial inoculants and deodorizing neutralizers added to curb future odor and jumpstart healthy bio-digestion.</p>
    </div>

    <div class="highlight-box">
        <h4 style="color: #0369a1; margin-bottom: 4px;">Stage 5: Verification, Digital Invoicing & Legal Decanting</h4>
        <p style="margin-bottom: 0;">Customer inspects clean tank via flashlight/inspection camera. Chamber sealed securely. Digital invoice with GST issued via SMS/Email. Tanker navigates to authorized municipal treatment facility for compliant decanting.</p>
    </div>

    <div class="callout">
        <div class="callout-title">Specialized B1/B2/B3 Basement SOP</div>
        <p>For multi-tier underground parking basements where ceiling height is under 2.4 meters, Dial-a-Septic deploys auxiliary booster pumps or specialized low-profile mobile units with multi-hose couplers, eliminating vehicle height entry barriers.</p>
    </div>
</div>

<!-- PAGE 3: Pricing Models & B2B Packages -->
<div class="page">
    <div class="header">
        <div>
            <div class="brand-badge">Commercial Pricing & Revenue Models</div>
            <div class="brand-title">DIAL-A-SEPTIC TANK CLEANERS</div>
        </div>
        <div class="header-meta">
            <div>Document: <strong>Business Plan of Action</strong></div>
            <div>Page: <strong>03 of 04</strong></div>
        </div>
    </div>

    <h2>4. Commercial Pricing Architecture (Verified Rate Card)</h2>
    <p>All rates are fixed <strong>Per One Trip — Loading, Cleaning & Outside Dumping Included</strong>:</p>

    <table>
        <thead>
            <tr>
                <th style="width: 26%;">Service Category</th>
                <th style="width: 22%;">Capacity / Vehicle</th>
                <th style="width: 22%;">Verified Rate (INR)</th>
                <th style="width: 30%;">Deliverables & Scope</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>1. Individual Houses (Slums & Houses)</strong></td>
                <td>3,000L / 5,000L / 7,000L</td>
                <td><span class="badge badge-blue">Rs 2,000 / 2,200 / 2,500</span></td>
                <td>Per Trip: Loading + Cleaning + Outside Dumping included. Standard blue vacuum tanker.</td>
            </tr>
            <tr>
                <td><strong>2. Apartments, Villas, IT Parks & Commercial (G+3)</strong></td>
                <td>3,000L (Small Vehicle)<br>5,000–7,000L (Big Vehicle)</td>
                <td><span class="badge badge-green">Rs 2,500/-<br>Rs 3,000/-</span></td>
                <td>High-capacity vacuum evacuation for multi-storey residential, corporate campuses & labour camps.</td>
            </tr>
            <tr>
                <td><strong>3. Basement, Cellar & Small Access Areas</strong></td>
                <td>Special Small Vehicle</td>
                <td><span class="badge badge-amber">Rs 2,500/- (Per Trip)</span></td>
                <td>Enters low-clearance basements, cellars, and narrow lanes. Full loading, suction & outside dumping.</td>
            </tr>
            <tr>
                <td><strong>4. Grease Trap Cleaning (Hotels / Restaurants)</strong></td>
                <td>3,000L (Small Vehicle)<br>5,000–7,000L (Big Vehicle)</td>
                <td><span class="badge badge-blue">Rs 3,000/-<br>Rs 5,000/-</span></td>
                <td>Cleans grease trap tanks, chambers, crude oil, kitchen food wastage & removes foul smells effectively.</td>
            </tr>
            <tr>
                <td><strong>5. Underground Drainage & Hanging Lines</strong></td>
                <td>High-Pressure Jetting Rig</td>
                <td><span class="badge badge-green">Starts from Rs 2,000/-</span></td>
                <td>Price per one drainage chamber. High-pressure jetting & suction cleaning. Suitable for cellar drainages.</td>
            </tr>
            <tr>
                <td><strong>6. Crude Oil & Industrial Waste Cleaning</strong></td>
                <td>Heavy Chemical Tanker</td>
                <td><span class="badge badge-amber">Custom Quote</span></td>
                <td>Crude oil, sludge & industrial waste cleaning. Safe loading, transport & authorized disposal.</td>
            </tr>
            <tr>
                <td><strong>7. Per One Labour Charges</strong></td>
                <td>Trained Specialist</td>
                <td><span class="badge badge-blue">Rs 2,500/- per labour</span></td>
                <td>To clean drainage line, underground septic tank, sump or wastage sludge cleaning.</td>
            </tr>
            <tr>
                <td><strong>8. Underground Drainage Chamber Clearing</strong></td>
                <td>Chamber Clearing Rig</td>
                <td><span class="badge badge-blue">Rs 2,000/- per chamber</span></td>
                <td>Mechanical de-blocking, silt removal, and flow restoration per chamber.</td>
            </tr>
            <tr>
                <td><strong>9. STP Tanks Cleaning & Major Projects</strong></td>
                <td>7-Chamber Enterprise Unit</td>
                <td><span class="badge badge-green">Free Site Visit & Quote</span></td>
                <td>Commercial apartments, villas, IT parks & industries. Comprehensive on-site inspection and detailed scope quotation.</td>
            </tr>
        </tbody>
    </table>

    <div class="callout" style="margin-top: 10px;">
        <div class="callout-title">Universal Trip Guarantee</div>
        <p>Every single service trip includes: <strong>Septic Tank Loading + Transport + Outside Dumping + Grease Trap & Chamber Cleaning + Safe & Hygienic Service + Trained Operators.</strong></p>
    </div>

    <h2>5. Annual Maintenance Contract (AMC) Tiers</h2>
    <div class="grid-3">
        <div class="card card-accent">
            <h4>Silver Care (Residential)</h4>
            <p><strong>Target:</strong> Small apartments & independent villas</p>
            <ul>
                <li>2 Scheduled septic tank cleanings/year</li>
                <li>Bi-annual drain line inspection</li>
                <li>Priority emergency dispatch</li>
                <li>10% discount on unscheduled callouts</li>
            </ul>
        </div>
        <div class="card card-warn">
            <h4>Gold Care (Commercial F&B)</h4>
            <p><strong>Target:</strong> Restaurants, cafeterias, food courts</p>
            <ul>
                <li>Monthly grease trap de-sludging</li>
                <li>Monthly kitchen drain jetting</li>
                <li>Off-peak night service (after 11 PM)</li>
                <li>GHMC hygiene audit compliance certificate</li>
            </ul>
        </div>
        <div class="card card-success">
            <h4>Platinum Care (IT / Enterprise)</h4>
            <p><strong>Target:</strong> Tech parks, gated townships, hospitals</p>
            <ul>
                <li>Comprehensive quarterly STP servicing</li>
                <li>Quarterly basement drain de-silting</li>
                <li>Hanging pipeline scale removal</li>
                <li>24/7 dedicated account manager & 45-min SLA</li>
            </ul>
        </div>
    </div>
</div>

<!-- PAGE 4: 30-60-90 Day Execution Roadmap -->
<div class="page">
    <div class="header">
        <div>
            <div class="brand-badge">Execution Timeline & KPIs</div>
            <div class="brand-title">DIAL-A-SEPTIC TANK CLEANERS</div>
        </div>
        <div class="header-meta">
            <div>Document: <strong>Business Plan of Action</strong></div>
            <div>Page: <strong>04 of 04</strong></div>
        </div>
    </div>

    <h2>6. Phased 30-60-90 Day Execution Roadmap</h2>

    <div class="grid-3">
        <div class="card card-accent">
            <h4>Phase 1: Days 1 – 30 (Foundation & Digital Dominance)</h4>
            <ul>
                <li><strong>Website Launch:</strong> Deploy high-speed, modern responsive portal with interactive cost estimator and WhatsApp instant book.</li>
                <li><strong>Google Business Profile:</strong> Optimize GMB in Madhapur with primary category "Septic System Service" & "Drainage Service".</li>
                <li><strong>Hyperlocal Landing Pages:</strong> Index 20 target localities (Madhapur, Hitech City, Kondapur, Kokapet, etc.).</li>
                <li><strong>WhatsApp Automation:</strong> Auto-reply with service catalogue, pricing sheet, and live GPS coordination.</li>
            </ul>
        </div>
        <div class="card card-warn">
            <h4>Phase 2: Days 31 – 60 (B2B Outbound & Commercial AMC)</h4>
            <ul>
                <li><strong>Corporate Pitching:</strong> Target top 50 facility management companies (CBRE, JLL, Cushman) operating tech parks in Cyberabad.</li>
                <li><strong>F&B Partnerships:</strong> Direct outreach to 100+ restaurant managers in Jubilee Hills and Madhapur for grease trap AMCs.</li>
                <li><strong>Monsoon Pre-Inspection Drive:</strong> Launch preventive basement and drainage desilting campaigns before heavy rains.</li>
                <li><strong>Customer Feedback Loop:</strong> Implement post-service 5-star Google review collection system via automated SMS.</li>
            </ul>
        </div>
        <div class="card card-success">
            <h4>Phase 3: Days 61 – 90 (Scale, Fleet & Retention)</h4>
            <ul>
                <li><strong>Expanded Fleet Coverage:</strong> Station standby tankers in Gachibowli and Tellapur for sub-30 min response times.</li>
                <li><strong>Contract Renewal Automation:</strong> CRM alerts for scheduled 6-month septic maintenance reminders.</li>
                <li><strong>Construction Site Partnerships:</strong> Bulk portable toilet servicing agreements with tier-1 infrastructure builders.</li>
                <li><strong>Quarterly Performance Review:</strong> Track customer acquisition costs, average job margin, and recurring AMC ratio.</li>
            </ul>
        </div>
    </div>

    <h2>7. Key Performance Indicators (KPIs) to Track</h2>
    <table>
        <thead>
            <tr>
                <th>Key Performance Indicator</th>
                <th>Baseline (Month 1)</th>
                <th>Target (Month 3)</th>
                <th>Target (Month 6)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Monthly Service Callouts</strong></td>
                <td>60 – 80 jobs</td>
                <td>150 – 200 jobs</td>
                <td>350+ jobs</td>
            </tr>
            <tr>
                <td><strong>Recurring AMC Contracts</strong></td>
                <td>5 active contracts</td>
                <td>25 active contracts</td>
                <td>60+ active contracts</td>
            </tr>
            <tr>
                <td><strong>Average Response Time</strong></td>
                <td>60 – 75 minutes</td>
                <td>45 minutes</td>
                <td>30 – 40 minutes</td>
            </tr>
            <tr>
                <td><strong>Google Review Rating</strong></td>
                <td>4.5+ Stars</td>
                <td>4.8+ Stars (150+ reviews)</td>
                <td>4.9 Stars (400+ reviews)</td>
            </tr>
            <tr>
                <td><strong>Commercial Inbound Web Conversion</strong></td>
                <td>3.5%</td>
                <td>7.0%</td>
                <td>10.0%+</td>
            </tr>
        </tbody>
    </table>

    <div class="footer">
        <div>Dial-a-Septic Tank Cleaners • Strategic Operations Blueprint</div>
        <div>Emergency 24/7 Hotline: 80740 14420 | Madhapur, Hyderabad</div>
    </div>
</div>

</body>
</html>
"""

html_file = 'Business_Plan_Of_Action.html'
pdf_file = 'Business_Plan_Of_Action_Dial_A_Septic.pdf'

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Wrote {html_file}")
render_pdf(html_file, pdf_file)
