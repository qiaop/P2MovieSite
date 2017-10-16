#!/usr/bin/env python
# -*- coding:utf-8 -*-

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","A Story of a boy and his toys that come to life",
        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar","A marine on an alien planet",
        "http://upload.wikimedia.org/wikipedia/zh/b/b0/Avatar-Teaser-Poster.jpg",
        "http://www.youtube.com/watch?v=-9ceBgWV8io")

ironfist = media.Movie("羞羞的铁拳","开心麻花团队的一部爆笑力作",
        "https://img1.doubanio.com/view/photo/l/public/p2500484148.webp",
        "https://www.youtube.com/watch?v=GRR1ua5jEug")

movies = [toy_story,avatar,ironfist]
fresh_tomatoes.open_movies_page(movies)

