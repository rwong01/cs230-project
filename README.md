# CS230 Project - Pokémon Image & Text Generator

## Objectives
The goal of this project is to generate new Pokémon characters with both sprite images and description text to accompany it. We make use of the StyleGAN2-ADA library and CLIP library to complete the two halves of this project, first to generate images of characters, and then to pair it with generated text descriptions.
## Dataset Download
Download using an image scraper extenstion
* https://pokemondb.net/pokedex/national

## Dataset Santizing
Use a took like ImageMagick to make all images 128x128px and RGB format only, not RGBA. Use `dataset_tool.py` to validate dataset and generate a single package.

## Final Results
![Final_Results](https://raw.githubusercontent.com/rwong01/cs230-project/main/results_final.png)
![Final_Results](https://raw.githubusercontent.com/rwong01/cs230-project/main/finals_text.png)
## Libraries
* https://github.com/NVlabs/stylegan2-ada-pytorch LICENSE: [Nvidia Source Code License](https://nvlabs.github.io/stylegan2-ada-pytorch/license.html)
* https://github.com/openai/CLIP LICENSE: [MIT License](https://github.com/openai/CLIP/blob/main/LICENSE)
