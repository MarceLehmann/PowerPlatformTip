---
title: "#PowerPlatformTip 158: 'Return Flow Data to Power Apps with ParseJSON (No Premium)'"
date: 2026-05-14
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - PowerAutomate
  - PowerFx
  - JSON
  - ParseJSON
  - PowerPlatformTip
excerpt: "Return one JSON text output from 'Respond to a Power App or flow' and unpack it in Power Apps with ParseJSON. Nested objects, arrays and typed values in a single output, no dozens of return fields, and no premium license because it runs in app context."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Send complex data back from a flow as **one text output** containing JSON via *Respond to a Power App or flow*, then rebuild it in Power Apps with **`ParseJSON`**. You get nested records, arrays and typed values from a single field, and it stays **standard/non-premium** because the flow runs in the Power Apps app context.

> 🧰 **Free tool:** Paste a JSON sample and get ready-to-use Power Fx — field access with casts, a `Type()` definition and a `ClearCollect`/`ForAll` for arrays (with a custom collection name): **[ParseJSON in Power Apps converter](https://tools.powerplatformtip.com/tools/parsejson-converter/)**.

Returning structured data from Power Automate to a canvas app used to mean either the old *Split* string trick or defining a long list of individual return outputs. Neither scales for nested objects or arrays.
The modern way: return a **single JSON string**, and let **`ParseJSON`** turn it back into a `Dynamic` value (or a typed object) inside Power Apps. One output, any depth.

## 💡 Challenge
Your flow produces a complex result, for example a customer record with a list of orders, and you want it in your canvas app.

- *Respond to a Power App or flow* only offers flat, typed outputs (Text, Number, Boolean, …). Modelling a nested/array structure means dozens of fields, or it is simply not possible.
- Many makers reach for the **Response (HTTP)** action instead, which shows a **premium diamond**. That action belongs to the Request/Response (HTTP) connector and *is* premium.
- The result: over-engineered flows or an accidental premium dependency for a scenario that does not need one.

## ✅ Solution
Serialize your result as **JSON text**, return it in **one** *Respond to a Power App or flow* output, and parse it in Power Apps with **`ParseJSON`**.
*Respond to a Power App or flow* (from the **Power Apps** connector) is **standard**. As long as the rest of the flow uses no premium connector, the flow runs in app context and needs **no premium license**, only a Microsoft 365 license. That is the "shown as premium but it isn't" confusion: the premium diamond you saw is on the HTTP **Response** action, not on this one.

## 🔧 How it's done

**1. Trigger the flow from Power Apps.**

🔸 Use the **Power Apps (V2)** trigger so inputs are typed and the flow stays in app context.

**2. Build the JSON in the flow.**

🔸 Shape your data with **Select** / **Compose**, or wrap objects and arrays and run them through **`json()`**. Example payload:

```json
{
  "customer": { "name": "Jane Doe", "vip": true, "since": "2022-09-01" },
  "orders": [
    { "id": 1001, "total": 149.90 },
    { "id": 1002, "total": 32.50 }
  ]
}
```

**3. Return it as one text output.**

🔸 Add *Respond to a Power App or flow* → add a **Text** output, e.g. `jsonResult` → set its value to the JSON string (the `Compose`/`json()` output). Only this **one** field leaves the flow.

**4. Parse it in Power Apps (dynamic).**

🔸 On your button's **OnSelect**, capture the response and parse it:

```power
Set( gblResp, ParseJSON( ReturnFlowData.Run(TextInput1.Text).jsonresult ) );

// Access nested fields with dot notation + explicit casting
Set( custName, Text( gblResp.customer.name ) );
Set( isVip,    Boolean( gblResp.customer.vip ) );
Set( since,    DateValue( gblResp.customer.since ) );
```

🔸 Turn the array into a typed table with `Table()` + `ForAll()`:

```power
ClearCollect(
    colOrders,
    ForAll(
        Table( gblResp.orders ),
        { id: Value( ThisRecord.Value.id ), total: Value( ThisRecord.Value.total ) }
    )
)
```

**5. (Optional) Skip the casting with a typed `ParseJSON`.**

🔸 Pass a `Type` as the second argument so the result is directly usable, no per-field conversion:

```power
Set(
    gblTyped,
    ParseJSON(
        ReturnFlowData.Run(TextInput1.Text).jsonresult,
        Type(
            {
                customer: { name: Text, vip: Boolean, since: Date },
                orders: Table( { id: Number, total: Number } )
            }
        )
    )
);

// gblTyped.customer.name and gblTyped.orders are ready to use, no Text()/Value() needed
```

## 🎉 Result
Any structure, nested records and arrays included, travels back to Power Apps through a **single** standard output. No exploding return-field lists, no old Split hacks, and **no premium license** for a scenario that shouldn't need one.

## 🌟 Key Advantages

🔸 **One output, any shape:** nested objects and arrays in a single JSON string instead of dozens of flat return fields.

🔸 **Standard, not premium:** *Respond to a Power App or flow* is a Power Apps connector action; it runs in app context on a Microsoft 365 license. The premium diamond lives on the separate HTTP **Response** action.

🔸 **Typed on demand:** use the `Type` argument of `ParseJSON` to get ready-to-use records and tables without manual casting.

🔸 **Future-proof:** replaces the legacy *Split* string method for returning arrays.

## 🛠️ FAQ

**Q1: Is the *Respond to a Power App or flow* action premium?**

No. It is part of the **Power Apps** connector and is standard. The premium diamond you may have seen is on the **Response** action of the Request/Response (HTTP) connector, which is a different action. As long as the flow uses no premium connector, it runs in app context and needs only a Microsoft 365 license.

**Q2: Why does `ParseJSON` need `Text()`, `Value()` or `Boolean()` around fields?**

Without the `Type` argument, `ParseJSON` returns a **Dynamic** value. JSON has no dedicated date/GUID types, and numbers/booleans still need an explicit cast for safe use in formulas. Use `Text()`, `Value()`, `Boolean()`, `DateValue()` etc., or pass a `Type` as the second argument to skip casting.

**Q3: How do I handle a JSON array?**

Wrap it with `Table( gblResp.arrayField )` to get a single-column table of Dynamic values, then use `ForAll()` with `ThisRecord.Value.<field>` to project it into a typed table (see step 4).

**Q4: My dates come back wrong. Why?**

JSON only stores dates as strings. Return them in **ISO 8601** (e.g. `2022-09-01`) and convert with `DateValue()`; for other formats, wrap in `Text()` first. `DateValue`/`DateTimeValue` use the current user's language settings.

**Q5: Is there a size limit?**

Keep payloads reasonable. Very large results should be paged or stored (e.g. in a SharePoint/Dataverse source the app reads directly) rather than pushed through a single flow response.

## 🔗 Related Tips
- [#PowerPlatformTip 128: Dynamic Data Retrieval](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-128-dynamic-data-retrieval/), using Parse JSON with dynamic keys on the flow side.
- [#PowerPlatformTip 37: Table to JSON](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-37-table-to-json/), turning a two-column table into JSON in Power Automate.
- [Return an Array from PowerAutomate to PowerApps (Split Method)](https://www.powerplatformtip.com/article/powerplatform/2022/05/23/return-an-array-from-powerautomate-to-powerapps-split-method/), the legacy approach this tip modernizes.
- 🧰 [ParseJSON in Power Apps converter](https://tools.powerplatformtip.com/tools/parsejson-converter/), generate the Power Fx (`ParseJSON`, `Type()`, `ClearCollect`/`ForAll`) from a JSON sample.
