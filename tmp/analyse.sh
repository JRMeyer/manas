for i in *.txt; do cat "${i}" | apertium -d ~/source/apertium//languages/apertium-kir/ kir-tagger > "${i}.tagged"; done
for i in *.txt; do cat "${i}" | python3 ngrams.py 3 > "${i}.trigrams"; done

