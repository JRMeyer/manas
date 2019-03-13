for i in *.txt; do cat "${i}" | apertium -d ~/source/apertium//languages/apertium-kir/ kir-tagger > "${i}.tagged"; done

