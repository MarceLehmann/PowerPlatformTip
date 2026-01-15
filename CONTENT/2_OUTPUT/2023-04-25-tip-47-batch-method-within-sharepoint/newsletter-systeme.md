# PowerPlatformTip #47: Batch-Method within SharePoint

**Boost SharePoint performance with Batch requests.
    
        
            #PowerPlatformTip 47
            Batch-Method within SharePoint

        
        
            
                

**TL;DR**

                Creating 100 items? Don't trigger 100 flows. Use the SharePoint REST API $batch** endpoint to create/update up to 1000 items in a single HTTP call.

            

            
                

**Why This Matters**

                Looping through 'Create Item' action is slow and consumes API limits rapidly. Batching is 100x faster and safer for bulk operations, preventing throttling and timeouts.

            

            
                

**Deep Dive: How to Implement**

                
        

1. **Use 'Send HTTP Request'**: Use the 'Send an HTTP request to SharePoint' action. Method: **POST**. URL: _api/$batch.
        

2. **Set Headers**: Content-Type must be multipart/mixed; boundary=batch_GUID. The boundary string separates your requests.
        

3. **Construct Body**: You need to build a text payload where each 'Create Item' request is separated by the boundary string. Use a 'Select' action to generate these text blocks from an array.Be careful with newlines! The batch format is very strict about spacing.
        
            

            
                

**3 Real-World Use Cases**

                
        

**📥 Bulk Import**
Importing 500 rows from Excel/SQL to a SharePoint list in seconds instead of minutes.
        

**🔄 Archive/Migration**
Moving old items to an archive list in bulk at the end of the year.
        

**📝 Audit Logs**
Writing multiple audit log entries at once at the end of a flow execution.
        
            

            
                

**Quick FAQ**

                
        

**Q: Limit per batch?**
SharePoint allows up to 1000 requests in a single batch, but 50-100 is often a safer sweet spot for timeout management.
        

**Q: Is it complex?**
It requires understanding REST API syntax, but the performance gain is worth the learning curve.
        

**Q: Does it work for Updates?**
Yes, you can Batch Create, Update, and Delete items.
        
            

            
                [Get Help Implementing This Solution](https://www.powerplatformtip.com)
            
            
            **P.S.** Once you master the Batch API, 'Apply to Each' loops for SharePoint updates will feel painfully slow.

        
        
            #PowerPlatform #PowerApps #SharePoint #PowerPlatformTip

            © 2026 All rights reserved

---
[Mehr erfahren](https://www.powerplatformtip.com)
