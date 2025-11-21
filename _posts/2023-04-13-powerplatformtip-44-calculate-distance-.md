---
title: "PowerPlatformTip 44 – Calculate the Distance"
date: 2023-04-13
modified: 2025-11-21
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - PowerAutomate
  - DistanceCalculation
  - Geolocation
  - Haversine
  - LocationServices
  - MarcelLehmann
excerpt: "Calculate accurate great-circle distances directly in your Power Platform app using the Haversine formula and a ready-made JSON snippet."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

Here’s a cool tip to calculate the distance between two places without relying on premium services like Google or Bing maps.

## 💡 Challenge

How do you provide accurate, real-time location-based distance calculations inside PowerApps or Power Automate, without extra costs?

## ✅ Solution

You can use the Haversine formula – a proven geospatial calculation mechanism.
- There’s a ready-to-use code snippet available:  
  [CalculateDistance.json @ GitHub – Marcel Lehmann](https://github.com/MarceLehmann/CodeSnippets/blob/main/CalculateDistance.json)
- Just copy the JSON logic and paste into your Power Platform workflow (typically as an inline calculation or custom connector).
- Replace the latitude and longitude values for locations A and B with your own values.

## 🔧 How it's done

1. Obtain coordinates:
   - Manually input latitude and longitude for each location, or use the PowerApps location function to fetch the user/device position (`Location.Latitude`, `Location.Longitude`).
2. Drop the values into the shared script or formula:
   ```
   // Example for PowerApps
   With(
     {
       r: 6371000,
       p: (Pi() / 180),
       latA: YourStartLatitude,
       lonA: YourStartLongitude,
       latB: YourEndLatitude,
       lonB: YourEndLongitude
     },
     Round(
       (2 * r) * Asin(
         Sqrt(
           0.5 - Cos((latA - latB) * p) / 2 +
           Cos(latB * p) * Cos(latA * p) * (1 - Cos((lonA - lonB) * p)) / 2
         )
       ),
       2
     )
   )
   ```
3. For JSON users, import the code from the referenced snippet and wire up your variables according to context.
4. The result is your distance in meters, output instantly in your app or flow.

## 🎉 Result

Enjoy accurate, fast, and cost-effective distance calculations for any business scenario – including logistics, travel, or field service.

## 🌟 Key Advantages

- No dependency on paid mapping services
- Works both in manual and automated scenarios
- Can leverage device location for dynamic, user-centered calculations

## 🛠️ FAQ

Q1: What is the Haversine formula?  
A1: A mathematical function for calculating the shortest distance between two points on the Earth, given their latitude and longitude.

Q2: How do I get my coordinates in PowerApps?  
A2: Use built-in location functions or user input fields to collect latitude and longitude.

Q3: Can I use this in Power Automate as well?  
A3: Yes, simply adapt the code for use in expressions, custom connectors, or flow steps.
