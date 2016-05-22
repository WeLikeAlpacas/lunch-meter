# Lunch Meter #

A software to manage the kicthen purchases based on how many units (places where people eat) exists.

## MVP ##

The software should accept the creation of recipes, units, menu and measuring the quantity of ingredients should be bought.

### Recipe ###

A recipe consist in a list of ingredients and which quantity it is needed to serve ONE person. Should be possible to register general recipes and per unit recipes.

### Units ###

Units are places where people eat. It can have recipes and hold how many people work there.

### Menu ###

Are a monthly schedule of which recipes will be prepared by each day per unit. A day can have more than 1 recipe. While building the menu we only should select per unit recipes or general recipes.

### Calculating purchases reports ###

Based on which recipes and how many people per unit per time schedule (default 1 week) the software should calculate the ingredients' quantities needed and inform that as report.  
