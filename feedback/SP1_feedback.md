## Professor's feedback:

1. Your background of ‘who’, ‘what’ and ‘why’ is a bit sparse. And the ‘why’ doesn’t correlate to the ‘why’ on the prior slide. The ‘what’ doesn’t really make any sense.
2. The background research table was great. I’d add maybe a column that talks about what you thought was lacking in each paper.
3. Why do we have a ‘weather’ and a ‘weather pt 2’ on the fishbone? What is the distinction between these two?
4. Your two ‘features’ slides should really be combined into one data dictionary like I had requested. I’d like to see that fixed for next time. In addition to the feature name and description, there should also be columns for the type of feature (e.g. categorical) and a sample data point from that feature. Don’t use these separate boxes, just use a table, it takes up way less space.
5. Why is the bike-friendliness of the city relevant to the discussion? Also, not sure what the bullet after that means.
6. OK, now I see your data dictionary, so not sure why you included those other two slides. Add a column with the description and you can drop the other two slides.
7. Summary statistics: font too small. Also, reduce the number of decimal places, we only care about two places max. One place would be fine.
8. Slide on ‘further exploration’: Lose the styling, add more detail. For example: you talk about ‘creating a new dataset’ with months and mean temps, but then talk about seasons. How are you relating seasons to months, and which hemisphere are you in? Then, the part about you deciding this “might not be super relevant” is way too vague and casual. Why isn’t it relevant? How did you determine that? And, feeling “inclined to explore it” anyway says to me that you did that exploration out of charity or something. Everything you do must have a reason, not just because you felt inclined to. The way this slide should have appeared was a slide on the relevance of seasonality, with a table showing a summarization of the data by season (or month and then how that relates to season), then some metrics demonstrating its relevance (or not).
9. Slide on data cleaning: ditto. Too much styling, not nearly enough detail. What do you mean ‘irregular date column’? And strings being hard to work with, well yes they are. But that’s not why you transform them. You transform them because you require quantitative values for your model. As for what you did about these: you did not format the date as mm/dd/yyyy because your model would not have accepted the forward slashes as anything useful. And, I don’t need to know what packages you used.
10. PCA slide: this slide and discussion were significantly lacking. Please go back and review the slides I provided on PCA. First, why did you use it? Second, why is 100% your chosen explained variance? If you were going do to that you might as well just use the raw dataset and not do PCA. Next, the table below the chart is entirely too small to read. This slide and the verbal explanation that went with it requires significant improvement for the next time: if you feel it is relevant to your analysis to do PCA then explain why, and fix these deficiencies. If not, then drop it. Don’t just do it for no reason.
11. Why is ‘data features and selection’ the title of your correlation slide? What is your ‘selection’? I know these are data features, what else would they be? What is the key takeaway of this slide? What is the list on the right supposed to signify?
12. The second filtered correlation matrix: why did you choose those two to drop? Why not drop the others? Need explanations.
13. Overall, way too much focus on style, not nearly enough demonstration of knowledge gained in class. Please work on this for the next time.



## What Kenzy remembers

- Column of description of data in dictionary
- Fewer decimal places in summary stats
- Rethink PCA
- Assumptions:
    - The riders check the temp 
    - Rentals are actual riding and not booked
- Don’t drop seasons.
    - Look and see if seasons is correlated with rentals on it’s own; if yes factor it in.
- Create weekday column



## What Will remembers

- Figure out PCA more, 
- determine functioning days of the bike rental company and on which days they lie, weekends/weekdays.
- Keep Seasons in as tehy might help the model, just use a modelt hat can take in categorical data as well as quantiative.
- Remember that we do know the total number of bikes in our company's fleet.
- Our fishbone diagram is still the best diagram here.
- Brad got tons of props for his background slides.


## What Venus remembers

- The assumption she gave is that the bike rental is recreational.
- Fluctuations don't depend on the season and rentals are probably not done ahead of time
- Seasonality is captured with temperatures
- Factor and see variation and season correlated with bike rental by itself
- average inputs such as temperatures and dew points
- negative features account for them when doing scaling
- Look at the weekdays column... days of the week correlation such as weekdays vs weekends
- She said fewer bikes were rented on weekends compared to weekdays.. so think about if its rideshare vs recreational
- Functioning day doesn't correlate to any specific weekday
- Look at weekday and give it some thought, she said she didn't find any correlation so she said we might probably drop it.
- Look at hour of day rentals and break it off by day and night
- Account for negative features when scaling

