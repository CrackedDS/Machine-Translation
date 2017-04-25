# Machine-Translation
NOTE: Code Cleaning, still in progress to make the code more readable to a 3rd party.

Approaching Machine Translation by designing and coding a RNN from ground up.

INTRODUCTION:
The objective was to translate an input sentence in a language to produce an output sentence in the target language. The chosen input language was English and the target language was Spanish. Although the designed Neural Network was trained on this dataset, the same neural network can be retrained to operate for different sets of weights over any input and output language.

TRACK THE WORKS:
•	Conversion from word to number:
The first obstacle of the project was to find a way to map the word vector (sentence) into a real number space. Decided to use the ASCII equivalent of each character in the word. This is done by using the inbuilt function of Python called ord(). The resulting number from this conversation is then brought between 1 and 26 to reduce the size of each translated word because the ASCII values of some of the characters are 3 digit numbers. This way, the input sentence (sequence of words) can be converted into its equivalent number sequence.

•	Converting the variable length input vector to a fixed length input vector:
The input sentence can be of any length. Since the length of the sentence is not known beforehand, the RNN design gets complicated as it would require a lot of preprocessing of the data before it can be fed into the neural net. Hence, decided to convert the variable length input into a fixed length feature vector. Then found the average length of a sentence in both languages and fixed that as the size of the feature vector. The size was 26.

o	Initial Approach:
Initially just concatenated the words in the sentence to get the fixed length size. For example, “Hello World” became “HelloWorld”. This happened only when the size exceeded 26. But the performance of the neural net on this data was extremely bad. Hence, moved to the next approach.

o	Final Approach – Auto Encoder Design:
For this approach decided to limit the dataset to contain sentences which are of size less than 29. This is not necessary but if longer sentences are done, many iterations of the auto encoder has to be run since reducing the sentence length for more than 5 in one iteration will reduce the performance of the encoder. This will increase the number of weights that are being calculated and to avoid the complexity, limited the dataset to sentences of length less than or equal to 29. The minimum length of the sentence was set to 26 because otherwise the sentence when appended with ‘nonsense’ words to make it 29 will have many repetitions in a feature in the final feature vector (mostly in the last couple features). Now, the encoder will take in 29 length vector as input and the middle level of the encoder will be 26 length which is collected and given as input to the RNN. This encoder was trained and the weights are stored in a file.

•	Neural Network – Recurrent Neural Network Design:
The 26-length feature vector is passed as input to the RNN. The RNN has 3 hidden nodes and 1 output node. While 26 features are passed into the neural net 3 at a time. For example, if the input was ‘1 2 3 4 5’, it’s passed as ‘1 2 3’, ‘2 3 4’, ‘3 4 5’, ‘4 5 1’, ’5 1 2’. Each feature goes as an input into the each of the hidden node. Each hidden node has a connection with itself and the other 2 nodes. After this step, the three outputs from the hidden nodes is passed to 1 output node and the output node passes input to itself. That is, output at time ‘t’ is passed as a feature to the output node at time ‘t+1’.  The output of the RNN will be a 26-length feature vector as there are 26 words in the input vector. Now this 26-length feature vector is passed as input into the middle level of the auto encoder for Spanish which was trained before. This will spit out a Spanish equivalent number vector. This is then converted into a word vector from the mapping that is stored while converting the words to numbers. The RNN itself is unrolled in time over 5 time steps before passing in the next input. Till 5 time steps, the RNN trains itself by updating its hidden node weights. After 5 time steps, the input is passed to it. Finally, the RNN is trained over many epochs on the dataset to observe convergence of the weights. 

FUTURE DEVELOPMENT:
•	The RNN can be trained over many more epochs and with a much larger dataset. 
•	More hidden nodes can be added to the RNN which will increase the complexity of the system but might improve the performance. 
•	Multiple levels of the Auto Encoder can be implemented to accommodate much larger sentences.

NOTE:
Check for diagrams of the RNN and the Auto Encoder in the files.
