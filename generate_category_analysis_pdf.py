import os
from pdf_common import COMMON_CSS, render_pdf

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Business Category & Industry Analysis - Dial-a-Septic Tank Cleaners</title>
<style>
{COMMON_CSS}
</style>
</head>
<body>

<!-- PAGE 1: Executive Summary & Category Overview -->
<div class="page">
    <div class="header">
        <div>
            <div class="brand-badge">Comprehensive Research Dossier</div>
            <div class="brand-title">DIAL-A-SEPTIC TANK CLEANERS</div>
        </div>
        <div class="header-meta">
            <div><strong>Location:</strong> Madhapur, Hyderabad</div>
            <div><strong>Industry:</strong> Urban Wastewater & Sanitation Management</div>
            <div><strong>Date:</strong> 2026 Strategic Review</div>
        </div>
    </div>

    <div class="doc-hero">
        <div class="doc-tag">Deliverable 01 / 03 • Market Intelligence</div>
        <h1>Business Category & Industry Analysis</h1>
        <p>In-depth market valuation, competitive landscape, regulatory drivers, customer segmentation, and growth potential for mechanized sanitation, STP, grease trap, and basement drainage services across Hyderabad's prime urban corridors.</p>
    </div>

    <h2>1. Executive Industry Overview</h2>
    <p>
        The urban wastewater management and commercial de-sludging sector in Hyderabad represents a mission-critical, recession-proof municipal utility ecosystem. Historically dominated by fragmented, unorganized informal laborers operating antiquated machinery without regulatory safety protocols, the market is currently undergoing a structural transformation toward <strong>mechanized vacuum suction tankers, high-pressure hydro-jetting, and compliant environmental management</strong>.
    </p>
    <p>
        The rapid vertical expansion of Hyderabad—specifically the Cyberabad IT and Financial District corridors comprising <strong>Madhapur, Gachibowli, Hitech City, Kondapur, Kokapet, and Nanakramguda</strong>—has created dense residential high-rises, expansive commercial tech parks, multi-level basements, and thousands of dining hubs. All of these require round-the-clock, compliant, and odor-free sanitation operations.
    </p>

    <div class="grid-3">
        <div class="card card-accent">
            <h4>Hyper-Growth Territory</h4>
            <p>Over 20 key micro-markets in Western Hyderabad experiencing rapid multi-tier real estate expansion and commercial densification.</p>
        </div>
        <div class="card card-warn">
            <h4>Strict Legal Norms</h4>
            <p>Strict enforcement of Prohibition of Employment as Manual Scavengers Act and GHMC zero-manual-entry rules demanding mechanized suction.</p>
        </div>
        <div class="card card-success">
            <h4>24/7 SLA Urgency</h4>
            <p>Plumbing overflows, grease blockages, and STP failures represent operational emergencies requiring sub-60-minute dispatch response times.</p>
        </div>
    </div>

    <h2>2. Market Dynamics & Growth Drivers in Hyderabad</h2>
    <ul>
        <li><strong>Commercial Densification & Tech Corridors:</strong> Grade-A IT parks, multinational campuses, and co-working spaces operate centralized Sewage Treatment Plants (STPs) and commercial grease interceptors that require strict periodic maintenance to avert corporate downtime.</li>
        <li><strong>High-Rise Multi-Level Basements (B1, B2, B3):</strong> Modern residential towers and malls feature underground parking and drainage networks beneath the municipal sewer line. Gravity-defying pumping systems accumulate heavy sludge and demand specialized low-clearance or high-lift suction equipment.</li>
        <li><strong>Food & Beverage (F&B) Boom:</strong> The exponential growth of cloud kitchens, cafeterias, and casual dining outlets across Jubilee Hills, Madhapur, and Gachibowli has elevated grease trap de-sludging from an occasional chore to a mandatory bi-weekly hygiene compliance requirement.</li>
        <li><strong>Construction & Labour Camp Sanitation:</strong> Infrastructure megaprojects and real estate developments require mobile portable toilet deployment and scheduled septic evacuations to maintain worker health and environmental compliance.</li>
    </ul>
</div>

<!-- PAGE 2: Service Verticals Deep Dive -->
<div class="page">
    <div class="header">
        <div>
            <div class="brand-badge">Category Analysis: Service Verticals</div>
            <div class="brand-title">DIAL-A-SEPTIC TANK CLEANERS</div>
        </div>
        <div class="header-meta">
            <div>Document: <strong>Category Analysis</strong></div>
            <div>Page: <strong>02 of 04</strong></div>
        </div>
    </div>

    <h2>3. Comprehensive Breakdown of the 6 Core Service Verticals</h2>
    <p>Dial-a-Septic Tank Cleaners' service portfolio spans residential hygiene to complex industrial wastewater operations:</p>

    <table>
        <thead>
            <tr>
                <th style="width: 22%;">Service Category</th>
                <th style="width: 28%;">Operational Scope</th>
                <th style="width: 25%;">Target Client Base</th>
                <th style="width: 25%;">Technical Requirements</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>1. Septic Tank Cleaning (Houses & Apartments)</strong></td>
                <td>Liquid extraction, bottom sludge de-caking, loading, cleaning & outside dumping</td>
                <td>Individual houses, villas, apartments, IT parks, labour camps, commercial buildings</td>
                <td>Small Vehicles (3,000L) & Big Vehicles (5,000L – 7,000L) with high-vacuum pumps</td>
            </tr>
            <tr>
                <td><strong>2. Drainage Cleaning & De-clogging</strong></td>
                <td>Clearing mainline blockages, tree root ingress, silt accumulation, flow restoration</td>
                <td>Apartment societies, commercial complexes, industrial sheds, hospitals</td>
                <td>High-pressure hydro-jetting rigs, suction cleaning per drainage chamber (starts Rs 2,000/-)</td>
            </tr>
            <tr>
                <td><strong>3. STP Tank Cleaning & Major Projects</strong></td>
                <td>Bar screen de-trashing, collection tank de-silting, SBR & Aeration de-sludging, filter feed tanks</td>
                <td>IT parks, commercial towers, gated townships, hotels, hospitals</td>
                <td>Full on-site inspection, industrial vacuum units, gas detectors, authorized decanting</td>
            </tr>
            <tr>
                <td><strong>4. Grease Trap Cleaning</strong></td>
                <td>Extraction of Fats, Oils & Grease (FOG), bio-waste removal, odor elimination</td>
                <td>Hotels, restaurants, canteens, corporate cafeterias, cloud kitchens</td>
                <td>Small Vehicle (3,000L) & Big Vehicle (5,000–7,000L), hot-water hydro jetting</td>
            </tr>
            <tr>
                <td><strong>5. Cellar / Basement & Restricted Access</strong></td>
                <td>Underground drainage, hanging pipeline descaling, sump suction in low-clearance decks</td>
                <td>Basements, cellars, narrow access lanes, high-rise parking floors</td>
                <td>Special small low-profile vehicle provided for tight access areas (Fixed Rs 2,500/- per trip)</td>
            </tr>
            <tr>
                <td><strong>6. Crude Oil & Industrial Waste Cleaning</strong></td>
                <td>Crude oil, industrial chemical sludge, factory wastewater evacuation</td>
                <td>Manufacturing facilities, automotive hubs, industrial estates</td>
                <td>Chemical-resistant vacuum tankers, trained operators, authorized industrial dumping</td>
            </tr>
        </tbody>
    </table>

    <div class="callout">
        <div class="callout-title">Standard Trip Inclusions & Customer Guarantee</div>
        <p>Every single service execution includes: <strong>Septic Tank Loading + Transport + Outside Dumping + Grease Trap & Chamber Cleaning + Safe & Hygienic Service + Trained Operators.</strong> Plus specialized trained labour support available at Rs 2,500/- per labour.</p>
    </div>
</div>

<!-- PAGE 3: Customer Personas & Market Segmentation -->
<div class="page">
    <div class="header">
        <div>
            <div class="brand-badge">Target Audience & Competitor Matrix</div>
            <div class="brand-title">DIAL-A-SEPTIC TANK CLEANERS</div>
        </div>
        <div class="header-meta">
            <div>Document: <strong>Category Analysis</strong></div>
            <div>Page: <strong>03 of 04</strong></div>
        </div>
    </div>

    <h2>4. Customer Persona & Segmentation Matrix</h2>

    <div class="grid-2">
        <div class="card card-accent">
            <h4>Persona A: Gated Society RWA President / Facility Manager</h4>
            <ul>
                <li><strong>Profile:</strong> Managing 200–1,500 apartment units in Kondapur, Nallagandla, or Tellapur.</li>
                <li><strong>Pain Points:</strong> Overflowing sewage sumps causing resident outrage, foul odors, unpunctual informal vendors, lack of GST invoicing.</li>
                <li><strong>Buying Triggers:</strong> Formal GST billing, reliable 24/7 SLA, certified equipment, neat and odor-controlled execution.</li>
            </ul>
        </div>
        <div class="card card-accent">
            <h4>Persona B: Commercial IT Park Operations Head</h4>
            <ul>
                <li><strong>Profile:</strong> Tech park facilities in Hitech City, Madhapur, and Gachibowli.</li>
                <li><strong>Pain Points:</strong> STP breakdown disrupting operations, environmental compliance audits, safety liability with manual labor.</li>
                <li><strong>Buying Triggers:</strong> 100% mechanized process, zero-manual-scavenging compliance, trained PPE-clad workforce, AMC retainers.</li>
            </ul>
        </div>
        <div class="card card-warn">
            <h4>Persona C: Restaurant / Cloud Kitchen General Manager</h4>
            <ul>
                <li><strong>Profile:</strong> F&B outlets in Jubilee Hills, Madhapur, Hitech City food courts.</li>
                <li><strong>Pain Points:</strong> Blocked sinks during peak dinner rushes, stench invading customer dining areas, GHMC food health inspection penalties.</li>
                <li><strong>Buying Triggers:</strong> Rapid emergency response, off-peak night cleaning (11 PM - 6 AM), grease disposal certification.</li>
            </ul>
        </div>
        <div class="card card-success">
            <h4>Persona D: Construction Project Infrastructure Lead</h4>
            <ul>
                <li><strong>Profile:</strong> Project managers at construction sites in Kokapet, Kollur, Manikonda.</li>
                <li><strong>Pain Points:</strong> Unhygienic labor camps leading to workforce attrition and sickness, lack of municipal drainage connections.</li>
                <li><strong>Buying Triggers:</strong> Punctual scheduled vacuum evacuation, bulk pricing, portable toilet supply and upkeep contracts.</li>
            </ul>
        </div>
    </div>

    <h2>5. Competitive Landscape: Informal vs. Modern Mechanics</h2>
    <table>
        <thead>
            <tr>
                <th>Factor</th>
                <th>Traditional Local Tankers</th>
                <th>Dial-a-Septic Tank Cleaners</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Availability</strong></td>
                <td>Unpredictable, daytime only</td>
                <td><span class="badge badge-green">Guaranteed 24/7/365 Emergency Dispatch</span></td>
            </tr>
            <tr>
                <td><strong>Machinery & Reach</strong></td>
                <td>Basic single-stage pumps, short hoses</td>
                <td><span class="badge badge-blue">High-vacuum multi-stage, B1-B3 reach, 100m+ hoses</span></td>
            </tr>
            <tr>
                <td><strong>Safety & Legal</strong></td>
                <td>Hazardous manual intervention, no PPE</td>
                <td><span class="badge badge-green">100% Mechanized, Full PPE, Zero Manual Scavenging</span></td>
            </tr>
            <tr>
                <td><strong>Pricing Transparency</strong></td>
                <td>Arbitrary haggling on arrival</td>
                <td><span class="badge badge-blue">Transparent upfront quotes, formal GST invoicing</span></td>
            </tr>
            <tr>
                <td><strong>Digital Accessibility</strong></td>
                <td>Word of mouth or painted wall signs</td>
                <td><span class="badge badge-green">Modern interactive web portal, WhatsApp instant book</span></td>
            </tr>
        </tbody>
    </table>
</div>

<!-- PAGE 4: SWOT & Regulatory Compliance -->
<div class="page">
    <div class="header">
        <div>
            <div class="brand-badge">Strategic Analysis & Compliance</div>
            <div class="brand-title">DIAL-A-SEPTIC TANK CLEANERS</div>
        </div>
        <div class="header-meta">
            <div>Document: <strong>Category Analysis</strong></div>
            <div>Page: <strong>04 of 04</strong></div>
        </div>
    </div>

    <h2>6. Strategic SWOT Analysis</h2>
    <div class="grid-2">
        <div class="card card-success">
            <h4>STRENGTHS (Internal)</h4>
            <ul>
                <li>Centralized headquarters in Patrika Nagar, Madhapur — minutes from high-density tech corridors.</li>
                <li>Multi-vertical competence: Septic, STP, Drainage, Grease Trap, Basements, and Portable Toilets under one roof.</li>
                <li>24/7 dedicated dispatch with established 1+ year operating track record.</li>
                <li>Multi-level basement (B1/B2/B3) deep-suction capabilities.</li>
            </ul>
        </div>
        <div class="card card-warn">
            <h4>WEAKNESSES (Internal)</h4>
            <ul>
                <li>Brand currently relies heavily on manual phone inquiries; needs automated digital conversion funnel.</li>
                <li>Customer perception of the sanitation sector tends to be low-tech unless brand identity is modernized.</li>
                <li>Fleet scale requires careful dispatch orchestration during peak monsoon emergency surges.</li>
            </ul>
        </div>
        <div class="card card-accent">
            <h4>OPPORTUNITIES (External)</h4>
            <ul>
                <li>Recurring Annual Maintenance Contracts (AMC) with gated societies and corporate IT parks.</li>
                <li>Monsoon prep packages (June-October) for basement drain protection against urban flooding.</li>
                <li>Hyperlocal SEO dominance for 20 western Hyderabad localities.</li>
                <li>Green wastewater transport certifications appeal to ESG-conscious corporates.</li>
            </ul>
        </div>
        <div class="card card-accent">
            <h4>THREATS (External)</h4>
            <ul>
                <li>Price undercutting by illegal, unorganized operators dumping waste indiscriminately.</li>
                <li>Traffic gridlock in Cyberabad during peak hours impacting rapid response SLAs.</li>
                <li>Changing municipal disposal tariffs at designated sewage treatment plants.</li>
            </ul>
        </div>
    </div>

    <h2>7. Regulatory, Environmental & Safety Mandates</h2>
    <div class="highlight-box">
        <h4 style="color: #0369a1; margin-bottom: 6px;">Statutory Compliance Standards:</h4>
        <p style="margin-bottom: 6px;">
            • <strong>Zero Manual Entry:</strong> Strict compliance with the <em>Employment of Manual Scavengers and Construction of Dry Latrines (Prohibition) Act</em>. 100% mechanized suction and camera inspection.
        </p>
        <p style="margin-bottom: 6px;">
            • <strong>Confined Space Safety:</strong> Gas monitoring detectors for Hydrogen Sulfide (H2S), Methane (CH4), and Carbon Monoxide before opening sealed chambers.
        </p>
        <p style="margin-bottom: 0;">
            • <strong>Authorized Environmental Disposal:</strong> Transporting septage exclusively to designated GHMC / HMWSSB decanting facilities and licensed STPs to prevent environmental contamination.
        </p>
    </div>

    <div class="footer">
        <div>Dial-a-Septic Tank Cleaners • Confidential Strategic Dossier</div>
        <div>Contact: 80740 14420 | Madhapur, Hyderabad</div>
    </div>
</div>

</body>
</html>
"""

html_file = 'Business_Category_Analysis.html'
pdf_file = 'Business_Category_Analysis_Dial_A_Septic.pdf'

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Wrote {html_file}")
render_pdf(html_file, pdf_file)
