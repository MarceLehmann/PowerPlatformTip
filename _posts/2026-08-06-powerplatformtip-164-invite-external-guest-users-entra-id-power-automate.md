---
title: "#PowerPlatformTip 164: 'Add External Users to Microsoft Entra ID (Azure AD) with Power Automate'"
date: 2026-08-06
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - EntraID
  - GraphAPI
  - B2B
  - Guests
  - PowerPlatformTip
excerpt: "Automate B2B guest onboarding: POST to the Microsoft Graph /invitations endpoint from a flow to add an external user to Microsoft Entra ID (Azure AD) as a guest - send the default invite or craft your own from the returned inviteRedeemUrl. No app registration."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** `POST /v1.0/invitations` with `invitedUserEmailAddress` and `inviteRedirectUrl` adds an external user to Microsoft Entra ID (Azure AD) as a **guest**. Set `sendInvitationMessage: true` to let Graph email the invite, or use the returned `inviteRedeemUrl` to send your own. Run it via *HTTP with Microsoft Entra ID* - no app registration.

Onboarding external partners, freelancers, or customers as guests usually means clicking through the Entra admin center one person at a time. When that onboarding is already part of a process - a new project, a signed contract, an approved access request - you want it to happen automatically. Microsoft Graph's B2B **invitation** API does exactly that from a flow.

## 💡 Challenge
An external collaborator needs access to a Team, a SharePoint site, or an app. Today someone manually invites each guest in the Microsoft Entra admin center, then follows up to grant access. It's repetitive, easy to forget, and disconnected from the request or approval that triggered it.

## ✅ Solution
Use the Microsoft Graph **create invitation** endpoint to add the external user as a B2B guest straight from Power Automate. A single `POST /invitations` creates a `userType: Guest` account and either sends the standard Microsoft invitation email or returns an `inviteRedeemUrl` you can drop into your own branded email. Call it through the preauthorized *HTTP with Microsoft Entra ID* action (see #138) - no app registration, no secret.

## 🔧 How it's done

**1. Add the Graph call.**

🔸 *HTTP with Microsoft Entra ID* → Method `POST`, Uri:

```
https://graph.microsoft.com/v1.0/invitations
```

🔸 Body - only `invitedUserEmailAddress` and `inviteRedirectUrl` are required:

```json
{
  "invitedUserEmailAddress": "jane@partner.com",
  "invitedUserDisplayName": "Jane (Partner Co.)",
  "inviteRedirectUrl": "https://myapps.microsoft.com",
  "sendInvitationMessage": true
}
```

🔸 `inviteRedirectUrl` is where the user lands after redeeming (e.g. `https://myapps.microsoft.com` or your app). `sendInvitationMessage: true` tells Graph to email the invite; omit it (defaults to `false`) if you'll send your own.

**2. Send your own email instead (optional).**

🔸 The `201 Created` response contains `inviteRedeemUrl`. Set `sendInvitationMessage` to `false`, then feed `body('HTTP')?['inviteRedeemUrl']` into a *Send an email (V2)* action for a fully branded onboarding message.

**3. Personalise the standard invite (optional).**

🔸 Add `invitedUserMessageInfo` with a `customizedMessageBody` and `ccRecipients` to include a welcome note and CC the internal sponsor - while still letting Graph handle delivery.

**4. Use the new guest downstream.**

🔸 The response also returns `invitedUser.id`. Use that object id in follow-up calls to add the guest to a group or Team, or to assign a license - all in the same flow.

## 🎉 Result
The moment your process fires - an approval, a form, a new project - the external user is created as a guest in Microsoft Entra ID and invited automatically. No manual admin-center clicks, consistent display names, and you can chain group/Team membership right after. Onboarding that took a support ticket now takes zero clicks.

## 🌟 Key Advantages

🔸 **No app registration:** the *HTTP with Microsoft Entra ID* action authenticates with the connection's identity (#138).

🔸 **Least privilege:** `User.Invite.All` is enough - you don't need broad directory write access.

🔸 **Your email or theirs:** send the default Microsoft invite, or use `inviteRedeemUrl` for a branded one.

🔸 **Chainable:** the returned guest `id` lets you add group/Team membership in the same run.

## 🛠️ FAQ

**Q1: Which Graph permission is the minimum?**

`User.Invite.All` (delegated or application) is the least-privileged permission for creating invitations. `User.ReadWrite.All` and `Directory.ReadWrite.All` also work but grant far more - stick with `User.Invite.All`.

**Q2: Does the guest get access to anything just by being invited?**

No. The invitation creates a `userType: Guest` account, but the person must still **redeem** the invitation, and you must still grant access to specific resources (add them to a group, Team, or app). Inviting ≠ authorising.

**Q3: Can I invite without sending the Microsoft email?**

Yes. Leave out `sendInvitationMessage` (or set it to `false`) - no email is sent. Take `inviteRedeemUrl` from the response and deliver your own onboarding email, or store it for later.

**Q4: Can I add them as a full member instead of a guest?**

Set `invitedUserType` to `Member` in the body. Use this sparingly and deliberately - members have broader default directory access than guests, so `Guest` (the default) is the safer choice for external people.

## 🔗 Related Tips
- [#PowerPlatformTip 138: Graph API via HTTP with Microsoft Entra ID](https://www.powerplatformtip.com/article/powerplatformtip/PowerPlatformTip-138-Graph-API-HTTP/), the auth-free way to run this request.
- [#PowerPlatformTip 87: Licensing, Sharing Canvas Apps with Guests](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-87-licensing-sharing-canvas-apps-with-guests/), what your new guests need to actually use your apps.
- [#PowerPlatformTip 58: HTTP Actions](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-58-http-actions/), the fundamentals of calling REST APIs from a flow.
