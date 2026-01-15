# PowerPlatformTip #10: Use all variables in PowerApps

**Stop limiting yourself to Set() and UpdateContext().
    
        
            #PowerPlatformTip 10
            Use all variables in PowerApps

        
        
            
                

**TL;DR**

                Master With** for scoped calculations and **Param** for deep linking. Moving beyond basic variables is the first step to professional-grade apps.

            

            
                

**Why This Matters**

                Sticking to just Set (Global) and UpdateContext (Local) leads to cluttered app state and performance issues. Using the right variable type for the job makes your code cleaner, faster, and easier to debug.

            

            
                

**Deep Dive: How to Implement**

                
        

1. **Use 'Set' Sparingly**: Global variables persist everywhere. Use them only for user preferences or app-wide configurations loaded on Start.
        

2. **Prefer 'UpdateContext'**: Keep variables local to the screen whenever possible. This reduces memory usage and prevents naming conflicts.
        

3. **Master 'With'**: The most underused function. Use it to create temporary 'variables' inside a formula. It improves readability and avoids unnecessary recalculations without polluting app state.Example: With({currentUser: User()}, Label.Text = currentUser.FullName)
        

4. **Leverage 'Param'**: Capture values from the App URL. Essential for deep linking users directly to a specific record or screen.
        
            

            
                

**3 Real-World Use Cases**

                
        

**🔍 Deep Linking**
Send emails with a link like ...&ID=123. Use Param("ID") in OnStart to navigate directly to that record.
        

**🧮 Complex Math**
Use With() to calculate intermediate values (like tax or totals) inside a Patch function without creating permanent variables.
        

**🚀 Performance**
Replace heavy global variable lookups with local context variables to speed up screen transitions.
        
            

            
                

**Quick FAQ**

                
        

**Q: When should I use With vs UpdateContext?**
Use With for values needed *only* inside one specific formula. Use UpdateContext if you need the value elsewhere on the screen.
        

**Q: Can I change a With variable?**
No, With variables are immutable (read-only) within their scope. This makes them predictable and bug-free.
        

**Q: Does Param work in Play mode?**
Yes, but you need to manually append parameters to the URL in your browser to test it.
        
            

            
                [Get Help Implementing This Solution](https://www.powerplatformtip.com)
            
            
            **P.S.** If you aren't using With() yet, try it on your next complex If() statement. You'll thank me later.

        
        
            #PowerPlatform #PowerApps #SharePoint #PowerPlatformTip

            © 2026 All rights reserved

---
[Mehr erfahren](https://www.powerplatformtip.com)
