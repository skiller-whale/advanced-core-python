from contextlib import ExitStack

def round_robin(streams, words):
    word_idx = 0
    while True:
        for stream in streams:
            stream.write(words[word_idx] + "\n")
            word_idx += 1
            if word_idx == len(words):
                break

txt_files = [f'data/word_set_{i}.txt' for i in range(7)]
sentence = "It is with the utmost pleasure that I now share with you the tale of William Shakespaw, a cat who dared to go where no other cat ever dared before"
words = sentence.split(" ")

with ExitStack() as stack:
    streams = [stack.enter_context(open(fname, "w")) for fname in txt_files]
    round_robin(streams, words)


round_robin(5)