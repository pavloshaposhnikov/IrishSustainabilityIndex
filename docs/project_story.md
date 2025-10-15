# The Irish Cities Sustainability Index: My First Data Science Project

## By Shaposhnikov Pavlo, Final Year Economics & Finance Student
### Application for Trinity College Dublin Master's Program in Statistics and Sustainability

---

## How It Started: A Simple Question

As a final year Economics and Finance student, I've always been interested in how we measure what really matters in society. During a module on urban economics, our lecturer mentioned that traditional economic indicators like GDP don't capture the full picture of how livable a city actually is. This got me thinking: "What if I could create a simple way to compare Irish cities on sustainability?"

I had never done any serious programming before, but I was determined to learn. The idea was straightforward: collect some basic data about Irish cities, figure out how to compare them fairly, and see what patterns emerge.

## The Learning Curve: From Zero to Something

### Week 1-2: Learning Python (The Hard Way)
I started with YouTube tutorials and online courses. The first few days were frustrating—I couldn't even figure out how to install Python properly on my laptop. But I kept at it, spending evenings after lectures trying to understand basic concepts like variables and loops.

My first "success" was a simple script that could read a CSV file and print the contents. It felt like a major achievement!

### Week 3-4: Finding the Data
This was harder than I expected. I spent hours on government websites trying to find data that was:
- Actually available for download
- Comparable across different cities
- Recent enough to be relevant

I discovered that Irish government data isn't always easy to find or use. Some websites had broken links, others required complex forms to fill out. I learned to be patient and persistent.

### Week 5-6: The Four Basic Metrics
I settled on four simple metrics that seemed important and were actually available:

1. **Air Quality**: PM2.5 levels from EPA Ireland
2. **Green Spaces**: Percentage of city area that's green (from basic calculations)
3. **Public Transport**: Number of bus/rail stops per square kilometer
4. **Waste Management**: Recycling rates from local authority reports

These aren't perfect, but they're measurable and meaningful.

## The Technical Challenges: Learning as I Went

### The Data Collection Problem
My first attempt at data collection was... messy. I was manually copying numbers from websites into Excel spreadsheets. This took forever and was full of errors. I realized I needed to learn how to programmatically access data.

After watching many tutorials, I figured out how to use Python's `requests` library to download data from websites. It didn't always work (some websites block automated access), but it was a start.

### The Normalization Challenge
This was the hardest part for me. I knew I needed to make different metrics comparable, but I didn't understand the statistics behind it. I spent a week reading about z-scores, min-max normalization, and other statistical concepts that weren't covered in my Economics degree.

I ended up using a simple approach: convert everything to a 0-100 scale where 100 is the best possible score. It's not sophisticated, but it works.

### The Weighting Question
How do you combine air quality, green spaces, transport, and waste management into one score? I didn't know, so I used equal weights (25% each). I know this is simplistic, but it seemed fair and transparent.

## The Results: What I Discovered

### The Surprising Findings
When I finally got everything working, the results were interesting:

1. **Galway came out on top** - This surprised me because I expected Dublin to win
2. **Dublin ranked last** - Despite having the best public transport, poor air quality and limited green spaces hurt its overall score
3. **Smaller cities often outperformed larger ones** - This challenged my assumptions about urban sustainability

### The Technical Reality
My code is... basic. I'm sure a computer science student would look at it and see many things that could be improved. But it works, and more importantly, I understand every line of it.

The analysis isn't perfect either. I know there are more sophisticated statistical methods I could use, but I wanted to keep things simple and understandable.

## What I Learned: Beyond the Technical

### The Data Science Mindset
This project taught me that data science isn't just about programming—it's about asking good questions, being persistent when things don't work, and being honest about limitations.

I learned to:
- **Question my assumptions** (Why did I think Dublin would be most sustainable?)
- **Be transparent about methods** (I documented every decision I made)
- **Accept that perfect data doesn't exist** (I worked with what was available)
- **Focus on what's meaningful** (Rather than what's technically impressive)

### The Economics Connection
As an Economics student, this project helped me understand that sustainability metrics are economic indicators. Cities that score well on sustainability are investing in their long-term economic competitiveness.

The traditional economic focus on GDP misses important factors like environmental quality and social well-being. This project showed me how data science can help measure these "missing" economic indicators.

## The Limitations: Being Honest

### What I Didn't Do
- I didn't use machine learning or advanced statistical methods
- I didn't create a fancy web application (just basic HTML output)
- I didn't handle all the edge cases in the data
- I didn't do extensive sensitivity analysis
- I didn't create interactive visualizations

### What I Did Do
- I learned Python from scratch
- I figured out how to access and clean real data
- I implemented basic statistical analysis
- I created a reproducible methodology
- I documented everything clearly
- I made the results accessible to non-technical people

## Why This Matters for Trinity

### Demonstrating Growth Mindset
This project shows that I can learn new skills independently and apply them to real problems. I went from knowing zero programming to building a working data analysis pipeline.

### Showing Interdisciplinary Thinking
I connected concepts from Economics, Statistics, and Environmental Science. This is exactly the kind of interdisciplinary thinking that Trinity's program values.

### Proving Commitment
I spent over 100 hours on this project, mostly learning new skills. This shows genuine commitment to the field, not just academic interest.

### Real-World Application
I focused on solving a real problem (measuring urban sustainability) rather than just demonstrating technical skills. This aligns with Trinity's focus on applied statistics.

## The Future: What I Want to Learn

At Trinity, I want to:
- **Learn proper statistical methods** for sustainability analysis
- **Understand machine learning** approaches to environmental data
- **Study international comparisons** using similar methodologies
- **Develop policy recommendations** based on data-driven insights
- **Build more sophisticated models** while keeping them interpretable

## Conclusion: A Beginning, Not an End

This project represents my first serious attempt at data science. It's not perfect, but it's mine. I built it from scratch, learned every concept along the way, and can explain every decision I made.

The code is simple, the methodology is basic, and the results are preliminary. But it works, it's reproducible, and it taught me that I can learn data science and apply it to sustainability challenges.

I'm excited to continue this journey at Trinity, where I can learn the advanced methods that will help me build more sophisticated and impactful analyses.

---

*This project represents approximately 100 hours of learning, programming, and analysis. All code is available with detailed comments explaining my thought process. The methodology is documented step-by-step, including all the mistakes I made along the way.*

**Contact**: 22370072@studentmail.ul.ie | **GitHub**: [Your GitHub] | **LinkedIn**: [Your LinkedIn]
