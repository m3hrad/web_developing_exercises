import os.path
import json
from pprint import pprint
from glob import glob

class Song:
    def __init__(self,song_id):
        folder = "lastfm_subset/"+song_id[2]+"/"+song_id[3]+"/"+song_id[4]+"/"+song_id+".json";
        fileExists = False;
        if(os.path.exists(folder)):
            fileExists = True;
            with open(folder) as data_file:
                data = json.load(data_file);
        else:
            data = "";
        self.track_id = song_id
        if(fileExists ) :
            self.artist = data["artist"]
        else:
            self.artist = "file"
        if(fileExists ) :
            self.title = data["title"]
        else:
            self.title = "not found"
        if(fileExists ) :
            self.timestamp = data["timestamp"]
        else:
            self.timestamp = "-1"
        if(fileExists ) :
            self.tags = data["tags"]
        else:
            self.tags = []
        if(fileExists ) :
            self.similars = data["similars"]
        else:
            self.similars = []
    def get_tags(self,limit=0):
        result=[];
        for key, value in self.tags:
            if(float(value) > limit):
                result.append(key);
        return result;

    def get_similars(self,limit=0):
        result = []
        for key, value in self.similars:
            if(float(value) > limit):
                result.append(key);
        return result;

    def shared_tags(self,other_song):
        return tuple(list(set(self.get_tags()) & set(other_song.get_tags())));

    def combined_tags(self,other_song):
        resultList = list(set(self.get_tags()).union(set(other_song.get_tags())))
        return tuple(resultList);
