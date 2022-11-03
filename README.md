# Language Classifier
## Using Single Layer Network of Perceptrons

<p>
The aim of the project is to create a single-layer network to identify the language an input text is written in.
Files contains a set of texts written in four languages – English, Polish, German and Uzbek. To classify a given text, it counts the number of occurences of each letter of the latin alphabet. Ignores all other characters – only counts the frequencies of the 26 letters of the latin alphabet.
</p>

<p>
For each text, it generates a 26-element input vector containing the number of occurences of each letter. Then normalize it:

```
vˆ = v / |v|
```
</p>

<p>
The output of the network has local representation: one neuron is assigned to each language. For a given text only the appropriate neuron should have value 1 and all others 0. To classify an input text, it selects the neuron with the maximum activation.
</p>
