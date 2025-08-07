## PM

#### 🧭 Process 23 – 3-Layer Product Map (Core / Experimental / Custom)  
**Owner:** PM  
**Departments:** General, PM  
**Category:** Planning & Strategy, Team Sync  
**Type:** Product-Related  
**Tools:** Asana, ClickUp, Notion  
**Related Process IDs:** 11  

**Context & Problem:**
Product teams and stakeholders often confuse strategic features with one-off client requests.  
The roadmap becomes a mess.  

**Goal:**
Visually and structurally separate product development into three clear tracks to help everyone understand what’s core, what’s a test, and what’s custom.  

**How It Works:**

1. Create a “Product Map” page in Notion (or board in ClickUp)

Split features into three labeled categories:  

    - 🔵 Core – Long-term, strategic, foundational parts of the platform

(e.g., authentication, CMS core, navigation engine)  

    - 🟠 Experimental – Tests, MVPs, innovation pieces being validated

(e.g., SmartParking AI add-on, new AR interface)  

    - 🟢 Custom – One-off or client-specific features not meant for the general product

(e.g., museum-specific integration, white-labeled UI)  

2. Each feature includes:
    - Owner
    - Link to design/spec
    - % progress
    - Delivery date
3. Updated weekly by PMs or Tech Leads

Used in all product reviews and planning  

**Tools:**
ClickUp (with tags/labels) → Notion (for visual product map)  

**Benefits:**

* Helps prioritize correctly
* Improves transparency with clients
* Shows product maturity and innovation areas

#### 📥 Process 36 – Unified “Release Review” Channel  
**Owner:** PM  
**Departments:** Design, Development, Marketing  
**Category:** Communication, Deployment & Delivery, Team Sync  
**Type:** Product-Related  
**Tools:** ClickUp, Loom, Slack, Tines  
**Related Process IDs:** N/A  

**Context & Problem:**
Once a feature or fix goes live, many team members—including Sales, UX, QA, and even other Devs—don’t know what was released.  
This causes misalignment, missed training opportunities, and lack of product ownership.  

**Goal:**
Create a central Slack channel where every release is shared, reviewed, and open to comments across departments.  

**How It Works:**

1. Channel Setup:
    - Slack channel: #release-review
    - Visible to all departments
2. For every release (even small):
    - Dev or PM posts:
    - 🆕 What was released
    - 📂 Related tasks (ClickUp link)
    - 🧪 Notes if anything still needs to be tested
    - 🎥 Optional Loom with walkthrough or visual changes
3. Cross-Team Comments Welcome:
    - Anyone can comment with:
    - Questions
    - Feedback
    - Suggestions
    - Praise
4. Optional Weekly Digest:
    - Tines/Slackbot compiles all entries into a Monday digest

**Tools:**
Slack → Loom (optional) → ClickUp task links → Tines (digest automation)  

**Benefits:**

* Builds shared product awareness
* Encourages constructive, asynchronous feedback
* Reduces silos between Dev, UX, Marketing, QA, Sales
* Makes quality part of company culture, not just code

#### 🧰 Process 37 – Minimum Release Package Template  
**Owner:** PM  
**Departments:** Design, Development  
**Category:** Communication, Documentation  
**Type:** Product-Related  
**Tools:** ClickUp, Loom, Slack, Tines  
**Related Process IDs:** N/A  

**Context & Problem:**
Every team or release owner tends to manage handoffs differently.  
As a result, some features go live:  

* Without QA validation
* With outdated documentation
* Without internal announcement or assets for marketing

This inconsistency creates confusion, bugs, and missed opportunities.  

**Goal:**
Define a minimum set of deliverables that must be completed before closing any release—ensuring quality, alignment, and readiness across departments.  

* What the Template Includes

Every release (even minor) must check off the following items:  

1. Task Completed
    - All subtasks and linked items are resolved in ClickUp
2. QA Passed
    - Bug log reviewed
    - Critical issues resolved and retested
3. Loom Video Created
    - Short walkthrough explaining: what was built, how it works, and where to find it
    - Used by team members, Sales, and Marketing
4. Figma Updated
    - UI reflects final state
    - Design tokens, components, and states are cleaned and archived
5. Documentation Saved
    - Feature added to Notion with:
    - Description
    - Owner
    - Release notes
    - Known limitations
6. Marketing Notified
    - Feature is added to the Go-To-Market sync
    - Visual and messaging needs confirmed
    - If public: timeline agreed with Marketing

**How It Works:**

* The template is integrated into ClickUp or Tines
* Each release card includes a “Release Checklist” subtask or automation
* Tines can prevent a release task from being marked complete unless all boxes are checked

**Tools:**
ClickUp checklist or form → Notion → Loom → Slack (for marketing sync)  
Optional: Tines blocker automation  

**Benefits:**

* Guarantees release consistency
* Reduces chaos for QA, Marketing, and Sales
* Ensures traceability and internal understanding
* Scales as you grow with minimal overhead

#### 💼 Process 42 – Sales: Early Product Access Tracker  
**Owner:** PM  
**Departments:** Development, Marketing, PM, Sales  
**Category:** Communication, Team Sync  
**Type:** Product-Related  
**Tools:** Loom, Notion, Slack  
**Related Process IDs:** N/A  

**Context & Problem:**
Sales often learns about new features after they're released—missing early demo opportunities.  

**Goal:**
Give Sales early visibility on internal features in final QA phase, so they can prepare and pitch in time.  

**How It Works:**

1. When a feature is entering final QA, PM or Dev Lead adds it to a Notion page called “Early Access Products”
2. The entry includes:
    - Feature name and owner
    - Pitch summary (1-liner)
    - Demo Loom (optional)
    - Value proposition
    - Ready-to-share deck
    - Expected release date
3. Slack #sales-drop channel posts each new entry
    - Sales can book internal demo or note potential leads

**Tools:**
Notion → Slack → Loom (optional) → Pitch Deck (PDF)  

**Benefits:**

* Sales is ready before launch
* Faster GTM execution
* Feature value is communicated clearly and on time

#### 📘 Process 70 – Internal Wiki: Product Pages Like Landing Pages  
**Owner:** PM  
**Departments:** Design, Development, Executive, Marketing, Sales  
**Category:** Communication, Team Sync  
**Type:** Product-Related  
**Tools:** Figma, GitLab, Loom, Notion  
**Related Process IDs:** N/A  

**Context & Problem:**
Marketing and Sales don’t always know how to position a product. UX team lacks a reference for voice, story, and purpose.  

**Goal:**
Create an internal wiki page for each product/module, styled like a mini landing page.  

**How It Works:**

1. Each product gets a dedicated Notion page with:
    - 🏷 Name
    - 💬 Pitch sentence
    - 📸 Screenshots or Figma links
    - 🧩 Key Features
    - 👥 Target Buyer Persona
    - 📈 Current status: dev / test / live
    - 🔗 Link to GitHub, ClickUp, and Loom
2. Page is accessible to all: Sales, Marketing, UX, PM

**Tools:**
Notion + Figma + Loom + GitHub → Linked together  

**Benefits:**

* Marketing writes faster, with better info
* Sales knows what to sell and how
* Design and PM stay aligned on purpose and tone

#### 📘 Process 157 – Knowledge Handoff from Team Leads to PM  
**Owner:** PM  
**Departments:** Design, Development, PM  
**Category:** Documentation, Team Sync  
**Type:** Product-Related  
**Tools:** General  
**Related Process IDs:** N/A  

**Context & Problem:**
PMs often lack the technical or UX background to write complete briefs on their own.  

**Goal:**
Require knowledge transfer sessions from each team lead to the PM before planning starts.  

**How It Works:**

* Each team lead shares:
    - 🛠 Dev: technical logic, backend requirements
    - 🎨 UX: design reasoning, edge cases
    - 🧪 QA: fragile zones, known failure patterns
* The knowledge is shared via:
    - Loom
    - Short Notion doc
    - Slack message + links
* The PM uses this input to create:
    - Internal roadmap brief
    - External client-facing proposal

**Benefits:**

* Stronger, well-structured brief
* Less revision or misalignment during delivery
* Promotes PM autonomy

#### 📘 804 – Annual CEO Decision Archive (Managed Only by PMO)  
**Owner:** PM  
**Departments:** CEO, PM  
**Category:** Documentation  
**Type:** Product-Related  
**Tools:** NAS & Drive  
**Related Process IDs:** N/A  

**Context & Problem:**
The CEO needs access to strategic memory without managing documentation.  

**Goal:**
Maintain a quarterly-updated, yearly file of all strategic decisions and results.  

**Structure:**

* 📅 Yearly PDF
* 📝 Each entry: decision, owner, result, impact
* 🔖 Tags: Department / Priority / Project

📁 File: CEO_StrategicActions_Summary_2024.pdf  