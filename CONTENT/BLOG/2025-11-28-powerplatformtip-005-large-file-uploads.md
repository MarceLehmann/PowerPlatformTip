---
title: "#PowerPlatformTip 005 – 'Large File Uploads'"
date: 2025-11-28
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - PowerApps
  - SharePoint
  - GraphAPI
  - PowerPlatformTip
excerpt: "The Office 365 Groups connector enables direct file uploads to SharePoint document libraries up to 250 MB without requiring premium licenses or Power Automate flows. Using the HttpRequest action with Microsoft Graph API endpoints, this approach eliminates binary data corruption issues common with standard SharePoint connectors. Connection speed significantly impacts practical file size limits, with slower networks performing better at 50-100 MB ranges."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 💡 Challenge

Power Apps developers frequently struggle with uploading larger files to SharePoint because the standard SharePoint connector has severe file size limitations and often corrupts binary data. Premium connectors or custom solutions typically require additional licensing costs, creating barriers for citizen developers and organizations with standard licensing. Teams need a reliable, license-friendly method that handles binary data correctly while supporting files beyond the typical 10-15 MB limits.

## ✅ Solution

The Office 365 Groups connector provides an HttpRequest action that calls Microsoft Graph API endpoints directly, bypassing the limitations of standard SharePoint connectors. This standard connector approach supports files up to approximately 250 MB without premium licensing requirements, handles binary data without corruption, and integrates seamlessly into both Canvas Apps and Power Automate flows. The solution leverages the same Graph API methods used by SharePoint Online itself, ensuring compatibility and stability.

## 🔧 How It's Done

1. Obtain your SharePoint site ID and drive ID  
   🔸 Navigate to your SharePoint site and extract the site ID from the URL or use Graph Explorer  
   🔸 Identify the document library drive ID using Graph API endpoints or PowerShell commands  
   🔸 Store these values as variables or constants in your Power App for reuse

2. Configure the Office 365 Groups connector in your Canvas App  
   🔸 Add the Office 365 Groups connector to your app connections  
   🔸 Create an attachment control or file upload control to capture user files  
   🔸 Reference the file using standard Power Apps attachment syntax like First(Attachments).Value

3. Implement the HttpRequest formula with Graph API  
   🔸 Use the PUT method against the Graph API endpoint with the following formula:

```powerapps
With(
    {
        siteId: "YOUR_SITE_ID_HERE",
        driveId: "YOUR_DRIVE_ID_HERE",
        folderName: "YOUR_FOLDER_NAME_HERE"
    },
    Office365Groups.HttpRequest(
        "https://graph.microsoft.com/v1.0/sites/" & siteId &
            "/drives/" & driveId &
            "/root:/" & folderName & "/" & First(Attachments).Name & ":/content",
        "PUT",
        First(Attachments).Value
    )
)
```

🔸 Replace YOUR_SITE_ID_HERE, YOUR_DRIVE_ID_HERE, and YOUR_FOLDER_NAME_HERE with your actual values  
🔸 The formula uses With() to store IDs as local variables for cleaner syntax  
🔸 Add error handling to manage timeout scenarios on slower connections

4. Test with various file sizes and connection speeds  
   🔸 Start with smaller files (10-50 MB) to validate the configuration  
   🔸 Gradually increase file sizes while monitoring upload success rates  
   🔸 Document practical limits based on your users' typical network conditions

## 🎉 Result

Teams can now upload files up to 250 MB directly from Canvas Apps to SharePoint without premium connectors, custom code, or Power Automate flows. Binary files like PDFs, images, and Office documents transfer without corruption, maintaining file integrity and usability. The solution runs on standard licensing, making it accessible to all Power Platform users regardless of their subscription tier.

## 🌟 Key Advantages

🔸 No premium license required – operates entirely with standard Office 365 Groups connector included in base Power Platform licensing  
🔸 Handles binary data correctly – eliminates the corruption issues that plague standard SharePoint connector file uploads  
🔸 Significantly larger file support – supports up to 250 MB compared to 10-15 MB limits of alternative approaches  
🔸 Direct integration – works natively in Canvas Apps without requiring intermediate Power Automate flows  
🔸 Production-ready stability – leverages Microsoft Graph API infrastructure used by SharePoint itself

## 🛠️ FAQ

**Q1: Why does the upload fail for large files on some networks?**  
A: The HttpRequest action has timeout limits that are affected by upload speed. On connections slower than 20 Mbps upload, files larger than 100 MB may timeout before completing. Test with your users' typical network conditions and set file size limits accordingly.

**Q2: Can I use this method in Power Automate flows?**  
A: Yes, the Office 365 Groups connector with HttpRequest action works in both Canvas Apps and Power Automate. The same Graph API endpoint and syntax apply, though you'll reference trigger outputs or previous action results instead of attachment controls.

**Q3: How does this compare to the Upload Session method for very large files?**  
A: For files beyond 250 MB, you must use the Graph API's createUploadSession endpoint, which requires chunking the file into multiple requests. The simple PUT method covered here is ideal for files under 250 MB and provides significantly simpler implementation.

## 🙏 Credits

The final solution described in this article is based on the approach originally shared by Laura Rogers on her blog at IW Mentor. Her article provided the key insight that the Office 365 Groups connector can upload files directly to SharePoint without requiring Power Automate. Full credit to her for discovering and publishing this method.

**Source:** [Power Apps File Upload to SharePoint Libraries (No Flow)](https://www.iwmentor.com/pages/blog/power-apps-file-upload-files-to-sharepoint-libraries-no-flow)
