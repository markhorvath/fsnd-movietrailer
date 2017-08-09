#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:01:51 2017

@author: markhorvath
"""
import fresh_tomatoes
import media

step_brothers = media.Movie("Step Brothers",
                        "Call me Dragon",
                        "https://upload.wikimedia.org/wikipedia/en/d/d9/StepbrothersMP08.jpg",
                        "https://www.youtube.com/watch?v=8QKE96wZTkw")

avatar = media.Movie("Avatar",
                     "A movie about obtaining the cleverly named unobtainium",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

dark_knight = media.Movie("The Dark Knight",
                          "AKA why the third one could never have been better",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=qY3UkAHufLY")

last_jedi = media.Movie("Star Wars VIII: The Last Jedi",
                        "Jedi are in this one",
                        "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",
                        "https://www.youtube.com/watch?v=zB4I68XVPzQ")

inglourious_basterds = media.Movie("Inglourious Basterds",
                        "The most tense scene involving a glass of milk ever",
                        "https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",
                        "https://www.youtube.com/watch?v=KnrRy6kSFF0")

war_planet_apes = media.Movie("War for the Planet of the Apes",
                              "No Mark Wahlberg",
                              "https://upload.wikimedia.org/wikipedia/en/d/d7/War_for_the_Planet_of_the_Apes_poster.jpg",
                              "https://www.youtube.com/watch?v=3KWAxBlZKMA&index=12&list=PLScC8g4bqD45-Bue4BX7U2h4IkzEV3hcL")

movies = [step_brothers, avatar, dark_knight, last_jedi, inglourious_basterds, war_planet_apes]

fresh_tomatoes.open_movies_page(movies)
