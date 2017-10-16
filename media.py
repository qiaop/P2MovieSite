#!/usr/bin/env python
# -*- coding:utf-8 -*-
import webbrowser

class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        """Constructor

        Keyword arguments:
        self -- instance self
        movie_title -- 电影标题
        movie_storyline -- 故事简介
        poster_image -- 海报图片链接
        trailer_youtube -- 预告片YouTube播放链接
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """show trailer，Open the webbrowser to play the vedio
        Keyword arguments:
        self -- instance self
        """
        webbrowser.open(self.trailer_youtube_url)
