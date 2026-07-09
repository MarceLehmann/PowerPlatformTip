---
title: "#PowerPlatformTip 152 – 'Build a Time Picker with One Line using Sequence()'"
date: 2026-02-19
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - PowerFx
  - Sequence
  - TimePicker
  - PowerPlatformTip
excerpt: "Need a time picker in Power Apps? Skip the clunky hour/minute controls. A single Sequence() line fills a dropdown with every 15-minute slot from 00:00 to 23:45 — and the same trick powers alphabets, date ranges, color palettes and more."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

Building a time picker in Power Apps usually means stacking hour and minute dropdowns or fiddling with input masks.
There's a much cleaner way: the **`Sequence()`** function generates a table of numbers you can transform into anything — including a full list of time slots — in a single line of Power Fx.
Credit for the neat time-picker one-liner goes to Matthew Devaney, who popularised this pattern.

## 💡 Challenge
You want users to pick a time in 15-minute steps. The usual approaches — two linked dropdowns for hours and minutes, or a free-text field with validation — are clunky, error-prone, and take real effort to build and maintain.

## ✅ Solution
Feed a **Dropdown** with a `Sequence()`-generated table. `Sequence(Records, Start, Step)` returns a single-column table (column name **Value**) of sequential numbers. Wrap it in `ForAll()` to turn each number into a `Time` value, and you get every quarter-hour of the day with zero manual data.

Set the **Items** property of a Dropdown to:

```powerapps
ForAll(Sequence(96), Time(0, Value * 15 - 15, 0))
```

96 slots × 15 minutes = 24 hours, so the list runs from **00:00 to 23:45**.

## 🔧 How it's done

1) **Add a Dropdown control** to your screen.
   🔸 Insert → Input → Drop down.

2) **Set the Items property** to the one-liner:
   ```powerapps
   ForAll(Sequence(96), Time(0, Value * 15 - 15, 0))
   ```
   🔸 `Sequence(96)` yields 1…96. `Value * 15 - 15` maps those to 0, 15, 30 … 1425 minutes — exactly 00:00 through 23:45.

3) **Format the display** so users see a clean time.
   🔸 If the values show as full date/times, wrap them: `ForAll(Sequence(96), Text(Time(0, Value * 15 - 15, 0), "hh:mm"))`.

4) **Read the selected value** with `Dropdown1.Selected.Value`.
   🔸 Use it directly in a `Patch()`, a variable, or combine it with a date via `DateAdd`.

## 🎉 Result
A fully working, scrollable time picker in 15-minute increments — built from a single formula, with no static data table to maintain. Change the interval by editing one number, and you're done.

## 🌟 Key Advantages
🔸 **One line, zero data:** no hardcoded list, no extra collection to maintain.
🔸 **Instantly adjustable:** want 30-minute steps? Use `Sequence(48)` and `Value * 30 - 30`.
🔸 **Reusable pattern:** the same `Sequence()` + `ForAll()` combo generates far more than times (see below).

### Bonus: more creative `Sequence()` uses
```powerapps
// Next 7 days (Microsoft Learn's recommended pattern)
ForAll(Sequence(7), DateAdd(Today(), Value, Days))

// Alphabet A–Z (65 = 'A')
ForAll(Sequence(26, 65), Char(Value))

// Countdown 20 → 1 (negative step)
Sequence(20, 20, -1)

// Odd numbers only
Sequence(20, 1, 2)

// Business hours, 30-minute slots from 08:00
ForAll(Sequence(21), Time(8, 30 * (Value - 1), 0))

// 12 calendar month names
ForAll(Sequence(12), Text(Date(Year(Today()), Value, 1), "mmmm"))
```

## 🛠️ FAQ
Q1: How many records can `Sequence()` generate?
A: Between 0 and 50,000. Values are rounded down to the nearest whole number, and 0 returns an empty table.

Q2: What is the column called in the generated table?
A: `Value`. That's why the formulas reference `Value` inside `ForAll()`.

Q3: Why `Value * 15 - 15` instead of `Value * 15`?
A: `Sequence(96)` starts at 1, so without the `- 15` the first slot would be 00:15 and you'd miss 00:00. Subtracting one step shifts the list to start at midnight. (Alternatively, `Sequence(96, 0)` starts at 0 and you can drop the `- 15`.)

Q4: Can I change the step size?
A: Yes. `Sequence(Records, Start, Step)` accepts a `Step` argument, and it can be negative to count down. For times, just adjust both the record count and the minute multiplier.

## 🔗 Related Tips
- [#PowerPlatformTip 84 – Tabbing in Dynamic Forms](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-84-tabbing-in-dynamic-forms/) — using `Sequence()` for reliable gallery binding.
- [#PowerPlatformTip 93 – Add RowNumbers](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-93-add-rownumbers/) — dynamic row numbering with `Sequence()`.
