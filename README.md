# Pod-Cli  
PodCli is a opensource and free software that delivers short and crisp summaries to lengthy and boring videos and audios of Podcast.
![podcli](https://user-images.githubusercontent.com/93109368/222878158-63097e03-6469-4cc3-bc86-dd12a97c0728.jpg)






## PROBLEM STATEMENT
Often, we find ourselves in situations where we can't spare enough time to listen to our beloved podcast. As technology enthusiasts, Pod-Cli transforms your humungous audio podcasts into text and provide you with a concise summary. The best part is that you can now enjoy listening to your favorite music while simultaneously reading the summarized text of your podcast.



## How Pod-Cli works:
1. We take the data from the YouTube/Spotify database and use [Natural Language Processing](https://www.ibm.com/in-en/topics/natural-language-processing) to convert the speech into [text files](https://en.wikipedia.org/wiki/Text_file).
2. The obtained transcript are then processed through [regex](https://regex101.com) to shorten it by removing repetitions and complexity.
3. It is then given to the [GPT-3](https://openai.com/product) api to come up with a summary.
Tech Stack: [Python](http://www.python.org)/[Java](https://www.java.com/en/), [Bash Scripting](https://www.javatpoint.com/bash-scripting).

## INITIAL STAGE VS PRESENT STAGE OF THE PROJECT
 Intially, we approached an algorithm that first divided the audio files into chunks of smaller length, then these chunks were individually processed to extract the text, the problem with this model was installing a number of dependencies and their incompatibility with the OS. We shifted our focus to whisper AI api which is an OSS by Open AI but that also did not go very well because of accuracy issues. 
At last, we found Assembly AI, handling the mp3 files with assembly AI is not at all complex, and the accuracy of the text generated is very almost perfect. The user need to get their own access token from their website, by following the commands given in "commands.txt" file a transcript.txt file is generated the file is then passed over to the "txtsumry.py" file that generates a short, crist and precise summary of the audio file instaniously. 
The generation of transcript takes about 10% to 15% of the time of the original audio file.

## THIS INFOGRAPHIC SHOWS THE IMAPCT OF OUR TEXT DERIVED FROM THE AUDIO AND THE SUMMERIZED TEXT 
![ereu](https://user-images.githubusercontent.com/93109368/222952944-84f773cc-ba4a-4eb2-b588-16aae29298be.png)


## optional packages/api:
1. Speech recognition engine/API support
2. CMU Sphinx (works offline)
3. Google Speech Recognition
4. Google Cloud Speech API
5. Wit.ai
6. Microsoft Bing Voice Recognition
7. Houndify API
8. IBM Speech to Text
9. Snowboy Hotword Detection (works offline)
