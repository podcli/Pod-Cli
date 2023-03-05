# Pod-Cli  

![podcli](https://user-images.githubusercontent.com/93109368/222878158-63097e03-6469-4cc3-bc86-dd12a97c0728.jpg)






## PROBLEM STATEMENT
Often, we find ourselves in situations where we can't spare enough time to listen to our beloved podcast. As technology enthusiasts, Pod-Cli transforms your humungous audio podcasts into text and provide you with a concise summary. The best part is that you can now enjoy listening to your favorite music while simultaneously reading the summarized text of your podcast.



## How Pod-Cli works:
1. It takes the audio from the YouTube/Spotify database or audio is provided and use Natural Language Processing and AI trained models to convert the speech into text files.
2. At first Audio is provided then it is given to the Assembly-ai api to come up with text file(basically converting audio to text).
3. The obtained raw file which contain fresly generated text,is then processed through regex and packages like nltk to summarize by removing stopwords,repetitions and complexity and using approaches like:
 (a)Extractive Summarization
 (b)Abstractive Summarization
 (c)frequency algorithm and through English syntax analysis

## INITIAL STAGE VS PRESENT STAGE OF THE PROJECT
 Intially, we approached an algorithm that first divided the audio files into chunks of smaller length, then these chunks were individually processed to extract the text, the problem with this model was installing a number of dependencies and their incompatibility with the OS. We shifted our focus to whisper AI api which is an OSS by Open AI but that also did not go very well because of accuracy issues. 
 At last, we found Assembly AI, handling the mp3 files with assembly AI is not at all complex, and the accuracy of the text generated is very almost perfect. The user need to get their own access token from their website, by following the commands given in "commands.txt" file a transcript.txt file is generated the file is then passed over to the "txtsumry.py" file that generates a short, crist and precise summary of the audio file instaniously. 
 The generation of transcript takes about 10% to 15% of the time of the original audio file.

## THIS INFOGRAPHIC SHOWS THE IMAPCT OF OUR TEXT DERIVED FROM THE AUDIO AND THE SUMMERIZED TEXT 
![ereu](https://user-images.githubusercontent.com/93109368/222952944-84f773cc-ba4a-4eb2-b588-16aae29298be.png)


## PACKAGES/API USED
1. nltk
2. assembly AI

## THIS INFOGRAPHIC SHOWS THE CONVERSION OF TEXT FILE TO SUMMERIZED FILE
### THE EXTRACTED TEXT 
 The following text file is generated when the ["transcribe.py"](https://github.com/podcli/Pod-Cli/blob/main/transcribe.py) script is executed in the terminal. this is the original text generated from the audio.
![WhatsApp Image 2023-03-05 at 1 57 03 PM](https://user-images.githubusercontent.com/93109368/222955115-6f1a6232-bc3a-4330-ab55-51a6736970f6.jpeg)
### THE SUMMERIZED TEXT
The following text file is generated when the ["txvsumry.py"](https://github.com/podcli/Pod-Cli/blob/main/txtsumry.py) script is executes in the terminal. this is the summerized version of the previous text file.
![WhatsApp Image 2023-03-05 at 1 57 21 PM](https://user-images.githubusercontent.com/93109368/222955226-68b98699-3685-4734-96f5-cc1c792c566d.jpeg)



