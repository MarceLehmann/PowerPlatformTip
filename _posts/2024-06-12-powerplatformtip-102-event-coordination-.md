---
title: "#PowerPlatformTip 102 – 'Event Coordination'"
date: 2024-06-12
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - MicrosoftGraph
  - EventManagement
  - Calendar
  - PowerPlatformTip
excerpt: "Silently manage event attendees in Power Automate using Microsoft Graph API—add guests without notifications and keep attendee lists private for secure event coordination."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Use the Microsoft Graph Update Event call with `hideAttendees: true` to add event attendees silently and keep the guest list private.

## 💡 Challenge
When you manage event attendees from Power Automate, the standard approach notifies everyone on every change — and by default all attendees can see the full guest list. That's noisy and, for sensitive events, a privacy problem.

## ✅ Solution
Update the event directly through the Microsoft Graph API. Setting the event's `hideAttendees` property to `true` keeps the guest list private, and writing the merged `attendees` array via a PATCH lets you add people without the usual notification flood.

## 🔧 How It's Done

**1. Get the current event and its attendees.**

🔸 GET `/events/{event-id}` via the Graph API.

🔸 Capture the `attendees` array from the JSON response.

**2. Build the new attendee object(s).**

🔸 Each needs an `emailAddress` (with `address` and `name`) and a `type` (e.g. `required`).

**3. Merge existing and new attendees without duplicates.**

🔸 `union(existingAttendees, newAttendees)`.

**4. Write the updated list back to the event.**

🔸 PATCH `/events/{event-id}` with the merged `attendees` array.

🔸 Set `"hideAttendees": true` in the request body.

**5. Optional: grab the full sample flow from GitHub.**

🔸 [EventCoordination.json](https://github.com/MarceLehmann/CodeSnippets/blob/main/EventCoordination.json)

## 🎉 Result
Attendees are added or updated quietly, keeping notification noise to a minimum, and the guest list stays private — participants only see their own RSVP.

## 🌟 Key Advantages

🔸 **Privacy:** the guest list stays hidden, so attendees can't see each other.

🔸 **Notification control:** silent updates instead of an alert flood.

🔸 **Flexible:** add one guest or many with the same call.

---

## 🎥 Video Tutorial
{% include video id="IMhOGfL9ggI" provider="youtube" %}

---

## 🛠️ FAQ
**1. How do I authenticate the Graph API request?**
Register a Microsoft Entra ID app, grant it the `Calendars.ReadWrite` permission, then use Power Automate's HTTP with Microsoft Entra ID connector to obtain a token and call Graph.

**2. What does `hideAttendees = true` do?**
It hides the full guest list so attendees only see their own RSVP and cannot view other participants.

**3. Can I remove attendees silently as well?**
Yes. Retrieve the current `attendees` array, filter out the one you want to remove, then PATCH the event with the updated array and `hideAttendees` set to `true`.

---