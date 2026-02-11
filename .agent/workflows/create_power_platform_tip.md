---
description: Workflow to create a new PowerPlatformTip from start to finish
---

# Create PowerPlatformTip Workflow

This workflow guides you through the process of creating a PowerPlatformTip, from intake to newsletter generation.

1.  **Phase 0: Intake & Validation**
    -   Ask the user for the topic or raw input if not already provided.
    -   Identify if this is **Flow A** (with research) or **Flow B** (input only).
    -   Extract all necessary details:
        -   Working title / topic
        -   Product focus (Power Automate / Power Apps / Dataverse)
        -   Primary use case
        -   Target outcome + CTA
        -   YouTube URL (if any)
    -   *Checkpoint*: Confirm details with the user before proceeding.

2.  **Phase 1: Draft & Review (Flow A Only)**
    -   If **Flow A**, generate the "Review Tip" format using the strict icon structure.
    -   Present it to the user.
    -   *Checkpoint*: Wait for user confirmation ("OK") or feedback.

3.  **Phase 2: Generate Jekyll Markdown**
    -   Create the Jekyll Markdown file content based on the approved tip.
    -   Ensure correct filename format: `YYYY-MM-DD-powerplatformtip-<NNN>-<slug>.md`.
    -   Ensure strict Front Matter (as per rules).
    -   If a YouTube ID is present, add the video include at the end.
    -   Save the file to the project content directory (ask if unsure).

4.  **Phase 3: Generate HTML Newsletter**
    -   Load template from `.agent/templates/newsletter_template.html`.
    -   Fill placeholders with content from Phase 2.
    -   Strictly maintain inline styles (no link decorations).
    -   Save as `YYYY-MM-DD-newsletter-<slug>.html`.
