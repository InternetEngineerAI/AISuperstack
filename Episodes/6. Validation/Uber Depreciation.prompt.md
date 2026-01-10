Prompt: > "Act as a financial analyst for gig economy workers. 
I want you to create a comprehensive Uber Vehicle Depreciation & Cost-Per-Mile Calculator based on 2026 data.

The calculator should ask for the following inputs:

Initial Value: (Purchase price or current market value)
Current Mileage: (Miles on the odometer now)
Estimated Exit Mileage: (At what mileage will the car be 'retired' from Uber?)
Salvage Value: (Expected resale value at exit mileage)
Annual Uber Miles: (Estimate of miles driven for work per year)

The calculator must output:

Depreciation Per Mile: Calculated as $(Initial Value - Salvage Value) / (Exit Mileage - Current Mileage)$
Annual Depreciation Cost: Total value lost per year based on my driving
The 'Real' Take-Home Pay: A formula where I can input a trip's gross pay and distance to see my profit after depreciation
2026 Tax Context: Briefly explain how this compares to the 2026 IRS Standard Mileage Rate of 72.5 cents

Provide the logic/formulas used and then ask for my vehicle's numbers to begin the calculation.
Key Factors to Include (2026 Context)
If building this as a tool or spreadsheet, ensure these variables are part of the logic:

The Real Cost Formula
Standard depreciation is often "Straight-Line," which is the most practical for Uber drivers.
$ Depreciation\ Per\ Mile = \frac{Current\ Value - Salvage\ Value}{Total\ Miles\ Remaining\ in\ Uber\ Life} $
Tax Deduction Methods
In 2026, you generally choose between:
Standard Mileage Rate (72.5¢): Easiest, includes depreciation, gas, and repairs.
Actual Expenses (MACRS): Allows for accelerated depreciation (like Section 179 or Bonus Depreciation), which is often better if you bought a heavy SUV ($>$6,000 lbs GVWR) or a high-end EV specifically for Uber Black.

The "Hidden" Variable: Deadhead Miles
Remind the user to track Deadhead Miles (miles driven with the app on but no passenger). These miles depreciate the car just as fast as active miles but are often forgotten in profit calculations.