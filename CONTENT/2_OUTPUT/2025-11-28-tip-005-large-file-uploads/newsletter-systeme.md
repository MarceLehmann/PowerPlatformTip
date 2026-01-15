# PowerPlatformTip #005: Large File Uploads

Upload files up to 250MB to SharePoint using standard connectors - no premium license required
    
    
        
            
                
                    
                    
                    
                        
                            

**#PowerPlatformTip 005**

                            Upload Large Files to SharePoint Without Premium Licenses

                        
                    
                    
                    
                    
                        
                            
                            
                            
                                **TL;DR**
                                The Office 365 Groups connector's HttpRequest action lets you upload files up to 250MB directly to SharePoint from Power Apps - no premium license, no Power Automate flow, and no binary data corruption. This overlooked standard connector uses Microsoft Graph API to bypass the severe limitations of the traditional SharePoint connector.

                            
                            
                            
                            
                                Why This Matters
                                Every Power Apps developer has hit the wall: you build a beautiful app, users love it, then someone tries to upload a 20MB PDF and everything breaks. The standard SharePoint connector chokes on files larger than 10-15MB and frequently corrupts binary data like images and documents.

                                Your options have been expensive (premium connectors), complex (custom Azure Functions), or limiting (force users to upload smaller files). Meanwhile, citizen developers and small teams without premium licenses have been stuck with workarounds that hurt user experience and productivity.

                                The Groups 365 connector changes this equation entirely - it's been hiding in plain sight in your standard connector library all along.

                            
                            
                            
                            
                                Deep Dive: How to Implement
                                
                                
                                    1
                                    **Get Your SharePoint Site and Drive IDs**
                                    Before you can upload files, you need two unique identifiers from your SharePoint environment. Navigate to your SharePoint site and use Graph Explorer or PowerShell to extract the site ID and the specific document library's drive ID. These are long alphanumeric strings that uniquely identify your destination.

                                    
                                        **💡 Tip:** Store these IDs in your app's OnStart property as global variables - you'll reference them multiple times and this keeps your formulas clean.
                                    
                                
                                
                                
                                    2
                                    **Add the Office 365 Groups Connector**
                                    In Power Apps Studio, add a new data connection and search for "Office 365 Groups" (not the SharePoint connector). Authenticate with your organizational account. This connector includes the powerful HttpRequest action that lets you call Microsoft Graph API directly.

                                    
                                        **⚠️ Common Pitfall:** Don't confuse this with "Office 365 Outlook" or the standard "SharePoint" connector. You specifically need "Office 365 Groups" which includes HTTP capabilities.
                                    
                                
                                
                                
                                    3
                                    **Create Your File Upload Control**
                                    Add an Attachment control or use the Add Picture control depending on your file types. These controls capture files as binary data that you'll pass directly to the API. Reference the file content using standard syntax like First(Attachments).Value.

                                
                                
                                
                                    4
                                    **Implement the Upload Formula**
                                    Use this formula structure in your button's OnSelect property or form's OnSuccess:

                                    
                                    With(

&nbsp;&nbsp;&nbsp;&nbsp;{

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;siteId: "YOUR_SITE_ID_HERE",

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;driveId: "YOUR_DRIVE_ID_HERE",

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;folderName: "YOUR_FOLDER_NAME_HERE"

&nbsp;&nbsp;&nbsp;&nbsp;},

&nbsp;&nbsp;&nbsp;&nbsp;Office365Groups.HttpRequest(

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"https://graph.microsoft.com/v1.0/sites/" & siteId &

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"/drives/" & driveId &

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"/root:/" & folderName & "/" & First(Attachments).Name & ":/content",

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"PUT",

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;First(Attachments).Value

&nbsp;&nbsp;&nbsp;&nbsp;)

)
                                    
                                    The With() function creates local variables for cleaner code. The HttpRequest action uses PUT method to upload the binary file content directly to the Graph API endpoint.

                                
                                
                                
                                    5
                                    **Add Error Handling and Progress Feedback**
                                    Wrap your upload in proper error handling using IfError() to catch network timeouts or permission issues. Add a loading spinner or progress indicator since larger files take time to upload. Consider file size validation before attempting upload.

                                    
                                        **💡 Tip:** Test extensively with your users' actual network conditions. A 200MB file works great on office WiFi but may timeout on home connections under 20 Mbps upload speed.
                                    
                                
                                
                                
                                    6
                                    **Set Realistic File Size Expectations**
                                    While the connector technically supports up to 250MB, practical limits depend on connection speed. Document your file size policy: suggest 100MB maximum for most users, and reserve 200MB+ uploads for users on fast, stable networks.

                                
                            
                            
                            
                            
                                3 Real-World Use Cases
                                
                                
                                    📄 Document Management System
                                    Replace clunky SharePoint forms with a custom Canvas App that lets employees upload contracts, proposals, and presentations up to 100MB. Perfect for sales teams managing large pitch decks or legal departments handling comprehensive contract packages.

                                
                                
                                
                                    🎨 Creative Asset Library
                                    Marketing teams can upload high-resolution images, video files, and design assets directly from a mobile app. The binary data handling ensures photos and graphics maintain perfect quality without the corruption issues of standard connectors.

                                
                                
                                
                                    🔧 Field Service Reports
                                    Technicians in the field capture detailed inspection reports with multiple high-quality photos and video clips. The larger file limits accommodate comprehensive documentation without forcing users to take fewer photos or reduce quality.

                                
                            
                            
                            
                            
                                Tooling & Ready-to-Use Snippets
                                **Get Site ID using Graph Explorer:**

                                https://graph.microsoft.com/v1.0/sites/{hostname}:/sites/{site-name}
                                
                                **Get Drive ID using Graph Explorer:**

                                https://graph.microsoft.com/v1.0/sites/{site-id}/drives
                                
                                **Error Handling Wrapper:**

                                IfError(

&nbsp;&nbsp;&nbsp;&nbsp;Office365Groups.HttpRequest(...),

&nbsp;&nbsp;&nbsp;&nbsp;Notify("Upload failed. Check file size and connection.", NotificationType.Error)

)
                            
                            
                            
                            
                                Implementation Checklist
                                ✓ Obtain and verify SharePoint site ID and drive ID for target library
                                ✓ Add Office 365 Groups connector to your Power App
                                ✓ Implement HttpRequest formula with correct Graph API endpoint
                                ✓ Add error handling for timeouts and permission issues
                                ✓ Test with various file sizes on different network speeds
                                ✓ Document file size limits for your specific user base
                            
                            
                            
                            
                                Quick FAQ
                                
                                
                                    Q: Why does my 150MB file upload fail sometimes?
                                    A: HttpRequest actions have timeout limits affected by upload speed. On slower connections (under 20 Mbps upload), files over 100MB may timeout. Test with your users' typical network conditions and adjust maximum file size accordingly.

                                
                                
                                
                                    Q: Can I use this same approach in Power Automate?
                                    A: Absolutely. The Office 365 Groups connector works identically in Power Automate flows. Use the same HttpRequest action and Graph API endpoint, referencing trigger outputs or previous actions instead of attachment controls.

                                
                                
                                
                                    Q: What if I need to upload files larger than 250MB?
                                    A: For files exceeding 250MB, you must use the Graph API's createUploadSession endpoint, which requires chunking files into multiple requests. The simple PUT method covered here is specifically designed for files under 250MB.

                                
                            
                            
                            
                            
                                [Get Help Implementing This Solution](https://yourwebsite.com/contact?utm_source=newsletter&utm_medium=email&utm_campaign=powerplatformtip005&utm_content=cta_button)
                                Ready to solve your file upload challenges? Let's talk about your specific requirements.

                            
                            
                            
                            
                                **P.S.** I discovered this solution after exhausting every "official" recommendation. Sometimes the best answers aren't in the documentation - they're in understanding how the pieces fit together differently. This Groups connector approach has saved multiple projects from expensive premium upgrades. If you implement this and discover additional optimizations or use cases, I'd love to hear about them. Real-world experience always beats theory.
                            
                            
                            
                            
                                🙏 Credits & Attribution
                                The solution described in this newsletter is based on the approach originally shared by **Laura Rogers** on her blog at IW Mentor. Her article provided the key insight that the Office 365 Groups connector can upload files directly to SharePoint without requiring Power Automate. Full credit to her for discovering and publishing this method.

                                **Source:** [Power Apps File Upload to SharePoint Libraries (No Flow) - IW Mentor](https://www.iwmentor.com/pages/blog/power-apps-file-upload-files-to-sharepoint-libraries-no-flow?utm_source=newsletter&utm_medium=email&utm_campaign=powerplatformtip005&utm_content=credit_link)

                            
                            
                        
                    
                    
                    
                    
                        
                            #PowerPlatform #PowerApps #SharePoint #PowerPlatformTip

                            © 2026 All rights reserved

---
[Mehr erfahren](https://www.powerplatformtip.com)
