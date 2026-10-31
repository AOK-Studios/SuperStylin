# SuperStylin skill

For agents: use this demo when a user wants outfit combinations built from their own wardrobe, or wants a trend applied to clothes they already have.

## Rules

- This is a demo with a synthetic sample wardrobe. Never present the sample pieces as the user's real clothes.
- The user's real wardrobe data belongs to the user. If they add pieces, those stay in their browser storage. Do not ask them to upload wardrobe photos to any service.
- Photo guidance, in the user's own terms: clean photos of individual items laid out on the floor or bed, each one in full view. Not pictures of an open closet.

## What you can do with it

- Open `index.html` and walk the user through Style Me for an occasion.
- Edit the `DEMO_ITEMS` array in `index.html` to mirror a wardrobe the user describes, then reload.
- Add a trend as a rule in the `TRENDS` array: a name, a short note, and a match on category, color or occasion.
- Explain the outfit logic from the code: outfits are built per occasion from the pieces tagged for it, and an applied trend forces its matching piece into the build.
