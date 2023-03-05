# Pod-Cli
![podcli](https://user-images.githubusercontent.com/93109368/222878158-63097e03-6469-4cc3-bc86-dd12a97c0728.jpg)


![PROBLEM STATEMENT](https://user-images.githubusercontent.com/93109368/222948308-f2b00ba8-d771-430a-8346-e090be1d9960.jpg)

PodCli is a opensource and free software that delivers short and crisp summaries to lengthy and boring videos and audios of Podcast.
## How PodCli works:
1. We take the data from the YouTube/Spotify database and use [Natural Language Processing](https://www.ibm.com/in-en/topics/natural-language-processing) to convert the speech into [text files](https://en.wikipedia.org/wiki/Text_file).
2. The obtained transcript are then processed through [regex](https://regex101.com) to shorten it by removing repetitions and complexity.
3. It is then given to the [GPT-3](https://openai.com/product) api to come up with a summary.
Tech Stack: [Python](http://www.python.org)/[Java](https://www.java.com/en/), [Bash Scripting](https://www.javatpoint.com/bash-scripting).

## optional pacakages/api:
1. Speech recognition engine/API support
2. CMU Sphinx (works offline)
3. Google Speech Recognition
4. Google Cloud Speech API
5. Wit.ai
6. Microsoft Bing Voice Recognition
7. Houndify API
8. IBM Speech to Text
9. Snowboy Hotword Detection (works offline)
