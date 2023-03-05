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
 Intially we tried to run using python.....blah blah blahh,  
 vaibhav
 ake 
 bolega

## THIS INFOGRAPHIC SHOWS THE IMAPCT OF OUR TEXT DERIVED FROM THE AUDIO AND THE SUMMERIZED TEXT 
![summerization](https://user-images.githubusercontent.com/93109368/222952904-e75ad3c3-de5d-4bed-a8c8-553a1d38c70d.jpg)

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
