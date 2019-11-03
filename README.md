## HACK OHI/O 2019: Energy Consumption at Ohio State
### Team members: Cole Smith, Elizabeth Gilbert, Matthew Walker

Energy data from: https://github.com/BabyBalooga/hackOHI.O
OSU building data from: https://gismaps.osu.edu/OSUMaps/Default.html?#

## Presentation

Our team completed the Engie challenge at HackOHI/O 2019, interactively mapping their data on energy consumption of Ohio State buildings in 2017-18 over time. We used plotly and dash in Python, and provided context around the buildings in time relative to their range of values and building occupancy. 

What better way is there to visualize energy usage than by actually seeing the buildings. With a timelapse of a regular day on campus, you can see the colors of the buildings change over time corresponding to that building's use of energy. In the morning on a regular school day, you may see the dorms lighting up red because everybody's getting ready to leave to go to school. In the middle of the day, you may see the academic buildings lighting up because everybody's plugging in their computers and using electricity. A nice aspect of using the interactive plots is that you can hover over buildings and see charts in the tooltip that give context about the relative energy being used at that point in time.  

The bar chart for the tooltip shows the energy stream usage for that building at that point in time, relative to the minimum and maximum energy usage over time for the building, to understand the snapshot relative to all time. Connecting in occupancy data on the Residence Halls, a strong (r = 0.5) correlation between estimated number of occupants and value of energy usage. 

The energy usage for one building at one point in time is represented across the four categories as values more interpretable than units of kWh and KBTU/HR. For example, 150,000 KBTU/HR is equivalent to brewing 548 pots of coffee. 

## Future Work

Using a new technology in a 25 hour time frame (24 hours + daylight savings time), we built out maintainable front end visualization code and back end structure for connecting and automatically updating the plots and statistics into one fluid dashboard, but weren't able to create all of the auto-updating functionality during the hackathon. In the future, we would like to have the bar chart and statistics update relative to the building and time frame selected by the user. 