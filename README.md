# SuperStylin

SuperStylin helps you put together new clothing combinations with your own clothing. It takes new trends from Instagram and fashion trends and applies them to what you already have, for any occasion. Just upload clean photos of your items laid out on the floor or bed, each one in full view. Not pictures of an open closet. The AI cleans them up, indexes them and categorizes them for you. Add new clothes as you go.

This repo is the public demo. One HTML file. No server, no account, no uploads. Open it and it runs.

## Run it

Open `index.html` in any browser. That is the whole install.

## What the demo does

- Shows a sample wardrobe of drawn placeholder pieces. They stand in for photos so you can see how it works without using any real clothes.
- Filters the wardrobe by category: tops, bottoms, shoes, layers, dresses.
- Style Me builds an outfit for an occasion, casual day, work, night out or big event, using only pieces in the wardrobe. Hit New combo for another one.
- Trend cards apply a current look to your own pieces. Apply one and Style Me has to build with it.
- Add a piece with the form and it stays in your wardrobe, saved in your browser only.

## How the full version works

Each piece starts as a clean photo of one item laid out on the floor or bed, in full view. The photo gets cleaned up and put on a white background, then indexed by category, color and occasion. Trends get read as simple rules, a color, a category, an occasion, and the outfit builder applies those rules to what you already own. This demo ships that same rule engine with sample trends and a sample wardrobe, so the whole idea runs in one file.

## Make it yours

Edit the `DEMO_ITEMS` list at the top of the script in `index.html`. Name, category, color and occasions are all it needs per piece. Add your own trends to the `TRENDS` list the same way.

## Privacy

Nothing leaves your machine. There are no network calls in this file at all, no analytics, no external images, no fonts, no libraries. Your added pieces live in your browser storage and nowhere else.

## License

MIT. See LICENSE.
