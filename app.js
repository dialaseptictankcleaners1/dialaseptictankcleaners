/* ==========================================================================
   DIAL-A-SEPTIC TANK CLEANERS - CLIENT JAVASCRIPT
   Interactive Quote Calculator, Locality Dispatcher, Service Modals, WhatsApp
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initHeroVideo();
  initCalculator();
  initLocalities();
  initServiceModals();
  initBookingForms();
  initStatsCounter();
  initVideoShowcase();
  initTestimonialVideos();
  initHeroTextAnimation();
  initScrollReveals();
  initLegalTOC();
  initCookieConsent();
});

// Primary Phone & WhatsApp Number
const PHONE_NUMBER = "918074014420";
const DISPLAY_PHONE = "80740 14420";

/* --------------------------------------------------------------------------
   1. NAVBAR & STICKY HEADER
   -------------------------------------------------------------------------- */
function initNavbar() {
  const header = document.querySelector('.header-nav');
  const mobileToggle = document.getElementById('mobileToggle');
  const navMenu = document.getElementById('navMenu');

  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 40) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      navMenu.classList.toggle('open');
    });

    // Close menu when clicking nav links
    navMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
      });
    });
  }
}

/* --------------------------------------------------------------------------
   2. INTERACTIVE COST ESTIMATOR / CALCULATOR (MATCHING VERIFIED RATE CARD)
   -------------------------------------------------------------------------- */
const PRICING_DATA = {
  septic: {
    name: "Septic Tank Cleaning",
    villa: { price: "Rs 2,000 – Rs 2,500", tanker: "Small / Standard Tanker (3,000L – 7,000L)", time: "40 – 60 mins", inclusions: ["Per Trip: Loading + Cleaning + Outside Dumping", "3,000L = Rs 2,000 | 5,000L = Rs 2,200 | 7,000L = Rs 2,500", "100% mechanized high-vacuum suction", "Safe, hygienic, and odor-free disposal"] },
    apartment: { price: "Rs 2,500 – Rs 3,000", tanker: "Small (3,000L) or Big Vehicle (5,000–7,000L)", time: "45 – 75 mins", inclusions: ["Per Trip: Loading + Cleaning + Outside Dumping", "3,000L Small Vehicle = Rs 2,500", "5,000L – 7,000L Big Vehicle = Rs 3,000", "Strict zero manual entry compliance"] },
    itpark: { price: "Rs 2,500 – Rs 3,000/trip", tanker: "Commercial Dedicated Fleet", time: "Scheduled Service", inclusions: ["Commercial rate: 3,000L = Rs 2,500 | 5,000–7,000L = Rs 3,000", "Trained & uniform operators with full PPE", "Loading, cleaning & outside dumping included", "GST invoice & corporate compliance certificate"] },
    restaurant: { price: "Rs 2,500 – Rs 3,000", tanker: "Commercial Rapid Tanker", time: "45 mins", inclusions: ["Per Trip: Loading + Cleaning + Outside Dumping", "Small Vehicle = Rs 2,500 | Big Vehicle = Rs 3,000", "Quick turnaround to avoid kitchen downtime", "Outside dumping at authorized municipal facility"] },
    construction: { price: "Rs 2,500 – Rs 3,000/trip", tanker: "Heavy Duty Tanker (3,000L – 7,000L)", time: "60 mins", inclusions: ["Per Trip: Loading + Cleaning + Outside Dumping", "Small Vehicle = Rs 2,500 | Big Vehicle = Rs 3,000", "Ideal for labour camps and construction septic pits", "Scheduled daily or weekly cycle available"] }
  },
  drainage: {
    name: "Drainage & Sewer Line Jetting",
    villa: { price: "Starts from Rs 2,000", tanker: "High-Pressure Jetting & Suction Rig", time: "30 – 50 mins", inclusions: ["Rs 2,000/- Per One Drainage Chamber", "High-pressure hydro-jetting & suction cleaning", "Removes blockages, sludge, and foul smell", "Suitable for underground lines & hanging lines"] },
    apartment: { price: "Starts from Rs 2,000/chamber", tanker: "High-Pressure Jetting Unit", time: "1 – 2 hours", inclusions: ["Rs 2,000/- Per Drainage Chamber", "Chamber-by-chamber silt and blockage clearing", "Removes stubborn debris, grease, and roots", "Restores uninterrupted wastewater gravity flow"] },
    itpark: { price: "Starts from Rs 2,000/chamber", tanker: "Heavy Industrial Jetting Rig", time: "Custom Scope", inclusions: ["Rs 2,000/- Per Drainage Chamber", "Cellar & hanging line drainage cleaning", "Trained operators with safety gas meters", "Includes pipeline flow verification"] },
    restaurant: { price: "Starts from Rs 2,000/chamber", tanker: "Thermal Grease Jetting Rig", time: "45 mins", inclusions: ["Rs 2,000/- Per Kitchen Chamber", "High-pressure clearance of fat and food sludge", "Eliminates drain stench and foul odor", "Night execution available"] },
    construction: { price: "Starts from Rs 2,000/chamber", tanker: "Heavy Sludge Jetting Unit", time: "60 mins", inclusions: ["Rs 2,000/- Per Drainage Chamber", "Clears mud, cement silt, and site runoff", "High-volume suction and water blasting", "Safe outside dumping"] }
  },
  stp: {
    name: "STP Tanks Cleaning & Projects",
    villa: { price: "Custom Inspection Quote", tanker: "Specialized STP Suction Unit", time: "Site Visit Required", inclusions: ["Free site visit & comprehensive inspection", "Detailed transparent quote with scope of work", "Cleaning of collection, aeration & treated tanks", "Loading, transport & outside dumping"] },
    apartment: { price: "On-Site Inspection Quote", tanker: "Heavy STP Extraction Fleet", time: "Site Visit Required", inclusions: ["We visit, inspect and give you a good quotation", "Detailed scope of work covering all chambers", "In commercial apartments, villas & societies", "Experienced & trained operators"] },
    itpark: { price: "Formal Tender / AMC Quote", tanker: "Enterprise STP Overhaul Fleet", time: "Site Visit Required", inclusions: ["Comprehensive site inspection & technical quotation", "Covers Bar Screen, Raw Sewage, SBR & Sludge tanks", "Full safety protocols (Gas detection, PPE)", "Authorized environmental disposal logs"] },
    restaurant: { price: "On-Site Inspection Quote", tanker: "Commercial Bio-STP Unit", time: "Site Visit Required", inclusions: ["Inspection and quotation based on chamber capacity", "Grease and bio-reactor de-sludging", "Odor removal & outside dumping included", "Flexible maintenance schedules"] },
    construction: { price: "Custom Project Quote", tanker: "Site Silt & STP Unit", time: "Site Visit Required", inclusions: ["On-site inspection and detailed project quotation", "Sedimentation and treatment tank cleanout", "High-capacity loading and outside dumping", "Full regulatory compliance"] }
  },
  grease: {
    name: "Grease Trap Cleaning (Hotel / Restaurant / Canteen)",
    villa: { price: "Rs 3,000 – Rs 5,000", tanker: "Grease Extraction Unit", time: "30 mins", inclusions: ["3,000 Litres (Small Vehicle) = Rs 3,000/-", "5,000L – 7,000L (Big Vehicle) = Rs 5,000/-", "Cleans grease trap tanks, chambers & food waste", "Removes foul odors effectively"] },
    apartment: { price: "Rs 3,000 – Rs 5,000", tanker: "Grease & Chamber Rig", time: "45 mins", inclusions: ["Small Vehicle (3,000L) = Rs 3,000/-", "Big Vehicle (5,000–7,000L) = Rs 5,000/-", "Clubhouse / mess grease trap cleaning", "Includes loading, transport & outside dumping"] },
    itpark: { price: "Rs 3,000 – Rs 5,000/trap", tanker: "Food Court Multi-Trap Rig", time: "1 – 2 hours", inclusions: ["3,000 Litres (Small Vehicle) = Rs 3,000/-", "5,000L – 7,000L (Big Vehicle) = Rs 5,000/-", "Food court & corporate cafeteria grease traps", "Night-shift execution with zero odor"] },
    restaurant: { price: "Rs 3,000 – Rs 5,000", tanker: "Dedicated F&B Rapid Unit", time: "40 mins", inclusions: ["3,000 Litres (Small Vehicle) = Rs 3,000/-", "5,000L – 7,000L (Big Vehicle) = Rs 5,000/-", "Crude oil, grease, food wastage & bad smell removal", "Per Trip: Loading + Cleaning + Outside Dumping"] },
    construction: { price: "Rs 3,000 – Rs 5,000", tanker: "Mess Kitchen Unit", time: "45 mins", inclusions: ["Small Vehicle = Rs 3,000 | Big Vehicle = Rs 5,000", "Labour camp mess grease trap cleaning", "Prevents kitchen drain choking and pest influx", "Safe outside dumping"] }
  },
  portable: {
    name: "Portable Toilet & Labour Charges",
    villa: { price: "Rs 2,500/labour", tanker: "Mobile Sanitation & Labour", time: "Per Call", inclusions: ["Per One Labour Charge = Rs 2,500/-", "To clean drainage line, septic tank or sump", "Includes manual assistance for deep sludge clearing", "Trained and experienced personnel"] },
    apartment: { price: "Rs 2,500/labour", tanker: "Society Sanitation Crew", time: "Per Call", inclusions: ["Per One Labour Charge = Rs 2,500/-", "Drainage line, sump or wastage sludge cleaning", "Heavy sediment extraction assistance", "Full safety equipment provided"] },
    itpark: { price: "Rs 2,500/labour", tanker: "Campus Support Crew", time: "Per Call", inclusions: ["Rs 2,500/- Per One Labour Charge", "Underground tank & wastage sludge maintenance", "Trained operators with strict safety gear", "Official billing & compliance"] },
    restaurant: { price: "Rs 2,500/labour", tanker: "F&B Deep Sanitation Crew", time: "Per Call", inclusions: ["Rs 2,500/- Per One Labour", "Kitchen sump & grease line deep de-sludging", "Experienced staff with disinfectant wash", "Outside waste disposal"] },
    construction: { price: "Rs 2,500/labour", tanker: "Site Sanitation & Toilet Rig", time: "Scheduled", inclusions: ["Per One Labour Charge = Rs 2,500/-", "Drainage line, septic tank & camp sump clean", "Portable cabin waste suction & recharge", "Includes loading, transport & outside dumping"] }
  },
  basement: {
    name: "Basement / Cellar / Small Access Areas",
    villa: { price: "Rs 2,500/- Fixed Per Trip", tanker: "Special Small Vehicle", time: "45 mins", inclusions: ["Price Per Trip: Rs 2,500/-", "Special small vehicle for tight or restricted access", "Ideal for basements, cellars, and narrow lanes", "Loading, cleaning & outside dumping included"] },
    apartment: { price: "Rs 2,500/- Fixed Per Trip", tanker: "Low-Headroom Small Vehicle", time: "60 mins", inclusions: ["Price Per Trip: Rs 2,500/-", "Enters low-clearance basement parking decks", "Cellar drainage & underground septic suction", "Includes loading, cleaning & outside dumping"] },
    itpark: { price: "Rs 2,500/- Fixed Per Trip", tanker: "Cellar Compact Suction Unit", time: "60 – 90 mins", inclusions: ["Price Per Trip: Rs 2,500/- (Per Trip)", "Special low-clearance vehicle for underground decks", "Cellar & hanging line drainage cleaning", "Zero ceiling leaks or floor contamination"] },
    restaurant: { price: "Rs 2,500/- Fixed Per Trip", tanker: "Compact Basement Sump Unit", time: "45 mins", inclusions: ["Price Per Trip: Rs 2,500/-", "Special small vehicle for cellar kitchen lines", "Removes sludge, crude oil & bad odors", "Loading, transport & outside dumping included"] },
    construction: { price: "Rs 2,500/- Fixed Per Trip", tanker: "Narrow Access Silt Tanker", time: "60 mins", inclusions: ["Price Per Trip: Rs 2,500/-", "Special small vehicle for tight access construction pits", "Basement foundation drain and sump clean", "Outside dumping at authorized STP"] }
  }
};

let currentProperty = 'apartment';
let currentService = 'septic';
let currentBasement = 'ground';

function initCalculator() {
  const propertyPills = document.querySelectorAll('[data-calc-property]');
  const servicePills = document.querySelectorAll('[data-calc-service]');
  const basementPills = document.querySelectorAll('[data-calc-basement]');

  propertyPills.forEach(pill => {
    pill.addEventListener('click', () => {
      propertyPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      currentProperty = pill.dataset.calcProperty;
      updateCalculatorOutput();
    });
  });

  servicePills.forEach(pill => {
    pill.addEventListener('click', () => {
      servicePills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      currentService = pill.dataset.calcService;
      updateCalculatorOutput();
    });
  });

  basementPills.forEach(pill => {
    pill.addEventListener('click', () => {
      basementPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      currentBasement = pill.dataset.calcBasement;
      updateCalculatorOutput();
    });
  });

  const calcBookBtn = document.getElementById('calcBookBtn');
  if (calcBookBtn) {
    calcBookBtn.addEventListener('click', () => {
      const data = PRICING_DATA[currentService][currentProperty];
      const basementLabel = currentBasement === 'ground' ? 'Ground Level' : currentBasement.toUpperCase();
      const message = `Hello Dial-a-Septic Tank Cleaners!%0A%0AI want to book a service:%0A• Service: ${encodeURIComponent(PRICING_DATA[currentService].name)}%0A• Property Type: ${encodeURIComponent(currentProperty.toUpperCase())}%0A• Level: ${encodeURIComponent(basementLabel)}%0A• Estimated Quote: ${encodeURIComponent(data.price)}%0A%0APlease confirm tanker availability and arrival ETA.`;
      window.open(`https://wa.me/${PHONE_NUMBER}?text=${message}`, '_blank');
    });
  }

  updateCalculatorOutput();
}

function updateCalculatorOutput() {
  const priceDisplay = document.getElementById('calcPrice');
  const durationDisplay = document.getElementById('calcDuration');
  const tankerDisplay = document.getElementById('calcTanker');
  const inclusionsList = document.getElementById('calcInclusions');

  if (!PRICING_DATA[currentService] || !PRICING_DATA[currentService][currentProperty]) return;

  const data = PRICING_DATA[currentService][currentProperty];
  let priceStr = data.price;

  // Add small basement difficulty surcharge if B2/B3
  if (currentBasement === 'b2') {
    priceStr += " (+B2 level)";
  } else if (currentBasement === 'b3') {
    priceStr += " (+B3 booster)";
  }

  if (priceDisplay) priceDisplay.textContent = priceStr;
  if (durationDisplay) durationDisplay.textContent = `Estimated Time: ${data.time}`;
  if (tankerDisplay) tankerDisplay.textContent = `Equipment: ${data.tanker}`;

  if (inclusionsList) {
    inclusionsList.innerHTML = '';
    data.inclusions.forEach(item => {
      const div = document.createElement('div');
      div.innerHTML = `
        <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
        <span>${item}</span>
      `;
      inclusionsList.appendChild(div);
    });
  }
}

/* --------------------------------------------------------------------------
   3. 20 LOCALITY INTERACTIVE DISPATCHER
   -------------------------------------------------------------------------- */
const LOCALITY_DATA = {
  "Madhapur": { eta: "20 – 35 Mins", tankers: "3 Active Tankers", hub: "Central HQ (Patrika Nagar)" },
  "Gachibowli": { eta: "25 – 40 Mins", tankers: "2 Active Tankers", hub: "Financial District Fleet" },
  "Hitech City": { eta: "15 – 30 Mins", tankers: "3 Active Tankers", hub: "Cyber Towers Staging" },
  "Kondapur": { eta: "20 – 35 Mins", tankers: "2 Active Tankers", hub: "Botanical Garden Hub" },
  "Khajaguda": { eta: "30 – 45 Mins", tankers: "1 Active Tanker", hub: "Khajaguda Junction" },
  "Manikonda": { eta: "30 – 45 Mins", tankers: "2 Active Tankers", hub: "Puppalaguda Base" },
  "Narsingi": { eta: "35 – 50 Mins", tankers: "2 Active Tankers", hub: "ORR Junction Unit" },
  "Nanakramguda": { eta: "25 – 40 Mins", tankers: "2 Active Tankers", hub: "Financial District Unit" },
  "Kukatpally": { eta: "30 – 45 Mins", tankers: "2 Active Tankers", hub: "KPHB Staging" },
  "Hafeezpet": { eta: "25 – 40 Mins", tankers: "1 Active Tanker", hub: "Hafeezpet Station" },
  "Kokapet": { eta: "35 – 50 Mins", tankers: "2 Active Tankers", hub: "Golden Mile Base" },
  "Jubilee Hills": { eta: "25 – 40 Mins", tankers: "2 Active Tankers", hub: "Road No 36 Hub" },
  "Raidurgam": { eta: "20 – 35 Mins", tankers: "2 Active Tankers", hub: "Knowledge City Base" },
  "Kothaguda": { eta: "20 – 30 Mins", tankers: "2 Active Tankers", hub: "Whitefields Base" },
  "Borabanda": { eta: "30 – 45 Mins", tankers: "1 Active Tanker", hub: "Erragadda Axis" },
  "Lingampally": { eta: "35 – 50 Mins", tankers: "2 Active Tankers", hub: "BHEL Circle Unit" },
  "Nallagandla": { eta: "35 – 50 Mins", tankers: "2 Active Tankers", hub: "Aparna Townships Base" },
  "Gowlidoddi": { eta: "30 – 45 Mins", tankers: "1 Active Tanker", hub: "Wipro Circle Unit" },
  "Tellapur": { eta: "40 – 55 Mins", tankers: "2 Active Tankers", hub: "My Home Township Base" },
  "Kollur": { eta: "45 – 60 Mins", tankers: "1 Active Tanker", hub: "ORR Exit 2 Base" }
};

let selectedLocality = "Madhapur";

function initLocalities() {
  const pills = document.querySelectorAll('[data-locality]');
  const titleEl = document.getElementById('localLiveTitle');
  const metaEl = document.getElementById('localLiveMeta');
  const bookBtn = document.getElementById('localLiveBookBtn');

  pills.forEach(pill => {
    pill.addEventListener('click', () => {
      pills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      selectedLocality = pill.dataset.locality;
      
      const loc = LOCALITY_DATA[selectedLocality] || { eta: "30 – 45 Mins", tankers: "Active Units Available", hub: "Madhapur Main Fleet" };
      
      if (titleEl) {
        titleEl.textContent = `📍 ${selectedLocality}: Guaranteed ETA ${loc.eta}`;
      }
      if (metaEl) {
        metaEl.textContent = `🟢 ${loc.tankers} • Dispatched from ${loc.hub} • 24/7 Priority Hotline`;
      }
      
      // Auto prefill location in contact forms if present
      const locationInput = document.getElementById('leadLocation');
      if (locationInput) {
        locationInput.value = selectedLocality;
      }
    });
  });

  if (bookBtn) {
    bookBtn.addEventListener('click', () => {
      const loc = LOCALITY_DATA[selectedLocality] || { eta: "30 – 45 Mins" };
      const message = `Hello Dial-a-Septic!%0A%0ANeed emergency cleaning service in *${encodeURIComponent(selectedLocality)}*.%0APlease dispatch the nearest available vacuum tanker (ETA: ${encodeURIComponent(loc.eta)}).`;
      window.open(`https://wa.me/${PHONE_NUMBER}?text=${message}`, '_blank');
    });
  }
}

/* --------------------------------------------------------------------------
   4. SERVICE MODALS
   -------------------------------------------------------------------------- */
const SERVICE_DETAILS = {
  septic: {
    title: "1. Septic Tank Cleaning Services",
    subtitle: "Complete mechanized de-sludging for residential, commercial, and industrial facilities.",
    html: `
      <p>Dial-a-Septic Tank Cleaners provides heavy-duty mechanized vacuum suction services across Hyderabad. We eliminate accumulated scum, liquid effluent, and settled anaerobic sludge without foul odors or messy manual shoveling.</p>
      <h4 style="color:#22d3ee; margin:1rem 0 0.5rem 0;">Suitable For:</h4>
      <ul style="padding-left:1.2rem; margin-bottom:1rem; color:#cbd5e1;">
        <li>Residential apartments & gated societies</li>
        <li>Independent houses, villas & farmhouses</li>
        <li>Commercial buildings, offices & IT companies</li>
        <li>Hospitals, schools, colleges & hostels</li>
        <li>Labour camps, construction sites & industrial facilities</li>
      </ul>
      <h4 style="color:#22d3ee; margin:1rem 0 0.5rem 0;">Our Equipment & Guarantee:</h4>
      <p style="color:#cbd5e1;">We operate modern 4,000L to 12,000L high-vacuum suction tankers equipped with over 100 meters of flexible reinforced hose to reach difficult interior spots. 100% mechanized execution adhering strictly to the Prohibition of Manual Scavenging Act.</p>
    `
  },
  drainage: {
    title: "2. Drainage Cleaning & De-Clogging Services",
    subtitle: "High-pressure hydro-jetting and clearing of blocked sewer pipes and storm drains.",
    html: `
      <p>Wastewater and sewer line chokes cause foul stenches, backflow into bathrooms, and unhygienic overflows. We use advanced high-pressure water jetting (up to 250 bar) to disintegrate sludge, grease cakes, silt, and tree roots.</p>
      <h4 style="color:#22d3ee; margin:1rem 0 0.5rem 0;">What We Clear:</h4>
      <ul style="padding-left:1.2rem; margin-bottom:1rem; color:#cbd5e1;">
        <li>Mainline sewer blocks and overflowing manholes</li>
        <li>Residential building drainage pipe chokes</li>
        <li>Stormwater drain siltation and leaf debris</li>
        <li>Industrial wastewater pipeline scale</li>
      </ul>
      <p style="color:#cbd5e1;">Includes inspection camera verification and deodorizing rinse to ensure free, uninterrupted gravitational wastewater flow.</p>
    `
  },
  stp: {
    title: "3. STP Tank Cleaning Services (7 Chambers)",
    subtitle: "Specialized maintenance for Sequencing Batch Reactors, collection sumps, and treated tanks.",
    html: `
      <p>Modern residential townships and IT parks depend on Sewage Treatment Plants (STPs) to recycle wastewater. Dial-a-Septic Cleaners handles comprehensive chamber-by-chamber cleaning:</p>
      <ul style="padding-left:1.2rem; margin-bottom:1rem; color:#cbd5e1;">
        <li><strong>Bar Screen Chamber Cleaning:</strong> Debris, plastic, and solid trash extraction.</li>
        <li><strong>Collection / Raw Sewage Tank:</strong> Heavy settled sludge and grit evacuation.</li>
        <li><strong>SBR (Sequencing Batch Reactor) Tank:</strong> Controlled de-sludging without damaging biomass.</li>
        <li><strong>Sludge Holding Tank:</strong> High-density sludge pumping into sealed vacuum tankers.</li>
        <li><strong>Aeration Tank:</strong> Biological deposit washdown and diffuser inspection.</li>
        <li><strong>Filter Feed & Treated Water Tanks:</strong> Sediment removal to safeguard sand and carbon filters.</li>
      </ul>
      <p style="color:#cbd5e1;">Full compliance with Telangana Pollution Control Board (TSPCB) decanting guidelines.</p>
    `
  },
  grease: {
    title: "4. Grease Trap & Commercial Kitchen Cleaning",
    subtitle: "Eliminating Fats, Oils, and Grease (FOG) for hotels, restaurants, and cloud kitchens.",
    html: `
      <p>Fats, Oils, and Grease (FOG) solidify rapidly in commercial kitchen pipelines, choking interceptors and generating unbearable odors during dinner rushes. We provide emergency and scheduled maintenance throughout Hyderabad.</p>
      <h4 style="color:#22d3ee; margin:1rem 0 0.5rem 0;">Ideal For:</h4>
      <ul style="padding-left:1.2rem; margin-bottom:1rem; color:#cbd5e1;">
        <li>Hotels, dining halls, canteens & food courts</li>
        <li>Commercial restaurants & cloud kitchens (Swiggy/Zomato hubs)</li>
        <li>Corporate cafeterias in Hitech City and Gachibowli</li>
        <li>Hospital & institutional kitchens</li>
      </ul>
      <p style="color:#cbd5e1;">We offer night-shift execution (11 PM – 6 AM) so your dining service experiences zero downtime or customer odor complaints.</p>
    `
  },
  portable: {
    title: "5. Portable Toilet Cleaning & Site Sanitation",
    subtitle: "Punctual chemical servicing and waste pumping for construction sites and outdoor events.",
    html: `
      <p>Maintaining hygienic site bathrooms is critical for workforce retention, disease prevention, and municipal compliance. We provide rapid suction evacuation and chemical recharging for temporary toilets.</p>
      <h4 style="color:#22d3ee; margin:1rem 0 0.5rem 0;">Services Provided:</h4>
      <ul style="padding-left:1.2rem; margin-bottom:1rem; color:#cbd5e1;">
        <li>Scheduled weekly or bi-weekly vacuum pumping</li>
        <li>Fresh water replenishment & high-pressure cabin wash</li>
        <li>Deodorizing biodegradable blue chemical recharge</li>
        <li>Labour camp septic tank evacuation</li>
        <li>On-demand emergency response for mega infrastructure projects</li>
      </ul>
    `
  },
  basement: {
    title: "6. Basement Drainage Cleaning (B1 / B2 / B3 Levels)",
    subtitle: "High-suction lift and low-profile tankers for deep underground parking and sumps.",
    html: `
      <p>Underground basements (B1, B2, B3) present unique architectural challenges: low ceiling heights (often under 2.4 meters) prevent standard tankers from entering, while high gravitational lift can cause pump cavitation.</p>
      <h4 style="color:#22d3ee; margin:1rem 0 0.5rem 0;">Our Specialized Capabilities:</h4>
      <ul style="padding-left:1.2rem; margin-bottom:1rem; color:#cbd5e1;">
        <li><strong>B1, B2, B3 Basement Drainage:</strong> Low-profile suction units or auxiliary high-head boosters.</li>
        <li><strong>Hanging Pipeline Cleaning:</strong> Descaling and clearing suspended sewage pipelines on ceiling trays.</li>
        <li><strong>Underground Sump & Lift Stations:</strong> Total evacuation of accumulated silts and heavy slurry.</li>
        <li><strong>Zero Spill Guarantee:</strong> Odor-sealed hose clamps and spill mats protect polished parking floors.</li>
      </ul>
    `
  }
};

function initServiceModals() {
  const modalOverlay = document.getElementById('serviceModal');
  const modalTitle = document.getElementById('modalTitle');
  const modalSubtitle = document.getElementById('modalSubtitle');
  const modalBody = document.getElementById('modalBody');
  const modalClose = document.getElementById('modalClose');
  const modalBookBtn = document.getElementById('modalBookBtn');

  let activeServiceKey = 'septic';

  document.querySelectorAll('[data-service-modal]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const key = btn.dataset.serviceModal;
      activeServiceKey = key;
      const details = SERVICE_DETAILS[key];
      if (details && modalOverlay) {
        if (modalTitle) modalTitle.textContent = details.title;
        if (modalSubtitle) modalSubtitle.textContent = details.subtitle;
        if (modalBody) modalBody.innerHTML = details.html;
        modalOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  if (modalClose && modalOverlay) {
    modalClose.addEventListener('click', () => {
      modalOverlay.classList.remove('active');
      document.body.style.overflow = 'auto';
    });

    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) {
        modalOverlay.classList.remove('active');
        document.body.style.overflow = 'auto';
      }
    });
  }

  if (modalBookBtn) {
    modalBookBtn.addEventListener('click', () => {
      const details = SERVICE_DETAILS[activeServiceKey];
      const message = `Hello Dial-a-Septic!%0A%0AI am inquiring about *${encodeURIComponent(details ? details.title : 'Cleaning Service')}*.%0APlease share tanker availability and quote.`;
      window.open(`https://wa.me/${PHONE_NUMBER}?text=${message}`, '_blank');
    });
  }
}

/* --------------------------------------------------------------------------
   5. BOOKING FORMS & LEAD CAPTURE
   -------------------------------------------------------------------------- */
function initBookingForms() {
  // Hero Quick Dispatch Form
  const heroForm = document.getElementById('heroDispatchForm');
  if (heroForm) {
    heroForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const service = document.getElementById('heroService').value;
      const locality = document.getElementById('heroLocality').value;
      const phone = document.getElementById('heroPhone').value;

      if (!phone || phone.length < 10) {
        showToast("⚠️ Please enter a valid 10-digit mobile number.");
        return;
      }

      showToast("🚀 Emergency Dispatch Request Received! Connecting via WhatsApp...");
      
      setTimeout(() => {
        const message = `🚨 *EMERGENCY DISPATCH REQUEST*%0A%0A• Service: ${encodeURIComponent(service)}%0A• Locality: ${encodeURIComponent(locality)}%0A• Contact Phone: ${encodeURIComponent(phone)}%0A%0APlease confirm nearest tanker ETA immediately!`;
        window.open(`https://wa.me/${PHONE_NUMBER}?text=${message}`, '_blank');
        heroForm.reset();
      }, 700);
    });
  }

  // Main Contact Form
  const contactForm = document.getElementById('mainContactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('contactName').value;
      const phone = document.getElementById('contactPhone').value;
      const service = document.getElementById('contactService').value;
      const notes = document.getElementById('contactNotes').value;

      if (!phone || phone.length < 10) {
        showToast("⚠️ Please enter a valid 10-digit mobile number.");
        return;
      }

      showToast("✅ Booking Request Created! Opening WhatsApp...");

      setTimeout(() => {
        const message = `*BOOKING / AMC INQUIRY*%0A%0A• Name: ${encodeURIComponent(name)}%0A• Phone: ${encodeURIComponent(phone)}%0A• Service: ${encodeURIComponent(service)}%0A• Notes: ${encodeURIComponent(notes || 'None')}%0A%0AFrom www.dailaseptictankcleaners.com`;
        window.open(`https://wa.me/${PHONE_NUMBER}?text=${message}`, '_blank');
        contactForm.reset();
      }, 700);
    });
  }
}

/* --------------------------------------------------------------------------
   6. TOAST NOTIFICATION
   -------------------------------------------------------------------------- */
function showToast(text) {
  let toast = document.getElementById('liveToast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'liveToast';
    toast.className = 'toast-msg';
    document.body.appendChild(toast);
  }
  toast.textContent = text;
  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 4000);
}

/* --------------------------------------------------------------------------
   7. STATS ANIMATION & SMOOTH NUMERICAL COUNTER
   -------------------------------------------------------------------------- */
function initStatsCounter() {
  const statNumbers = document.querySelectorAll('.stat-number');
  if (!statNumbers.length) return;
  let animated = false;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !animated) {
        animated = true;
        
        statNumbers.forEach(numEl => {
          const rawText = numEl.textContent.trim();
          
          if (rawText.includes('1,200+')) {
            animateNumber(numEl, 0, 1200, 1400, (val) => `${val.toLocaleString('en-IN')}+`);
          } else if (rawText.includes('100%')) {
            animateNumber(numEl, 0, 100, 1200, (val) => `${val}%`);
          } else {
            numEl.style.transform = 'scale(1.08)';
            setTimeout(() => {
              numEl.style.transition = 'transform 0.4s ease';
              numEl.style.transform = 'scale(1)';
            }, 300);
          }
        });
        
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.25 });

  const statsSec = document.querySelector('.stats-section');
  if (statsSec) observer.observe(statsSec);
}

function animateNumber(element, start, end, duration, formatFn) {
  let startTime = null;
  function step(timestamp) {
    if (!startTime) startTime = timestamp;
    const progress = Math.min((timestamp - startTime) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.floor(start + (end - start) * eased);
    element.textContent = formatFn ? formatFn(current) : current;
    if (progress < 1) {
      window.requestAnimationFrame(step);
    } else {
      element.textContent = formatFn ? formatFn(end) : end;
    }
  }
  window.requestAnimationFrame(step);
}

/* --------------------------------------------------------------------------
   7B. GLOBAL HIGH-PERFORMANCE SCROLL REVEAL ENGINE
   -------------------------------------------------------------------------- */
function initScrollReveals() {
  const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
  if (!revealElements.length) return;

  // Stagger child elements in containers
  const staggerContainers = document.querySelectorAll('.reveal-stagger');
  staggerContainers.forEach(container => {
    const children = Array.from(container.children);
    children.forEach((child, idx) => {
      child.style.transitionDelay = `${idx * 0.12}s`;
    });
  });

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        // Unobserve immediately to keep GPU/CPU footprint completely free
        revealObserver.unobserve(entry.target);
      }
    });
  }, {
    rootMargin: '0px 0px -40px 0px',
    threshold: 0.1
  });

  revealElements.forEach(el => {
    revealObserver.observe(el);
  });
}

/* --------------------------------------------------------------------------
   8. FLEET VIDEO SHOWCASE SWITCHER
   -------------------------------------------------------------------------- */
function initVideoShowcase() {
  const videoPlayer = document.getElementById('fleetVideoPlayer');
  const videoSource = document.getElementById('fleetVideoSource');
  const buttons = document.querySelectorAll('.video-select-btn');
  const activeTitle = document.getElementById('videoActiveTitle');
  const activeDesc = document.getElementById('videoActiveDesc');

  if (!videoPlayer || !buttons.length) return;

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const src = btn.getAttribute('data-video-src');
      const poster = btn.getAttribute('data-video-poster');
      const title = btn.getAttribute('data-video-title');
      const desc = btn.getAttribute('data-video-desc');

      buttons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      if (activeTitle && title) activeTitle.textContent = title;
      if (activeDesc && desc) activeDesc.textContent = desc;

      if (poster) videoPlayer.poster = poster;
      if (videoSource && src) {
        videoPlayer.pause();
        videoSource.src = src;
        videoPlayer.load();
        videoPlayer.play().catch(() => {
          // Autoplay policy might block unmuted play
        });
      }
    });
  });
}

/* --------------------------------------------------------------------------
   9. ADVANCED HERO TITLE DYNAMIC TEXT ANIMATOR
   -------------------------------------------------------------------------- */
function initHeroTextAnimation() {
  const dynamicElement = document.getElementById('heroDynamicText');
  if (!dynamicElement) return;

  const phrases = [
    "24/7 Septic Tank Cleaning in Hyderabad",
    "Quick Tanker Arrival in 30–45 Mins",
    "100% Machine Cleaning (Safe & Clean)",
    "Starting from ₹2,000 per Trip",
    "Fast Drain & Sewer Blockage Clearing",
    "Clean & Safe Waste Disposal"
  ];

  let phraseIndex = 0;
  let charIndex = phrases[0].length;
  let isDeleting = true; // start by deleting after initial showcase pause
  const typingSpeed = 50;
  const deleteSpeed = 26;
  const pauseEnd = 2500;
  const pauseStart = 350;

  function tick() {
    const currentPhrase = phrases[phraseIndex];

    if (isDeleting) {
      charIndex--;
      dynamicElement.textContent = currentPhrase.substring(0, charIndex);
      if (charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        setTimeout(tick, pauseStart);
        return;
      }
      setTimeout(tick, deleteSpeed);
    } else {
      charIndex++;
      dynamicElement.textContent = currentPhrase.substring(0, charIndex);
      if (charIndex === currentPhrase.length) {
        isDeleting = true;
        setTimeout(tick, pauseEnd);
        return;
      }
      setTimeout(tick, typingSpeed);
    }
  }

  // Initial showcase pause before cycling starts
  setTimeout(tick, 2200);
}

/* --------------------------------------------------------------------------
   10. HERO VIDEO BACKGROUND (FIRST 20 SECONDS SEAMLESS LOOP)
   -------------------------------------------------------------------------- */
function initHeroVideo() {
  const heroVideo = document.getElementById('heroVideoBg');
  if (!heroVideo) return;

  heroVideo.muted = true;
  heroVideo.playsInline = true;

  // Seamlessly loop within the first 20 seconds
  heroVideo.addEventListener('timeupdate', () => {
    if (heroVideo.currentTime >= 20) {
      heroVideo.currentTime = 0;
      heroVideo.play().catch(() => {});
    }
  });

  // Ensure autoplay starts without sound
  const playPromise = heroVideo.play();
  if (playPromise !== undefined) {
    playPromise.catch(() => {
      // Fallback: Autoplay prevented until user interaction
      document.addEventListener('click', () => {
        heroVideo.play().catch(() => {});
      }, { once: true });
    });
  }
}

/* --------------------------------------------------------------------------
   11. PERMANENTLY MUTED TESTIMONIAL / CLIENT REVIEW VIDEOS
   -------------------------------------------------------------------------- */
function initTestimonialVideos() {
  const testimonialVideos = document.querySelectorAll('.video-reviews-section video');
  if (!testimonialVideos.length) return;

  testimonialVideos.forEach(video => {
    // Permanently mute and zero volume
    video.muted = true;
    video.defaultMuted = true;
    video.volume = 0;

    // Intercept any play, volume change, or user unmuting attempts
    const enforcePermanentMute = () => {
      if (!video.muted || video.volume > 0) {
        video.muted = true;
        video.volume = 0;
      }
    };

    ['volumechange', 'play', 'playing', 'loadedmetadata', 'canplay', 'timeupdate'].forEach(evt => {
      video.addEventListener(evt, enforcePermanentMute);
    });
  });
}

/* --------------------------------------------------------------------------
   12. LEGAL & POLICY PAGES TOC TRACKER
   -------------------------------------------------------------------------- */
function initLegalTOC() {
  const tocLinks = document.querySelectorAll('.legal-toc .toc-link');
  const sections = document.querySelectorAll('.legal-content .legal-card');
  if (!tocLinks.length || !sections.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        tocLinks.forEach(link => {
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
            if (window.innerWidth <= 960) {
              link.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
            }
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, {
    rootMargin: '-80px 0px -60% 0px',
    threshold: 0.05
  });

  sections.forEach(sec => observer.observe(sec));
}

/* --------------------------------------------------------------------------
   13. COOKIE CONSENT BANNER & PREFERENCE MANAGEMENT
   -------------------------------------------------------------------------- */
function initCookieConsent() {
  const COOKIE_STORAGE_KEY = 'dial_a_septic_cookie_choice';
  const savedChoice = localStorage.getItem(COOKIE_STORAGE_KEY);

  // Update status widget on cookies.html if present
  const statusEl = document.getElementById('cookieCurrentStatus');
  const btnAcceptManual = document.getElementById('btnAcceptCookiesManual');
  const btnRejectManual = document.getElementById('btnRejectCookiesManual');

  function updateStatusDisplay() {
    const current = localStorage.getItem(COOKIE_STORAGE_KEY);
    if (statusEl) {
      if (current === 'accepted') {
        statusEl.textContent = 'Accepted (All Cookies Enabled)';
        statusEl.style.color = 'var(--primary-brand)';
      } else if (current === 'rejected') {
        statusEl.textContent = 'Rejected (Essential Only)';
        statusEl.style.color = 'var(--accent-highlight)';
      } else {
        statusEl.textContent = 'Not Set (Pending Choice)';
        statusEl.style.color = 'var(--supporting-neutral)';
      }
    }
  }

  updateStatusDisplay();

  if (btnAcceptManual) {
    btnAcceptManual.addEventListener('click', () => {
      localStorage.setItem(COOKIE_STORAGE_KEY, 'accepted');
      updateStatusDisplay();
      if (typeof showToast === 'function') {
        showToast('✓ Cookie preference saved: All cookies accepted.');
      }
    });
  }

  if (btnRejectManual) {
    btnRejectManual.addEventListener('click', () => {
      localStorage.setItem(COOKIE_STORAGE_KEY, 'rejected');
      updateStatusDisplay();
      if (typeof showToast === 'function') {
        showToast('✓ Cookie preference saved: Non-essential rejected.');
      }
    });
  }

  // If user already made a choice, do not show banner
  if (savedChoice) {
    return;
  }

  // Create and inject banner if not already in DOM
  let banner = document.getElementById('cookieConsentBanner');
  if (!banner) {
    banner = document.createElement('div');
    banner.id = 'cookieConsentBanner';
    banner.className = 'cookie-consent-banner';
    banner.innerHTML = `
      <div class="cookie-consent-header">
        <span class="cookie-consent-icon">🍪</span>
        <h4 class="cookie-consent-title">We Value Your Privacy</h4>
      </div>
      <p class="cookie-consent-desc">
        We use essential cookies to ensure rapid WhatsApp &amp; phone booking, and to analyze website performance. Read our <a href="cookies.html">Cookies Policy</a>.
      </p>
      <div class="cookie-consent-actions">
        <button type="button" class="btn btn-primary btn-sm" id="btnAcceptCookies">
          Accept Cookies
        </button>
        <button type="button" class="btn btn-outline btn-sm" id="btnRejectCookies">
          Reject Non-Essential
        </button>
      </div>
    `;
    document.body.appendChild(banner);
  }

  // Slide banner in after slight delay
  setTimeout(() => {
    banner.classList.add('show');
  }, 900);

  // Bind Accept button
  const acceptBtn = document.getElementById('btnAcceptCookies');
  if (acceptBtn) {
    acceptBtn.addEventListener('click', () => {
      localStorage.setItem(COOKIE_STORAGE_KEY, 'accepted');
      banner.classList.remove('show');
      updateStatusDisplay();
      if (typeof showToast === 'function') {
        showToast('✓ Cookies accepted. Thank you!');
      }
    });
  }

  // Bind Reject button
  const rejectBtn = document.getElementById('btnRejectCookies');
  if (rejectBtn) {
    rejectBtn.addEventListener('click', () => {
      localStorage.setItem(COOKIE_STORAGE_KEY, 'rejected');
      banner.classList.remove('show');
      updateStatusDisplay();
      if (typeof showToast === 'function') {
        showToast('✓ Non-essential cookies rejected.');
      }
    });
  }
}
