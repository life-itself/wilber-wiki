# Works Hub Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace the chronological `/works` landing page with a reader-first hub and preserve the catalog at `/works/catalog`.

**Architecture:** Keep the site content-native: Markdown supplies the reading hierarchy and semantic links, while embedded HTML with existing Tailwind utilities supplies the asymmetric route chooser and responsive cover sequence. Move rather than duplicate the catalog so each route has one canonical page.

**Tech Stack:** Flowershow Markdown, embedded HTML, Tailwind utility classes, existing JPEG cover assets, shell/Python content checks.

---

### Task 1: Define route and content checks

**Files:**
- Test: repository content checked directly by shell assertions

**Step 1: Run failing assertions**

Assert that `works/catalog.md` exists; that `works/index.md` contains the three route
destinations, the four recommended cover paths, and the recommendation anchor; and
that the reading and phases guides link to `catalog.md`.

**Step 2: Confirm the expected failure**

The check must fail because `works/catalog.md` and the new hub do not yet exist.

### Task 2: Split the hub and catalog routes

**Files:**
- Create: `works/catalog.md`
- Modify: `works/index.md`
- Modify: `works/reading-guide.md`
- Modify: `works/phases.md`
- Modify: `index.md`
- Modify: `notes/index.md`
- Modify: `docs/index-maintenance.md`
- Modify: `docs/works-catalog.md`
- Modify: `AGENTS.md`

**Step 1: Move the existing catalog**

Preserve the complete chronological content at `works/catalog.md` and update its
cross-links so they resolve from the same directory.

**Step 2: Build the hub**

Add the three-route chooser, an accessible-introduction feature, and the three-book
main route with existing covers and concise copy derived from the full reading guide.

**Step 3: Update current operational links**

Change links whose label or context promises the chronological catalog to point to
`catalog.md`. Leave historical changelog and plan records unchanged.

**Step 4: Run the route and content checks**

Expected: all assertions pass.

### Task 3: Verify content and visual behavior

**Files:**
- Modify if required: `works/index.md`

**Step 1: Check local Markdown links and image paths**

Run a repository link check focused on the changed pages and confirm that every new
local target exists.

**Step 2: Run the Impeccable detector**

Run the detector once over the changed hub markup, fix material findings in a single
batch, and rerun only once if fixes were needed.

**Step 3: Render desktop and mobile**

Use a local Flowershow preview or the closest available rendered preview. Inspect one
desktop and one mobile viewport together for hierarchy, cover proportions, order,
overflow, and focusable link affordances.

**Step 4: Record and track the shipped change**

Add a concise dated changelog entry if the redesign is ready to ship, close the Beads
task with evidence, flush Beads state, and commit the implementation. Do not publish
or push unless separately requested.

