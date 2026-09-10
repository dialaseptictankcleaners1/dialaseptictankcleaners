import os
from pdf_common import COMMON_CSS, render_pdf

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Website Design Layout & Information Architecture - Dial-a-Septic Tank Cleaners</title>
<style>
{COMMON_CSS}
.wireframe-box {{
    background: #f1f5f9;
    border: 2px dashed #94a3b8;
    border-radius: 6px;
    padding: 10px;
    text-align: center;
    font-size: 11px;
    font-weight: 600;
    color: #475569;
    margin-bottom: 8px;
}}
.color-swatch {{
    display: inline-block;
    width: 28px;
    height: 28px;
    border-radius: 6px;
    vertical-align: middle;
    margin-right: 8px;
    border: 1px solid rgba(0,0,0,0.1);
}}
</style>
</head>
<body>

<!-- PAGE 1: Design Philosophy, Aesthetics & Design System -->
<div class="page">
    <div class="header">
        <div>
            <div class="brand-badge">UI/UX & Frontend Architecture</div>
            <div class="brand-title">DIAL-A-SEPTIC TANK CLEANERS</div>
        </div>
        <div class="header-meta">
            <div><strong>Location:</strong> Madhapur, Hyderabad</div>
            <div><strong>Platform:</strong> High-Performance Web Portal</div>
            <div><strong>Date:</strong> 2026 UX Design Specs</div>
        </div>
    </div>

    <div class="doc-hero">
        <div class="doc-tag">Deliverable 03 / 03 • Technical Design Document</div>
        <h1>Website Design Layout, Wireframe Structure & UI/UX Architecture</h1>
        <p>A comprehensive design blueprint creating a high-conversion, visually striking, and trustworthy web presence. Details the complete information architecture, color theory, typography, interactive modules, and mobile-first CRO patterns.</p>
    </div>

    <h2>1. Design Philosophy: "Industrial Modernity & Pristine Trust"</h2>
    <p>
        The typical sanitation and septic cleaning website in India suffers from dated 2005-era designs, low-resolution clip-art, garish text, and poor mobile readability. Dial-a-Septic Tank Cleaners requires an <strong>ultra-premium, modern environmental engineering aesthetic</strong> that immediately conveys:
    </p>
    <ul>
        <li><strong>Institutional Credibility:</strong> Looks like a corporate environmental services leader that IT park facility directors and gated community RWAs can trust without hesitation.</li>
        <li><strong>High-Urgency Frictionless Accessibility:</strong> For panicked homeowners facing a sewage overflow at 2 AM, one click immediately initiates a phone call or WhatsApp dispatch with zero barriers.</li>
        <li><strong>Modern Micro-Interactions:</strong> Clean subtle glassmorphism cards, dynamic interactive cost calculator, hover reveals, and sleek badge accents that feel responsive and alive.</li>
    </ul>

    <h2>2. Visual Design System & Design Tokens</h2>
    <div class="grid-2">
        <div class="card card-accent">
            <h4>Color Palette Tokens</h4>
            <table style="margin: 6px 0;">
                <tr>
                    <td><span class="color-swatch" style="background: #0a192f;"></span></td>
                    <td><strong>Deep Navy</strong> (<code>#0A192F</code>)</td>
                    <td>Primary background, headers, luxury stability</td>
                </tr>
                <tr>
                    <td><span class="color-swatch" style="background: #0284c7;"></span></td>
                    <td><strong>Oceanic Blue</strong> (<code>#0284C7</code>)</td>
                    <td>Primary brand accent, interactive elements</td>
                </tr>
                <tr>
                    <td><span class="color-swatch" style="background: #06b6d4;"></span></td>
                    <td><strong>Eco Cyan</strong> (<code>#06B6D4</code>)</td>
                    <td>Clean water/environmental highlights, gradients</td>
                </tr>
                <tr>
                    <td><span class="color-swatch" style="background: #f59e0b;"></span></td>
                    <td><strong>Amber Alert</strong> (<code>#F59E0B</code>)</td>
                    <td>24/7 emergency dispatch tags, urgent callouts</td>
                </tr>
                <tr>
                    <td><span class="color-swatch" style="background: #22c55e;"></span></td>
                    <td><strong>WhatsApp Green</strong> (<code>#22C55E</code>)</td>
                    <td>Direct booking triggers, active dispatch status</td>
                </tr>
                <tr>
                    <td><span class="color-swatch" style="background: #f8fafc;"></span></td>
                    <td><strong>Crisp Slate</strong> (<code>#F8FAFC</code>)</td>
                    <td>Clean body surface, contrast cards</td>
                </tr>
            </table>
        </div>

        <div class="card card-accent">
            <h4>Typography & Component Styling</h4>
            <ul>
                <li><strong>Primary Display Font:</strong> <code>Space Grotesk</code> (Google Font) — clean, modern, architectural headers with authoritative technical feel.</li>
                <li><strong>Body & Interface Font:</strong> <code>Plus Jakarta Sans</code> (Google Font) — ultra-legible, geometric sans-serif optimized for mobile screens.</li>
                <li><strong>Card Elevations:</strong> Subtle layered box shadows (<code>0 10px 30px -10px rgba(2,132,199,0.12)</code>) with 1px border highlights for a refined look.</li>
                <li><strong>Glassmorphic Badges:</strong> Semi-transparent frosted pill tags for 24/7 status, ratings, and certifications.</li>
                <li><strong>Iconography:</strong> High-contrast SVG line icons for all 6 service categories (pumps, hydro-jets, STP tanks, grease traps, portable units, basement layers).</li>
            </ul>
        </div>
    </div>
</div>

<!-- PAGE 2: Full Sitemap & Page Architecture -->
<div class="page">
    <div class="header">
        <div>
            <div class="brand-badge">Sitemap & Page Hierarchy</div>
            <div class="brand-title">DIAL-A-SEPTIC TANK CLEANERS</div>
        </div>
        <div class="header-meta">
            <div>Document: <strong>Design Layout & Structure</strong></div>
            <div>Page: <strong>02 of 04</strong></div>
        </div>
    </div>

    <h2>3. Complete Website Information Architecture (Sitemap)</h2>
    <p>A comprehensive single-page progressive disclosure architecture with dedicated deep-dive sections to maximize conversion flow and local SEO indexing:</p>

    <div class="card card-accent" style="margin-bottom: 16px;">
        <h4>1. Utility Top Bar (Always Visible)</h4>
        <p>• 24/7 Emergency Dispatch Hotline: <strong>80740 14420</strong> | • Direct Email: <strong>dailaseptictankcleaners@gmail.com</strong> | • Operating Hours: <strong>24/7 All Days</strong> | • Location: <strong>Madhapur, Hyderabad</strong></p>
    </div>

    <div class="card card-accent" style="margin-bottom: 16px;">
        <h4>2. Navigation Header (Sticky Glassmorphism)</h4>
        <p>• Brand Logo with mechanized tanker insignia | • Links: Services, B1-B3 Basements, STP Solutions, Service Areas, Pricing Estimator, Safety & Compliance | • CTAs: <strong>"Call Now"</strong> (Tel link) & <strong>"Book on WhatsApp"</strong></p>
    </div>

    <div class="card card-accent" style="margin-bottom: 16px;">
        <h4>3. Hero Section with Dual Urgency Triggers</h4>
        <p>• Headline: <em>"Professional 24/7 Septic Tank, Drainage & STP Cleaning in Hyderabad"</em><br>
        • Subtitle: <em>"100% Mechanized Vacuum Suction • B1/B2/B3 Basements • Residential, Commercial & IT Parks • 45-Minute Arrival SLA"</em><br>
        • Trust Badges: 1+ Years in Business • 24/7 Dispatch • Zero Manual Entry • GHMC Compliant<br>
        • Embedded Rapid Booking Card: Quick Service Selector + Phone Number input + "Request Immediate Dispatch"</p>
    </div>

    <div class="card card-accent" style="margin-bottom: 16px;">
        <h4>4. Live Dispatch Ticker & Trust Highlights</h4>
        <p>• Dynamic alert ticker: <em>"Current Status: Active Tankers Available in Madhapur, Gachibowli, Hitech City, Kondapur & Kokapet"</em><br>
        • Stat counter: <strong>1,200+ Jobs Completed</strong> • <strong>45-Min Avg Response</strong> • <strong>100% Mechanized</strong> • <strong>20+ Service Areas</strong></p>
    </div>

    <div class="card card-accent" style="margin-bottom: 16px;">
        <h4>5. The 6 Core Service Showcase (Interactive Tabs & Modals)</h4>
        <p>
            1. <strong>Septic Tank Cleaning:</strong> Residential villas, high-rises, commercial buildings, industrial facilities.<br>
            2. <strong>Drainage Cleaning:</strong> Choke clearance, high-pressure water jetting, sludge removal.<br>
            3. <strong>STP Tank Cleaning:</strong> Bar screen, raw sewage, SBR, sludge holding, aeration, treated water & filter feed tanks.<br>
            4. <strong>Grease Trap Cleaning:</strong> Restaurants, cloud kitchens, hotels, food courts, cafeterias.<br>
            5. <strong>Portable Toilet Cleaning:</strong> Construction sites, labour camps, events, IT parks, temporary bathrooms.<br>
            6. <strong>Basement Drainage (B1/B2/B3):</strong> Multi-level underground sumps, hanging pipelines, low-clearance suction.
        </p>
    </div>
</div>

<!-- PAGE 3: Interactive Features & Wireframe Layout -->
<div class="page">
    <div class="header">
        <div>
            <div class="brand-badge">Interactive Features & Wireframes</div>
            <div class="brand-title">DIAL-A-SEPTIC TANK CLEANERS</div>
        </div>
        <div class="header-meta">
            <div>Document: <strong>Design Layout & Structure</strong></div>
            <div>Page: <strong>03 of 04</strong></div>
        </div>
    </div>

    <h2>4. Wireframe Structure of Key Interactive Modules</h2>

    <div class="grid-2">
        <div>
            <h3>Wireframe: Interactive Cost Estimator</h3>
            <div class="card">
                <div class="wireframe-box">Step 1: Choose Property Type (Residential Villa / Apartment / IT Park / Restaurant / Construction)</div>
                <div class="wireframe-box">Step 2: Select Service Required (Septic Suction / STP / Grease Trap / Drain Jetting / Basement)</div>
                <div class="wireframe-box">Step 3: Select Basement Level (Ground / B1 / B2 / B3) & Estimated Capacity</div>
                <div class="wireframe-box" style="background: #e0f2fe; border-color: #0284c7; color: #0369a1;">
                    Estimated Cost Range: ₹2,500 – ₹4,500<br>
                    <span style="font-size: 10px;">Includes vacuum extraction, hose setup & deodorization</span>
                </div>
                <div class="wireframe-box" style="background: #22c55e; color: white; border: none; font-weight: 700;">
                    Book This Estimate on WhatsApp (Pre-filled Message)
                </div>
            </div>
        </div>

        <div>
            <h3>Wireframe: 20 Service Locality Hub Matrix</h3>
            <div class="card">
                <p style="font-size: 11px; margin-bottom: 8px;">Interactive clickable area pills that filter local tanker availability and dispatch times:</p>
                <div style="display: flex; flex-wrap: wrap; gap: 4px;">
                    <span class="badge badge-blue">1. Madhapur (HQ)</span>
                    <span class="badge badge-blue">2. Gachibowli</span>
                    <span class="badge badge-blue">3. Hitech City</span>
                    <span class="badge badge-blue">4. Kondapur</span>
                    <span class="badge badge-blue">5. Khajaguda</span>
                    <span class="badge badge-blue">6. Manikonda</span>
                    <span class="badge badge-blue">7. Narsingi</span>
                    <span class="badge badge-blue">8. Nanakramguda</span>
                    <span class="badge badge-blue">9. Kukatpally</span>
                    <span class="badge badge-blue">10. Hafeezpet</span>
                    <span class="badge badge-blue">11. Kokapet</span>
                    <span class="badge badge-blue">12. Jubilee Hills</span>
                    <span class="badge badge-blue">13. Raidurgam</span>
                    <span class="badge badge-blue">14. Kothaguda</span>
                    <span class="badge badge-blue">15. Borabanda</span>
                    <span class="badge badge-blue">16. Lingampally</span>
                    <span class="badge badge-blue">17. Nallagandla</span>
                    <span class="badge badge-blue">18. Gowlidoddi</span>
                    <span class="badge badge-blue">19. Tellapur</span>
                    <span class="badge badge-blue">20. Kollur</span>
                </div>
                <div class="callout" style="margin-top: 10px; padding: 8px 10px; font-size: 11px;">
                    <strong>Local SEO Advantage:</strong> Each locality has targeted schema markup and geo-coordinates for hyper-local Google indexing.
                </div>
            </div>
        </div>
    </div>

    <h2>5. Specialized Feature Modules</h2>
    <div class="grid-2">
        <div class="card card-warn">
            <h4>B1 / B2 / B3 Deep Basement Suction Showcase</h4>
            <p>Visual cross-section graphic illustrating low-clearance vehicle entry into B1, B2, and B3 parking decks with high-head vacuum booster lines to prevent pump cavitations. Crucial for high-rise commercial buildings.</p>
        </div>
        <div class="card card-accent">
            <h4>STP 7-Chamber Technical Tour</h4>
            <p>Interactive tabbed component breaking down specialized cleaning of: Bar Screen Chamber, Collection/Raw Sewage Tank, SBR Tank, Sludge Holding Tank, Aeration Tank, Treated Water Tank, and Filter Feed Tank.</p>
        </div>
    </div>
</div>

<!-- PAGE 4: CRO, Mobile Layout & Technical SEO -->
<div class="page">
    <div class="header">
        <div>
            <div class="brand-badge">CRO, Mobile & Technical SEO</div>
            <div class="brand-title">DIAL-A-SEPTIC TANK CLEANERS</div>
        </div>
        <div class="header-meta">
            <div>Document: <strong>Design Layout & Structure</strong></div>
            <div>Page: <strong>04 of 04</strong></div>
        </div>
    </div>

    <h2>6. Mobile-First Conversion Rate Optimization (CRO) Blueprint</h2>
    <p>Over 80% of emergency septic and drain inquiries originate from mobile smartphones while users are physically on-site examining an overflow. The mobile experience must be frictionless:</p>

    <div class="grid-3">
        <div class="card card-success">
            <h4>Sticky Bottom Emergency Bar</h4>
            <p>Fixed bottom bar with two primary buttons: <strong>"📞 Call 24/7 (80740 14420)"</strong> and <strong>"💬 WhatsApp Instant Dispatch"</strong>. Ensures instant conversion anytime during scrolling.</p>
        </div>
        <div class="card card-accent">
            <h4>1-Tap Pre-filled WhatsApp</h4>
            <p>Clicking WhatsApp launches a pre-configured text: <em>"Hello Dial-a-Septic, I need emergency cleaning for [Service] in [Locality]. Please share tanker ETA."</em></p>
        </div>
        <div class="card card-warn">
            <h4>Zero-Lag Performance</h4>
            <p>Engineered in Vanilla CSS and lightweight modern JS without bloated heavy frameworks to guarantee a sub-1.0s First Contentful Paint on mobile 4G/5G networks.</p>
        </div>
    </div>

    <h2>7. Technical Architecture & Local SEO Best Practices</h2>
    <table>
        <thead>
            <tr>
                <th style="width: 25%;">Component</th>
                <th style="width: 35%;">Implementation Standard</th>
                <th style="width: 40%;">Impact & Outcome</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Schema.org Structured Data</strong></td>
                <td><code>PlumbingService</code> & <code>LocalBusiness</code> JSON-LD markup with geo-coordinates, hours: "Mo-Su 00:00-24:00"</td>
                <td>Enables rich Google search snippets, direct call buttons in search results, and local pack rankings.</td>
            </tr>
            <tr>
                <td><strong>Semantic Heading Structure</strong></td>
                <td>Single <code>&lt;h1&gt;</code> for primary service proposition, logical <code>&lt;h2&gt;</code> for 6 verticals, <code>&lt;h3&gt;</code> for STP components</td>
                <td>Flawless accessibility and clear topical authority signals to search engine crawlers.</td>
            </tr>
            <tr>
                <td><strong>Accessibility & Performance</strong></td>
                <td>WCAG AA contrast ratios, responsive touch targets (48px+), descriptive ARIA labels</td>
                <td>Perfect usability for facility managers in dimly lit basements or outside in bright sunlight.</td>
            </tr>
            <tr>
                <td><strong>Lead Storage & Telemetry</strong></td>
                <td>Local booking state, instant mailto/tel integration, and WhatsApp webhook triggers</td>
                <td>Zero lost leads; dual notification to business phone and inbox.</td>
            </tr>
        </tbody>
    </table>

    <div class="callout">
        <div class="callout-title">Summary of Website Implementation Phases</div>
        <p>Following approval of this structural blueprint, the website will be developed as an extraordinary, modern, interactive, and responsive web application featuring custom SVG graphics, dynamic cost calculator, interactive STP visualizer, basement level selector, locality filter, and full conversion hooks.</p>
    </div>

    <div class="footer">
        <div>Dial-a-Septic Tank Cleaners • Web Architecture & UX Specification</div>
        <div>Contact: 80740 14420 | www.dailaseptictankcleaners.com</div>
    </div>
</div>

</body>
</html>
"""

html_file = 'Website_Design_Layout_And_Structure.html'
pdf_file = 'Website_Design_Layout_And_Structure_Dial_A_Septic.pdf'

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Wrote {html_file}")
render_pdf(html_file, pdf_file)
