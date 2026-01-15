# PowerPlatformTip #59: Handle Dynamic Content Safely

**Stop flow failures with safe navigation (?).
    
        
            #PowerPlatformTip 59
            Handle Dynamic Content Safely

        
        
            
                

**TL;DR**

                item()['prop']** fails if 'prop' is missing. **item()?['prop']** returns null safely. One character makes your flows crash-proof.

            

            
                

**Why This Matters**

                Dynamic data (JSON, API responses) isn't always consistent. Missing fields cause runtime errors that stop your flow. The safe navigation operator (`?`) handles these cases gracefully.

            

            
                

**Deep Dive: How to Implement**

                
        

1. **Identify Risky Access**: Look for expressions accessing properties, e.g. variables('User')['MobilePhone']. If 'MobilePhone' is missing, flow fails.
        

2. **Add the Question Mark**: Change it to variables('User')?['MobilePhone']. Note the **?** before the bracket.
        

3. **Handle Nulls**: Now, if the field is missing, you get null instead of an error. Use coalesce(..., 'Default') to provide a fallback value.Example: coalesce(item()?['Phone'], 'No Phone')
        
            

            
                

**3 Real-World Use Cases**

                
        

**🌐 API Responses**
External APIs often omit fields that have empty values. Safe navigation handles this automatically.
        

**📋 SharePoint Lookups**
Empty lookup columns often return nothing. Direct access crashes; safe access returns null.
        

**✅ Approvals**
Comments fields in approvals might be empty/missing if the user didn't type anything.
        
            

            
                

**Quick FAQ**

                
        

**Q: Does it slow down the flow?**
No, it has zero performance cost.
        

**Q: Used in Filter Array?**
Yes! It's crucial in Filter Array to prevent the filter from crashing on items missing the filter column.
        

**Q: Can I chain them?**
Yes: body('Get_Item')?['Author']?['Email'] safely navigates deep trees.
        
            

            
                [Get Help Implementing This Solution](https://www.powerplatformtip.com)
            
            
            **P.S.** This is the #1 tip I give to anyone debugging 'random' flow failures. It's almost always a missing property.

        
        
            #PowerPlatform #PowerApps #SharePoint #PowerPlatformTip

            © 2026 All rights reserved

---
[Mehr erfahren](https://www.powerplatformtip.com)
