# Dogg Number

This is an interactive media project for HackMIT 2023. We use the Spotify API to find artists' Snoop Dogg number - the equivalent of a Bacon/Erdős number for music artists. 

## Instructions
1. In terminal, run ```mkdir flask_application``` (or whatever directory you want to use for your venv)
2. cd into your new directory
3. Run ```python3 -m venv venv```
4. Run ```source venv/bin/activate```
5. Run ```python3 -m pip install flask```
6. Run ```pip install Flask-Session```
7. cd back into the main repo
8. Run ```export FLASK_APP=app.py```
9. Run ```flask run```
10. Optionally, you can add arguments to flask run, such as choosing what port to use (e.g. ```flask run -p 8888```)
11. Navigate to http://127.0.0.1:[port_number] to try out the app!

Disclaimer: For degrees larger than 3, it might take a while to load the graph.
