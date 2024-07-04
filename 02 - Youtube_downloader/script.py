from pytube import YouTube
from pytube import Playlist
from slugify import slugify
from datetime import datetime

def generateOutputPath(author, playlist = ""):
    author = slugify(author)
    if playlist == "":
        path = "./downloaded-vids/"+author
    else:
        playlist = slugify(playlist);
        path = "./downloaded-vids/"+author+"/"+playlist;
    return path;

def downloadVideo(video, playlist = "", index = "", isOnlySound = False):
    if video.age_restricted == True:
        print("La video est soumise a une limite d'âge et ne peux donc pas être téléchargée.")
        return
    else:
        outputPath = generateOutputPath(video.author, playlist);
        prefix = index + " - " if index != "" else "";
        extention = ".mp3" if isOnlySound == True else ".mp4";
        fileName = prefix + slugify(video.title) + extention
        print("Téléchargement de: "+ video.title)

        if isOnlySound == True:
            video.streams.get_audio_only().download(outputPath, fileName)
        else:
            video.streams.get_highest_resolution().download(outputPath, fileName);

        print("Téléchargement terminé !");

def downloadPlaylist(playlistUrl, isOnlySound = False):
    playlist = Playlist(playlistUrl)
    playlistVideo = playlist.videos;
    for index, video in enumerate(playlistVideo):
        downloadVideo(video, playlist.title, str(index), isOnlySound);
    print("Toute la playlist à bien été téléchargée.")

# Demander ce que souhaite télécharger l'utilisateur (video, playlist)
downloadType = input("Que souhaitez vous télécharger ?\n1. Une playlist\n2. Une video\n");
onlySound = input("Souhaitez vous ne télécharger que le son ?\n1. Oui\n2. Non\n")

isOnlySound = True if onlySound == "1" else False;

if downloadType == "1":
    # Si playlist demander url de la playlist
    playlistUrl = input("Url de la playlist: ");
    # Telecharger la playlist
    playlist = Playlist(playlistUrl);
    downloadPlaylist(playlistUrl);

if downloadType == "2":
    # Si video demander url de la video
    videoUrl = input("Url de la video: ");
    video = YouTube(videoUrl);
    # video.streams.get_highest_resolution().download(outputPath, fileName);
    # Telecharger la video
    downloadVideo(video, isOnlySound=isOnlySound)